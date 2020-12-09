from django.db import models

# Create your models here.

class Todo(models.Model):

    def __str__(self):
        return self.title
    
    title = models.TextField(max_length=20)
    content =  models.TextField(max_length=100)
    status = models.BooleanField()

