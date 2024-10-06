from django.db import models

# Create your models here.

class Message(models.Model):
    fullName = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, verbose_name='شماره موبایل')
    text = models.TextField(verbose_name='متن پیام')
    
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
        db_table = 't_message'
    
