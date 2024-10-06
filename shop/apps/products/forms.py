from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(label="نام", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))
    text = forms.CharField(label="متن پیام", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر خود را بنویسید'}))
    class Meta:
        model = Comment
        fields = ['name', 'text']