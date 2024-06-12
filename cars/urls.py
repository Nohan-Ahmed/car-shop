from django.urls import path
from . import views

urlpatterns = [
    path('details/<slug:car_slug>-id?<int:pk>/', views.CarDetailsView.as_view(), name='car_details'),
]
