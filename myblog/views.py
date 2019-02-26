from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post


def index(request):
    '''首页'''
    post = Post.objects.all()
    context = {}
    context['post_list'] = post
    return render(request, 'myblog/index.html', context)


# 文章详情页
def detail(request, post_id):
    return HttpResponse("这是{0}文章详情页".format(post_id))


# 文章分类页
def cate(requests, cate_id):
    return HttpResponse("这是{0}分类".format(cate_id))


# 登录页面
def logIn(request):
    return HttpResponse("这是登录页")


# 注册页面
def register(request):
    return HttpResponse("这是注册页")