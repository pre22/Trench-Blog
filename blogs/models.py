from django.db import models
from django.contrib.auth.models import User

class CategoryTable(models.Model):
    name = models.CharField(max_length=25, default='General')
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,) # Allows for many to one relationship
    category = models.ForeignKey(CategoryTable, null=True, on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

    