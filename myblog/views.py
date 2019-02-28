import random
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm


def index(request):
    '''首页'''
    posts = Post.objects.all()
    context = {}
    context['post_list'] = posts
    return render(request, 'myblog/index.html', context)


# 文章详情页
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']
            avatar = f'images/avatar/avatar{random.randint(0,24)}.jpg'
            comment = Comment(
                post=post,
                user=user,
                content=content,
                email=email,
                avatar=avatar)
            comment.save()
            return redirect(to='blog:detail', post_id=post_id)
            # print(user, content, email)
        # print(form.errors)

    tags = post.tags.all()
    if request.method == 'GET':
        post.views += 1
        post.save()
    context = {}
    context['post'] = post
    context['tags'] = tags
    context['form'] = form
    context['comments'] = comments
    return render(request, 'myblog/detail.html', context)


# 文章分类页
def cate(request, cate_id):
    posts = Post.objects.filter(category__id=cate_id)
    context = {}
    context['post_list'] = posts
    return render(request, 'myblog/category.html', context)


# 文章标签页
def tag(request, tag_id):
    posts = Post.objects.filter(tags__id__exact=tag_id)
    context = {}
    context['post_list'] = posts
    return render(request, 'myblog/category.html', context)


# 登录页面
def logIn(request):
    return HttpResponse("这是登录页")


# 注册页面
def register(request):
    return HttpResponse("这是注册页")
