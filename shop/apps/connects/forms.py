from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    fullName = forms.CharField(label='نام و نام خوانوادگی', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی را بنویسید'}))
    email = forms.CharField(label='ایمیل', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل را بنویسید'}))
    mobile = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موبایل را بنویسید'}))
    text = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام را بنویسید'}))

    class Meta:
        model = Message
        fields = '__all__'
    