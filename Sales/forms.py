from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'paid'
                  ]
        widgets = {
            'line_one_quantity': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'tb1', 'name': 'tb1', 'onkeyup': 'calc(this)'}),
            'line_one_unit_price': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'tb2', 'name': 'tb2', 'onkeyup': 'calc(this)'}),
            'line_one_total_price': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': True, 'value': '0', 'id': 'total', 'name': 'total'}),
            'total': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': True, 'value': '0'}),

        }


class InvoiceSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Invoice
        fields = ['name', 'line_one']
