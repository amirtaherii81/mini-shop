from django.shortcuts import render
from apps.products.models import Product
from django.views import View
from django.db.models import Q
# Create your views here.

class SearchResultView(View):
    def get(self, request, *args, **kwargs):    
        query = self.request.GET.get("q")
        print(query)
        product = Product.objects.filter(
            Q(title__icontains=query)|
            Q(discription__icontains=query)
            )
        
        context = {
            'products': product,
            }
        return render(request, 'search_app/search_result.html', context)

            
