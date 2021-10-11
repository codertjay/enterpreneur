from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import user_register_view, profile_view

app_name = 'users'
urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
