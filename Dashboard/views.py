from django.http import JsonResponse
from django.shortcuts import render
from Dashboard.models import Order
from STOCK_MANAGEMENT_APP.models import Stock
from django.core import serializers
# from .form import OrderForm


def dashboard_with_pivot(request):
    header = 'LIST OF SALES ITEMS'
    # form = OrderForm(request.POST or None)
    # queryset = Stock.objects.select_related()
    queryset = Order.objects.select_related()
    # queryset = Order.objects.select_related().filter(foreign_record__foreign_attribute__gt=foo)
    # context = {
    #     "title": "New Invoice",
    #     'header': header,
    #     "queryset": queryset,
    # }
    # return render(request, 'dashboard_with_pivott.html', context)
    return render(request, 'new_one.html',{'queryset':queryset})



def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)