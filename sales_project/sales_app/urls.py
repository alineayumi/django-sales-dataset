from django.urls import path
from sales_app import views

app_name = 'sales_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='products')
]
