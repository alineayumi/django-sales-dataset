from django.urls import path
from sales_app import views

app_name = 'sales_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('sales/', views.SalesListView.as_view(), name='sales'),
    path('sales/<int:pk>/', views.SalesDetailView.as_view(), name='sale_detail'),
    path('sales/create/', views.SalesCreateView.as_view(), name='sale_create'),
    path('sales/<int:pk>/publish/', views.sale_publish, name='sale_publish'),
]
