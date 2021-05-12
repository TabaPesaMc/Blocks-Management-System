from django.shortcuts import render, redirect
from .models import Stock, StockHistory
from .forms import StockCreateform, StockSearchForm, StockUpdateForm, IssueForm, ReceiveForm, ReorderLevelForm,StockHistorySearchForm
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def home(request):
    tittle = 'welcome: This is the Home Page'
    context = {
        'tittle': tittle
    }
    # return redirect('/list_item')
    return render(request, 'home.html', context)


@login_required
def list_item(request):
    header = 'TAARIFA ZILIZO REKODIWA'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        'header': header,
        'querysett': queryset
    }
    # if request.method == 'POST':
    #     category = form['category'].value()
    #     queryset = Stock.objects.filter(  # category_icontains=form['category'].value(),
    #
    #         item_name__icontains=form['item_name'].value()
    #     )
    if request.method == 'POST':
        category = form['category'].value()
        queryset = StockHistory.objects.filter(
            item_name__icontains=form['item_name'].value()
        )

        if (category != ''):
            queryset = queryset.filter(category_id=category)


        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

    context = {
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, 'list_item.html', context)


@login_required
def add_items(request):
    header = 'Add Items'
    form = StockCreateform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added successfully')
        return redirect('/list_item')
    context = {
        'form': form,
        'header': header
    }
    return render(request, 'add_items.html', context)


def update_item(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully updated')
            return redirect('/list_item')
    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'successfully deleted')
        return redirect('/list_item')
    return render(request, 'delete_items.html')


def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    content = {
        'queryset': queryset
    }
    return render(request, 'stock_detail.html', content)


def issue_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.receive_quantity = 0
        instance.quantity -= instance.issue_quantity
        instance.issue_by = str(request.user)
        # instance.issue_by = str(request.user)
        messages.success(request, 'Issued SUCCESSFULLY. ' + str(instance.quantity) + ' ' + str(
            instance.item_name) + 's now left in store')
        instance.save()
        return redirect('/stock_detail/' + str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Issue' + str(queryset.item_name),
        'queryset': queryset,
        'form': form,
        'username': 'Issue By: ' + str(request.user),
    }
    return render(request, 'add_items.html', context)


def receive_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_quantity = 0
        instance.quantity += instance.receive_quantity
        instance.receive_by = str(request.user)
        instance.save()
        messages.success(request, 'Received SUCCESSFULLY. ' + str(instance.quantity) + ' ' + str(
            instance.item_name) + 's now in store')
        return redirect('/stock_detail/' + str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Receive' + str(queryset.item_name),
        'instance': queryset,
        'form': form,
        'username': 'Receive By: ' + str(request.user),
    }
    return render(request, 'add_items.html', context)


def reorder_level(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Reorder level form' + str(instance.item_name) + 'is updated to ' + str(
            instance.reorder_level))
        return redirect('/list_item')
    context = {
        'instance': queryset,
        'form': form,
    }
    return render(request, 'add_items.html', context)


@login_required
def list_history(request):
    header = 'LIST OF HISTORY ITEMS'
    querysett = StockHistory.objects.all()
    # queryset = Stock.objects.all()
    # form = StockSearchForm(request.POST or None)
    form = StockHistorySearchForm(request.POST or None)
    context = {
        "header": header,
        "form": form,
        "querysett": querysett,
        # "queryset":queryset
    }
    if request.method == 'POST':
        category = form['category'].value()

        querysett = StockHistory.objects.filter(
                               item_name__icontains=form['item_name'].value(),
                               last_updated__range = [
                                                      form['start_date'].value(),
                                                      form['end_date'].value()
                                                   ]
                            )

        if (category != ''):
            querysett = querysett.filter(category_id=category)

        context = {
            "form": form,
            "header": header,
            "querysett": querysett,
            # "queryset": queryset,

        }
    return render(request, "list_history.html", context)



def index(request):
    return render(request,'index.html')