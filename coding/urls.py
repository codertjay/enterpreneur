from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', blog_list_view, name='blog_list'),
    path('<str:slug>/', blog_detail_view, name='blog_detail'),
    path('<str:slug>/update/', blog_update_view, name='blog_update'),
    path('<str:slug>/delete/', blog_delete_view, name='blog_delete'),
    path('<str:slug>/like/', blog_post_action, name='blog_action'),

]


