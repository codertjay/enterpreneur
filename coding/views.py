from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from .forms import BlogPostModelForm, BlogPostForm,BlogPostUnlikeForm,BlogPostLikeForm
from django.shortcuts import render, redirect
from .models import BlogPost
from django.shortcuts import get_object_or_404
from .forms import CommentForm


def blog_list_view(request):
    now = timezone.now()
    # queryset = BlogPost.objects.get_queryset()
    queryset = BlogPost.objects.published()
    context = {
        'post': queryset
    }

    return render(request, 'coding/list.html', context)


def blog_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = CommentForm(request.POST or None)
    context = {'post': obj}
    # , 'form': form
    try:
        if request.user.is_authenticated:
            user = request.user
            form.user = user
            # print(request.POST,form.user)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('blog:blog_detail', slug=slug)
    except:
        messages.error(request,"in valid form ")
        return redirect('blog:blog_detail', slug=slug)
    return render(request, 'coding/detail.html', context)


# @login_required
@staff_member_required
def blog_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.content = form.cleaned_data.get('content')
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    context = {'form': form}
    return render(request, 'coding/create.html', context)


@staff_member_required
def blog_update_view(request, slug):
    print('Django says:', request.method, request.path, request.user)
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blog:blog_list')

    context = {'post': obj, 'form': form, 'title': f'Update {obj.title}'}
    return render(request, 'coding/update.html', context)


@staff_member_required
def blog_delete_view(request, slug):
    print('Django says:', request.method, request.path, request.user)
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:blog_list')
    context = {'post': obj}
    return render(request, 'coding/delete.html', context)


def blog_category_view(request, category):
    if category == 'Music':
        queryset = BlogPost.objects.filter(category__iexact='Music')
        context = {'post': queryset}
    elif category == 'Comedy':
        queryset = BlogPost.objects.filter(category__icontains='Comedy')
        context = {'post': queryset}
    else:
        queryset = BlogPost.objects.filter(category__icontains='Comedy')
        context = {'post': queryset}
    return render(request, 'coding/category.html', context)


def blog_post_action(request,slug):
    print('Not working')
    form_like = BlogPostLikeForm(request.POST)
    form_unlike = BlogPostUnlikeForm(request.POST)
    context = {'formlike': form_like, 'formunlike': form_unlike}
    try:
        blog = get_object_or_404(BlogPost,slug=slug)
        form_like = BlogPostLikeForm(request.POST)
        form_unlike = BlogPostUnlikeForm(request.POST)
        print('none',request.POST)
        if form_like.is_valid():
            user = form_like.cleaned_data['user']
            if user in blog.like.all():
                messages.error(request,'You have already liked this post')
                return redirect('blog:blog_list')
            else:
                blog.like.add(user)
                return redirect('blog:blog_list')
        if form_unlike.is_valid():
            user = form_like.cleaned_data['user']
            if user in blog.unlike.all():
                messages.error(request,'You have already unlike this post')
                return redirect('blog:blog_list')
            else:
                blog.like.remove(user)
                messages.error(request,'You have already liked this post')
                return redirect('blog:blog_list')
        else:
            messages.error(request, 'There was an error ')
    except:
        messages.error(request, 'There was an error ')
    finally:
        messages.error(request, 'There was an error ')
    return render(request,'coding/detail.html',context)
