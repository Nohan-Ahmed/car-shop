from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:pk>', views.order_view, name='order'),
    # path('order/<int:pk>', views.OrderCreateView.as_view(), name='order'),
]
