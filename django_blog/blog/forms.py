# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget 

class PostForm(forms.ModelForm):
    tags = forms.CharField(widgets=TagWidget())  # Use TagWidget to handle the tags input

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in the form fields


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
