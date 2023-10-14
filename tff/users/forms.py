from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('id' , 'text' , 'image' ,'weight' ,   'user_pop')