from django.shortcuts import render
from coding.models import BlogPost
from .models import SearchQuery


def search_view(request):
    qs = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': qs}
    if qs is not None:
        SearchQuery.objects.create(user=user, query=qs)
        blog_list = BlogPost.objects.all().search(query=qs)
        context['blog_list'] = blog_list
    return render(request, 'searchapp/search.html', context)
