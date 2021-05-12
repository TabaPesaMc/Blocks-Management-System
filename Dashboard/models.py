from django.db import models
from Sales.models import Invoice
from STOCK_MANAGEMENT_APP.models import Stock


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='theas')
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE,related_name='thebs')
    # product_category = models.CharField(max_length=20)
    # payment_method = models.CharField(max_length=50)
    # shipping_cost = models.CharField(max_length=50)
    # unit_price = models.DecimalField(max_digits=5, decimal_places=2)