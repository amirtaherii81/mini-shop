from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import Product, Brand, FeatureProduct, Comment, Status, Order
from django.http import HttpResponse
from .forms import CommentForm
from django.contrib import messages
# Create your views here.


class ProductsFilterView(View):
    def get(self, request, item):
        try:
            brand = Brand.objects.get(name=item)
            products = Product.objects.filter(brand_name=brand, is_active=True)
            return render(request, 'products_app/products_filter.html', {'products': products})
        except Brand.DoesNotExist:
            return HttpResponse("Brand not found")
#----------------------------------------------------------------

class ProductDetialView(View):
    def get(self, request, pk):
        # form = CommentForm
        try:
            product = Product.objects.get(id=pk)
            return render(request, 'products_app/product_detail.html', {'product': product})
        except Product.DoesNotExist:
            return HttpResponse("Product not found")

#----------------------------------------------------------------  
class CommentView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        form = CommentForm()
        return render(request, 'products_app/comment.html', {'product':product ,'form':form})
    
    def post(self, request, pk):
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            product = Product.objects.get(id=pk)
            if form.is_valid():
                data = form.cleaned_data
                comment = Comment()
                comment.product = product
                comment.user = request.user
                comment.text = data['text']
                comment.name = data['name']
                comment.save()
                # next_url = request.GET.get('next')
                messages.success(request, 'نظر شما با موقعیت ارسال شد پس از بررسی ثبت میشود', 'success')
                return redirect('main:index')
            else:
                message.error(request, 'اطلاعات نامعتبر می باشد', 'error')
                return render(request, 'products_app/comment.html', {'product':product ,'form':form})
        else:
            messages.info(request, 'کاربر گرامی ابتدا باید در سایت ثبت نام کنید', 'info')
            return redirect('accounts:register')

            


