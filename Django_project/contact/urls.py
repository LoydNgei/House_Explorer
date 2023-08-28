# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact_agent/<int:house_id>/', views.contact_agent, name='contact_agent'),
    # path('house_details/<int:house_id>/', views.house_details, name='house_details'),
]
