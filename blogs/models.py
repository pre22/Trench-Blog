from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,) # Allows for many to one relationship
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
    
class CategoryTable(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    