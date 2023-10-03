from django.shortcuts import render
from users.models import User , Post
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = Post.objects.all().select_related('user_pop')
    return render(request,'main/main.html' ,{"data":data})

