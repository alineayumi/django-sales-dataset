from django.shortcuts import render
from django.views.generic import (TemplateView, View,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
from django.urls import reverse_lazy

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
    fields = ("name", "price")
    model = models.Product
