from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='House-home'),
    path('about/', views.about, name='House-about'),
    path('houses/', views.house_view, name='House-houses'),
    path('houses/search', views.search_houses, name='search_houses' ),
]
