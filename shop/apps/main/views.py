from django.shortcuts import render
from django.conf import settings
from django.views.generic.list import ListView
# from django.views import View
from apps.products.models import Product, Brand

# Create your views here.
def media_admin(request):
    return {'media_url': settings.MEDIA_URL}

def category_admin(request):
    brand = Brand.objects.all()
    return {'category': brand}


# def index(request):
#     products = Product.objects.all()
#     return render(request, 'main_app/index.html', {'products': products})

       
class IndexView(ListView):
    model = Product
    template_name = 'main_app/index.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
