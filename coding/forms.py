from django import forms
from .models import BlogPost, BlogComment, BlogPostLike, BlogPostUnlike
from django.contrib.auth.models import User


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError('This is not a valid title')
        print(title)
        return title


class BlogPostModelForm(forms.ModelForm):
    title = forms.CharField(max_length=200)

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'image', 'publish_date']

    def clean_title(self, *args, **kwargs):
        #  print(dir(self)) to check method that are related to this file
        instance = self.instance
        # print(instance) checking if the instance is gonna give me the name of the file if i am updating
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            """what this statement is doing is that if there is
             an instance i dont what any validation on the instance
              just like when i am updating the view so if i use the same
               name it wont give me validation error"""
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('This is not a valid title')
        print(title)
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']

    def _clean_form(self):
        if User.is_authenticated:
            BlogComment.user = User


class BlogPostUnlikeForm(forms.ModelForm):
    class Meta:
        model = BlogPostUnlike
        fields = ['user']


class BlogPostLikeForm(forms.ModelForm):
    class Meta:
        model = BlogPostLike
        fields = ['user','blog']
