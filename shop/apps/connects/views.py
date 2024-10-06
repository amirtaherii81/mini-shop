from django.shortcuts import render, redirect
from django.views import View
from .models import Message
from .forms import MessageForm
from django.contrib import messages



class MessageView(View):
    def get(self, request):
        form = MessageForm()
        return render(request, 'connects_app/messages.html', {'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message.objects.create(
                fullName=data['fullName'],
                email=data['email'],
                mobile=data['mobile'],
                text=data['text'],
            )
            messages.success(request, 'اطلاعات با موفقیت ثبت شد', 'success')
            return redirect('main:index')
        else: 
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد', 'error')
            return redirect('connects:message')
        
        