# Generated by Django 4.2.13 on 2024-07-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_comment_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='کاربر', max_length=100, verbose_name='نام'),
        ),
    ]
