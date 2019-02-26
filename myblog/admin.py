from django.contrib import admin

# Register your models here.
from .models import (Banner, Category, Comment, EmailVerifyRecord,
                     FriendlyLink, Post, Tags)

# class TagsInline(admin.TabularInline):
#     model = Tags
#     extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'was_published_recently')
    # fieldsets = [
    #     (None, {
    #         'fields': ['title', 'author', 'content']
    #     }),
    #     ('浏览信息', {
    #         'fields': ['views'],
    #         'classes': ['collapse']
    #     }),
    # ]
    # inlines = [TagsInline]
    list_filter = ['create_date']
    search_fields = ['content']


admin.site.register(EmailVerifyRecord)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(FriendlyLink)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags)