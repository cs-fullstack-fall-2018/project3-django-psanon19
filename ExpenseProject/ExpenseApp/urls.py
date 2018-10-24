from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('user/',views.index, name='index'),
    path('createUser/', views.createUser, name='createUser'),
    path('admin/', admin.site.urls),
    path('deposit/<int:pk>/', views.deposit, name='deposit'),
]


