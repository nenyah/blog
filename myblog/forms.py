import re
from django import forms
from django.core.exceptions import ValidationError


def word_length_validator(comment):
    if len(comment) < 10:
        raise ValidationError("字数不能少于10!")


def forbid_word_validator(comment):
    if 'a' in comment:
        raise ValidationError("内容不能出现禁用词！")


def without_chinese_validator(comment):
    partern = re.compile('[\u4e00-\u9fa5]')
    match = partern.search(comment)
    if not match:
        raise ValidationError("内容中没有中文！")


class CommentForm(forms.Form):
    content = forms.CharField(
        label='内容',
        widget=forms.Textarea({
            'placeholder': '评论必需包含中文，无中文评价将会导致评论失败',
        }),
        validators=[
            word_length_validator, forbid_word_validator,
            without_chinese_validator
        ])
    user = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.TextInput({
            'placeholder': '昵称',
        }))
    email = forms.EmailField(
        label='邮箱', widget=forms.TextInput({
            'placeholder': '邮箱',
        }))
