from django.urls import path, include
from lookup.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
]
