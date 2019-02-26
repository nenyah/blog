from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/5/
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /cate/1/
    path('cate/<int:cate_id>/', views.cate, name='cate'),
    # ex: /login/
    path('login', views.logIn, name='login'),
    # ex: /register/
    path('register', views.register, name='register'),
]
