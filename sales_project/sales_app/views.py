from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, View,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
from django.urls import reverse_lazy
from .forms import SaleForm, ProductForm
from django.db.models import Sum

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'sales_app/home.html'

class ProductListView(ListView):
    # setting the product_list to the name products to improve readability with frentend
    context_object_name = 'products'
    model = models.Product

class ProductDetailView(DetailView):
    context_object_name = 'product_detail'
    model = models.Product
    template_name = 'sales_app/product_detail.html'

class ProductCreateView(CreateView):
    form_class = ProductForm
    model = models.Product
    success_url = reverse_lazy("sales_app:products")

class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = models.Product
    success_url = reverse_lazy("sales_app:products")

class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy("sales_app:products")

class SalesListView(ListView):
    context_object_name = 'sales'
    model = models.Sale

class SalesDetailView(DetailView):
    context_object_name = 'sale_detail'
    model = models.Sale
    template_name = 'sales_app/sale_detail.html'

class SalesCreateView(CreateView):
    redirect_field_name = 'sales_app:sale_publish'
    form_class = SaleForm
    model = models.Sale

class SalesUpdateView(UpdateView):
    redirect_field_name = 'sales_app:sale_publish'
    form_class = SaleForm
    model = models.Sale

class SalesDeleteView(DeleteView):
    model = models.Sale
    success_url = reverse_lazy("sales_app:sales")

class DashboardView(TemplateView):
    template_name = 'sales_app/dashboard.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        products_list = models.Product.objects.all()
        context['products'] = products_list
        return context

def sale_publish(request, pk):
    sale = get_object_or_404(models.Sale, pk=pk)
    sale.save_amount()
    return redirect('sales_app:sales')
