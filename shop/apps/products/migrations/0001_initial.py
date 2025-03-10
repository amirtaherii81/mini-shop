# Generated by Django 4.2.13 on 2024-05-26 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(choices=[('Lenovo', 'Lenovo'), ('Dell', 'Dell'), ('HP', 'HP')], max_length=100, verbose_name='نام برند')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discription', models.TextField(verbose_name='توضیحات محصول')),
                ('image_product', models.ImageField(upload_to='', verbose_name='عکس محصول')),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'db_table': 't_product',
            },
        ),
        migrations.CreateModel(
            name='FeatureProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_size', models.CharField(max_length=100, verbose_name='سایز صفحه نمایش')),
                ('color', models.CharField(max_length=100, verbose_name='رنگ')),
                ('cpu', models.CharField(max_length=100, verbose_name='سری پردازنده')),
                ('ram', models.CharField(max_length=100, verbose_name='مشخصات رم')),
                ('graphics', models.CharField(max_length=100, verbose_name='مشخصات گرافیت')),
                ('grade', models.CharField(max_length=100, verbose_name='طبقه بندی')),
                ('processor_model', models.CharField(max_length=100, verbose_name='مدل پردازنده')),
                ('processor_manufacturer', models.CharField(max_length=100, verbose_name='سازنده پردازنده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'ویژگی محصول',
                'verbose_name_plural': 'ویژگی محصولات',
                'db_table': 't_feature_product',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='نظر')),
                ('is_active', models.BooleanField(default=False, verbose_name='تایید شده/تایید نشده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'db_table': 't_comment',
            },
        ),
    ]
