from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task , name='delete'),
    path('register/' , views.register_user , name='register') , 
    path('login/' , views.login_user , name='login')
]