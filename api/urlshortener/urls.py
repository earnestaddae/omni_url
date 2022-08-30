"""URL mapping for URLShortner"""

from django.urls import path 
from urlshortener import views

app_name = 'urlshortener'

urlpatterns = [
    path('create/', views.CreateShortURLView.as_view(), name='create'),
    path('<str:url_key>/', views.RedirectShortURLView.as_view(), name='redirect'),
]