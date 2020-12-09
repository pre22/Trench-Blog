from django import forms
from blogs.models import ContactModel, Comment
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from blogs.models import CustomUserField


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUserField
#         fields = UserCreationForm.Meta.fields + ('email', 'phone', 'address',)

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUserField
#         fields = UserChangeForm.Meta.fields



class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
