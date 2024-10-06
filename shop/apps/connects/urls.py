from django.urls import path
from .views import MessageView

app_name = 'connects'
urlpatterns = [
    path('', MessageView.as_view(), name='message'),
]

