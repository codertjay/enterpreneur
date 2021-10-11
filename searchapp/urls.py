from django.urls import path
from .views import search_view

app_name='searchapp'
urlpatterns = [
    path('', search_view, name='search_blog')
]

