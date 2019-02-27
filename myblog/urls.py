from django.conf.urls.static import static
from django.urls import path

from . import views
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/5/
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /cate/1/
    path('cate/<int:cate_id>/', views.cate, name='cate'),
    # ex: /tag/1/
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    # ex: /login/
    path('login', views.logIn, name='login'),
    # ex: /register/
    path('register', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
