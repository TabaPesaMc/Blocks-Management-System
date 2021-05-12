from django import forms
from .models import Stock, StockHistory,profile
from django.db.models.functions import TruncDate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StockCreateform(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'price']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')

        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name


class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=True)
    end_date = forms.DateTimeField(required=True)

    class Meta:
        model = StockHistory
        fields = ['category', 'item_name', 'start_date', 'end_date']

        # widgets = {'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
        #            'end_date': forms.DateInput(attrs={'class': 'datepicker'})
        #            }


class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'price']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to', 'price']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity', 'price']


class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']


