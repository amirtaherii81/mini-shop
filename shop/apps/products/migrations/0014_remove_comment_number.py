# Generated by Django 4.2.13 on 2024-07-22 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_comment_name_comment_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='number',
        ),
    ]
