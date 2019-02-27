# Create your models here.

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# class BlogUser(AbstractUser):
#     nikename = models.CharField('昵称', max_length=20, default='')


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50, default='')
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(
        verbose_name="验证码类型",
        choices=(("register", "注册"), ("forget", "找回密码"), ("update_email",
                                                          "修改邮箱")),
        max_length=30)
    send_time = models.DateTimeField(
        verbose_name="发送时间", auto_now_add=True, editable=True)

    class Meta:
        verbose_name = "邮箱验证码"
        # 复数
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='banner')
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('激活状态', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


class Category(models.Model):
    '''
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    '''
    name = models.CharField('分类名称', max_length=100, default='')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'

    def __str__(self):
        return self.name


class Tags(models.Model):
    '''标签'''
    name = models.CharField('标签名称', max_length=100, default='')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    '''文章'''
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django
    # 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(
        User, verbose_name='作者', on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=70, verbose_name='标题')

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    content = models.TextField('内容')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    create_date = models.DateTimeField(
        '创建日期', auto_now_add=True, editable=True)
    update_date = models.DateTimeField('更新日期', auto_now=True, null=True)

    # 博客封面，浏览数，推荐博客
    cover = models.ImageField('博客封面', upload_to='post', default=None)
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    category = models.ForeignKey(
        Category, verbose_name='博客分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, verbose_name='标签', blank=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_date <= now

    was_published_recently.admin_order_field = 'create_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布?'

    class Meta:
        # 按时间下降排序
        ordering = ['-create_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"


class Comment(models.Model):
    '''评论模型'''
    post = models.ForeignKey(Post, verbose_name='博客', on_delete=models.CASCADE)
    user = models.CharField('评论者', blank=True, max_length=50)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)
    content = models.TextField('内容')
    email = models.EmailField('邮箱', max_length=50)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class FriendlyLink(models.Model):
    '''友情链接'''
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
