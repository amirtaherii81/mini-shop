from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام برند')
    
    def __str__(self):
        return self.name if self.name else ''
    
        
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'
        db_table = 't_brand'
        
        
                
def upload_product_image(instance, filename):
    return f'images/{instance.brand_name}/{filename}'


class Product(models.Model):
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='نام برند', related_name='brand_name')
    title = models.CharField(max_length=100, verbose_name='عنوان') 
    price = models.IntegerField(verbose_name='قیمت')
    discription = models.TextField(verbose_name='توضیحات محصول')
    image_product = models.ImageField(upload_to=upload_product_image ,verbose_name='عکس محصول')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    def __str__(self):
        return f"{self.title}\t{self.brand_name}"
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        db_table = 't_product'



class FeatureProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE ,verbose_name='محصول', related_name='product_feature')
    page_size = models.CharField(max_length=100, verbose_name='سایز صفحه نمایش')
    color = models.CharField(max_length=100, verbose_name='رنگ')
    cpu = models.CharField(max_length=100,verbose_name='سری پردازنده')
    ram = models.CharField(max_length=100, verbose_name='مشخصات رم')
    graphics = models.CharField(max_length=100, verbose_name='مشخصات گرافیت')
    grade = models.CharField(max_length=100, verbose_name='طبقه بندی')
    processor_model = models.CharField(max_length=100, verbose_name='مدل پردازنده')
    processor_manufacturer = models.CharField(max_length=100, verbose_name='سازنده پردازنده')
    
    def __str__(self):
        return self.page_size
    
    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی محصولات'
        db_table = 't_feature_product'
        
        
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE,verbose_name='محصول مورد نقد و بررسی')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر نقد کننده')
    name = models.CharField(default='کاربر' ,max_length=100, verbose_name='نام', blank=True, null=True)
    text = models.TextField(verbose_name='متن نقد و بررسی')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_active=models.BooleanField(default=False,verbose_name="وضعیت")

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        db_table = 't_comment'

class Status(models.Model):
    status = models.CharField(max_length=100, verbose_name='وضعیت سفارش')
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'وضعیت سفارش'
        verbose_name_plural = 'وضعیت سفارشات'
        db_table = 't_status'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order')
    number = models.IntegerField(verbose_name='تعداد محصول')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name= 'وضعیت محصول')
    
    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
        db_table = 't_order'

    

