from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Laptop
from django.forms.widgets import SelectDateWidget
from django.forms.widgets import NumberInput

from django import forms
# Create your views here.

class AddLaptopView(CreateView):
           model=Laptop
           fields='__all__'


           def get_form(self):
                form = super(AddLaptopView, self).get_form()
                form.fields['Purchasedate'].widget = NumberInput(attrs={'type': 'date'})
                return form

           def post(self, request):
                form = super(AddLaptopView, self).get_form()
                form.save()
                return redirect('display')



class DisplayLaptopView(ListView):
    model=Laptop



class UpdateLaptopView(UpdateView):
    model=Laptop
    fields='__all__'

    def get_form(self):
        form = super(UpdateLaptopView, self).get_form()
        form.fields['Purchasedate'].widget = NumberInput(attrs={'type': 'date'})
        return form

    success_url = "/home/display"

class DeleteLaptopView(DeleteView):
    model=Laptop
    fields = '__all__'

    success_url = "/home/display"

