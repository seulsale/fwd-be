"""fwd_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from todo import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewset, base_name='Category')
router.register('todos', views.NoteViewset, base_name='Note')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/<str:username>/', views.Notas.as_view()),
    path('api/todos/<str:username>/<int:id_todo>/', views.EliminarNota.as_view()),
    path('api/', include(router.urls))
]
