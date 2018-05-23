"""为应用程序user定义URL模式"""

from django.urls import path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登录页面
    path('login/', login, {'template_name': 'users/login.html'},
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]
app_name = 'users'