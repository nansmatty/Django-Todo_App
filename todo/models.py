from django.db import models
# from datetime import datetime

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title