"""定义learning_logs的URL"""
from django.urls import path, re_path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry,
            name='edit_entry'),
]
app_name = 'learning_logs'
