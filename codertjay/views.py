from django.shortcuts import render
from .forms import ContactForm
from coding.models import BlogPost


def home_page(request):
    my_title = "Hello there..."
    qs = BlogPost.objects.all()[:5]
    context = {'title': 'Welcome to PrimeWorld','blog_list': qs}
    return render(request, 'codertjay/home_page.html',context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {'title': 'contact us', 'form': form}
    return render(request, 'codertjay/contact_page.html', context)


def about_page(request):
    return render(request, 'codertjay/about_page.html')
