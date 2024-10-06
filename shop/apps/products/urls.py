from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('<str:item>', ProductsFilterView.as_view(), name='product_filter'),
    path('product/<int:pk>', ProductDetialView.as_view(), name='product_detail'),
    path('comment/<int:pk>', CommentView.as_view(), name='comment'),
]
