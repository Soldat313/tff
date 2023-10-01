from django.urls import path, include
from django.views.generic import TemplateView
from .views import Registr
from . import views

urlpatterns = [
   path('', include('django.contrib.auth.urls')),
   path('registr/' , Registr.as_view(), name='registr'),
   path('upload_post/', views.upload_post , name='create_post')
]
