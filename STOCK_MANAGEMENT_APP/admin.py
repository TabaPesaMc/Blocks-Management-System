from django.contrib import admin
from .models import Stock,category
from .forms import StockCreateform


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category','issue_by','item_name', 'quantity']
    form = StockCreateform
    list_filter = ['category']
    search_fields = ['category', 'item_name']


# Register your models here.
admin.site.register(Stock,StockCreateAdmin)
admin.site.register(category)
