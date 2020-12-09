from django import forms
from blogs.models import ContactModel, Comment

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
