from django.views.generic import  FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
# from credit.models import Person
from credit.forms import PersonForm
from django.shortcuts import render
import json

class PersonCreateView(FormView):
    template_name = 'credit/person_form.html'
    form_class = PersonForm
    success_url = reverse_lazy('query_person')

    def form_valid(self, form):

        result = form.send_query()
        if result['result'] != []:
            return render(self.request, 'credit/result_form.html', result )
        else:
            return render(self.request, 'credit/result_form_error.html')



