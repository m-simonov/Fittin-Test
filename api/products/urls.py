from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('feed/', views.FileUploadView.as_view(), name='feed')
]


