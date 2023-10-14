from django.shortcuts import render , redirect
from django.views import View
from .forms import UserCreationForm , PostForm
from django.contrib.auth import authenticate , login
from django.views.decorators.csrf import csrf_exempt,csrf_protect
class Registr(View):
    templates_name = 'registration/registr.html'
    def get(self, request):
        context = {
            "form":UserCreationForm()
        }
        return render(request, self.templates_name , context)
    def post(self, request):
        form = UserCreationForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('login')
        
        context={
            "form":form
        }
        return render(request , self.templates_name , context)


def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            post_obj = form.instance
            return render(request, 'main/upload_post.html', {post_obj:"post_obj"})
    else:
        form = PostForm()
    return render(request,  'main/upload_post.html', {'form':form})

