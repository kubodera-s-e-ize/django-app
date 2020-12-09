from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .models import Todo

# Create your views here.

@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            'todos': todos
        }
        return render(request, 'todo/index.html', context)
    elif request.method == "POST":
        print(request.POST)
        todo = Todo(title=request.POST['title'], content=request.POST['content'], status=True if request.POST['status'] == "true" else False)
        todo.save()
        return HttpResponseRedirect(reverse('index'))


@require_http_methods(['GET'])
def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)


@require_http_methods(['POST'])
def edit(request, id):
    todo = Todo.objects.get(id=id)
    todo.title = request.POST['title']
    todo.content = request.POST['content']
    todo.status = True if request.POST['status'] == "true" else False
    todo.save()
    return HttpResponseRedirect(reverse('detail', args=(id,)))


@require_http_methods(['POST'])
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
