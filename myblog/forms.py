from django import forms


class CommentForm(forms.Form):
    user = forms.CharField(max_length=50)
    content = forms.CharField()
    email = forms.EmailField()