"""
URL configuration for tff project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from chat.views import chatbox

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/' , include('users.urls'), name='users'),
    path('main/' , include('main.urls'), name='main'),
    path('' , TemplateView.as_view(template_name='main/er403.html'), name='er'),
    path('chat/<str:chat_box_name>/', chatbox , name='chat'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)