# Generated by Django 4.2.13 on 2024-05-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_name_brand_brand_brand_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AlterModelTable(
            name='brand',
            table='t_brand',
        ),
    ]
