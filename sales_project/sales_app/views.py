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
