# Imported django built in modules
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# # Adding Custom FIelds to DJ builtin form
# class CustomUserField(AbstractUser):
#     email = models.EmailField(max_length=30, null=False, blank=False)
#     phone = models.PositiveIntegerField(null=False, blank=False)
#     address = models.CharField(max_length=50, null=False, blank=False)

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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        # return reverse_lazy('home')


class Profile(models.Model):
    name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE,)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)


    

    