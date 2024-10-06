from django.urls import path
import apps.main.views as views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
