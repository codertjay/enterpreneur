from django.contrib import admin
from coding.models import BlogPost,BlogComment,BlogPostLike,BlogPostUnlike


class BlogPostLikeModelAdmin(admin.TabularInline):
    model = BlogPostLike


class BlogPostUnlikeModelAdmin(admin.TabularInline):
    model = BlogPostUnlike

class PostModelAdmin(admin.ModelAdmin):
    inlines = [BlogPostLikeModelAdmin,BlogPostUnlikeModelAdmin]
    list_display = ["title", "updated", "timestamp", "slug"]
    list_display_links = ["updated"]
    list_filter = ["title", 'slug']
    search_fields = ['title', 'slug']
    list_editable = ['title', 'slug']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, PostModelAdmin)
