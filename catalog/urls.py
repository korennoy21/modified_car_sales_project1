
from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/new/', CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/edit/', CarUpdateView.as_view(), name='car_edit'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]
