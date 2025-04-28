from django.urls import path
from .views import predict_crop, home, about, contact

urlpatterns = [
    # path('', predict_crop, name='predict_crop'),
    path('', home, name='home'),
    path('predict/', predict_crop, name='predict'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
]
