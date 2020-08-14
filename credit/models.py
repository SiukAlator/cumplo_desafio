from django import forms

class Person(forms.Form):
    amount = forms.CharField(label='Monto (UF)',max_length=130)
    timer = forms.CharField(label='Plazo (días)',max_length=130)
    tmc_date = forms.CharField(label='Fecha TMC (dd-mm-yyyy)',max_length=130)
