from django.urls import path
from . import views

urlpatterns = [
    path('travel-plan/', views.travel_plan, name='travel_plan'),
]