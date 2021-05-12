from django.db import models
from STOCK_MANAGEMENT_APP.models import Stock

# Create your models here.

class Invoice(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField('Namba ya Malipo', blank=False, null=False, auto_created=True)
    invoice_date = models.DateField('Taree ya Malipo', auto_now_add=False, auto_now=False, blank=True, null=True)
    name = models.CharField('Jina la mteja', max_length=120, default='', blank=False, null=False)

    line_one = models.CharField('Aina ya Bidhaa', max_length=120, default='', blank=False, null=False)
    line_one_quantity = models.IntegerField('Kiasi/Idadi', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Bei', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Jumla', default=0, blank=True, null=True)

    line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    line_three = models.CharField('Line 3', max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    line_four = models.CharField('Line 4', max_length=120, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    line_five = models.CharField('Line 5', max_length=120, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    phone_number = models.CharField('Namba ya Simu', max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField('Imelipwa', default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Proforma Invoice', 'Proforma Invoice'),
        ('Invoice', 'Invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __unicode__(self):
        return self.invoice_number

