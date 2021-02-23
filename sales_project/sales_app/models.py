from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=32)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sales_app:product_detail", kwargs={'pk':self.pk})

class Sale(models.Model):
    product_name = models.ForeignKey(Product, related_name='sales', on_delete=models.PROTECT)
    client_name = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=32, blank=True, null=True)

    def save_amount(self):
        self.amount = self.product_name.price * self.quantity
        self.save()

    def get_absolute_url(self):
        return reverse("sales_app:sale_publish",kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.pk)
