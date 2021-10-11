from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from coding.views import blog_create_view, blog_category_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('coding.urls')),
    path('user/', include('users.urls')),
    path('search/', include('searchapp.urls')),
    path('codertjay/', include('codertjay.urls')),
    path('blog_new/', blog_create_view, name='blog_create'),
    path('<str:category>/', blog_category_view, name='blog_category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

