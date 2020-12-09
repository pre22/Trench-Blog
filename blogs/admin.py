from django.contrib import admin
from blogs.models import ContactModel, Post, CategoryTable, Comment
from django.contrib.auth.admin import UserAdmin
# from blogs.forms import CustomUserCreationForm, CustomUserChangeForm
# from blogs.models import CustomUserField


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUserField


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]



admin.site.register(Post, PostAdmin)
admin.site.register(ContactModel)
admin.site.register(CategoryTable)
admin.site.register(Comment)
# admin.site.register(CustomUserField, CustomUserAdmin)