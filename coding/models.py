from PIL import Image
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

choices = (
    ('M', 'Music'),
    ('C', 'Comedy'),
    ('L', 'Lifestyle'),
    ('E', 'Education'),
)

User = settings.AUTH_USER_MODEL


class BlogPostQueryset(models.QuerySet):
    def published(self):
        now = timezone.now()
        """this get_queryset() means BlogPost.objects  so you can add all or filter"""
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(content__icontains=query) |
                  Q(user__username__icontains=query) |
                  Q(slug__icontains=query)
                  )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQueryset(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()

        return self.get_queryset().published().search(query)



class BlogPostLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey('BlogPost',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class BlogPostUnlike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey('BlogPost',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)



class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=3, default=1, choices=choices)
    image = models.ImageField(default='Post_pic.jpg', upload_to='Blog_image',width_field="width_field",
            height_field="height_field")
    width_field = models.IntegerField(default=1)
    height_field = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    view_count = models.IntegerField(default=0)
    like = models.ManyToManyField(User,related_name='post_like',blank=True,through=BlogPostLike)
    unlike = models.ManyToManyField(User,related_name='post_unlike',blank=True,through=BlogPostUnlike)
    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        count1 = self.like
        count2 = self.unlike
        return f'{self.title}-like-{count1}-unlike-{count2}'

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    def get_update_url(self):
        return f'/blog/{self.slug}/update/'

    def get_delete_url(self):
        return f'/blog/{self.slug}/delete/'

    def save(self, **kwargs):
        super().save()

        """ but not that if you want to override the saved image you must install Image from PIL
         here i am opening the image"""
        img = Image.open(self.image.path)

        if img.height > 1000 and img.width > 800:
            output_size = (1000, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)


class BlogComment(models.Model):
    user = models.ForeignKey(User, null=True,  on_delete=models.SET_NULL)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


