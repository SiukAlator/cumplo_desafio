from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from credit.services import get_TMC
from credit.models import Person

class PersonForm(forms.Form):

    amount = forms.DecimalField(label='Monto (UF)',max_digits=25, decimal_places=20)
    timer = forms.IntegerField(label='Plazo (días)')
    tmc_date = forms.DateField(label='Fecha TMC', widget=forms.DateInput(attrs={'type': 'date'}))
    # name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)

    def send_query(self):
        
        # --- Tiempos ---- #
        #Menos de 90 días
        codes_90days_inf = [ '10', '11', '25', '26']
        #Más de 90 días
        codes_90days_sup = [ '4', '5', '6', '7', '8', '9', '27', '28', '29', '30', '31', '32', '33', '34', '35', '44', '45']
        #Más de un año
        codes_365days_sup = ['13', '14', '22', '24']

        # --- UF ----#
        #Entre 50UF y 200UF
        code_50uf_200uf_entre = ['44']
        #Menos 50UF
        code_50uf_inf = ['45']
        #Menos de 100UF
        code_100uf_inf = ['4', '28']
        #Entre 100UF y 200UF
        code_100uf_200uf_entre = ['5', '31']
        #Mas de 200UF
        code_200uf_sup = ['6', '32']
        #Menos de 200UF
        code_200uf_inf = ['7', '30', '33']
        #Entre 200UF y 5000UF
        code_200uf_5000uf_entre = ['8', '27', '35']
        #Mas de 5000UF
        code_5000uf_sup = ['9', '11', '25', '29', '34']
        #Menos de 5000UF
        code_5000uf_inf = ['10']
        #Menos de 2000UF
        code_2000uf_inf = ['13'] 
        #Mas de 2000UF
        code_2000uf_sup = ['14, 24'] 

        amount = self.cleaned_data['amount']
        timer = self.cleaned_data['timer']
        tmc_date = self.cleaned_data['tmc_date']

        # Se analiza el tiempo
        codes_timer = []
        if timer <= 90:
            codes_timer = codes_90days_inf
        elif timer >= 90:
            codes_timer = codes_90days_sup

        if timer >= 365:
            codes_timer +=  codes_365days_sup
        
        # Se analiza las UF
        codes_UF = []
        if amount <= 50:
            codes_UF = code_50uf_inf
        if 50 <= amount <= 200:
            codes_UF += code_50uf_200uf_entre
        if amount <= 100:
            codes_UF += code_100uf_inf
        if 100 <= amount <= 200:
            codes_UF += code_100uf_200uf_entre
        if amount >= 200:
            codes_UF += code_200uf_sup
        if amount <= 200:
            codes_UF += code_200uf_inf
        if 200 <= amount <= 5000:
            codes_UF += code_200uf_5000uf_entre
        if amount >= 5000:
            codes_UF += code_5000uf_sup
        if amount <= 5000:
            codes_UF += code_5000uf_inf
        if amount >= 2000:
            codes_UF += code_2000uf_sup
        if amount <= 2000:
            codes_UF += code_2000uf_inf

        #Se realiza la consulta con la fecha ingresada
        params = { 'date': tmc_date }
        data_tmc = get_TMC(params)
        result = []
        for itm in data_tmc:
            try:
                codes_timer.index(itm['Tipo'])
                codes_UF.index(itm['Tipo'])
                result.append(itm)
            except:
                pass

            
        response = { 'result': result}
        return response


   