from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm
from .models import Invoice
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv


# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "Sales/home.html", context)


def add_sales(request):
    header = 'Add Items'
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added successfully')
        return redirect("/sales/list_sales")
    context = {
        "form": form,
        "title": "New Invoice",
    }
    return render(request, "Sales/Add_Sales.html", context)


@login_required
def list_sales(request):
    form = InvoiceSearchForm(request.POST or None)
    header = 'LIST OF SALES ITEMS'
    queryset = Invoice.objects.all()
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "title": "New Invoice",
        'header': header,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Invoice.objects.filter(name__icontains=form['name'].value(),
                                          line_one__icontains=form['line_one'].value())

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CUSTOMER NAME','ITEM NAME', 'QUANTITY','PRICE','TOTAL','PAID','DATE'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.name, stock.line_one,
                                 stock.line_one_quantity,stock.line_one_unit_price,
                                 stock.line_one_total_price,stock.paid,stock.timestamp])
            return response

        context = {
            'form': form,
            'header': header,
            'queryset': queryset,
        }

    return render(request, "Sales/list_sales.html", context)


@login_required
def delete_sales_item(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'successfully deleted')
        return redirect('/sales/list_sales')
    return render(request, 'sales/delete_sales_item.html')
