from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from testapp.models import Employee

from django.urls import reverse_lazy


# Create your views here.




class ReadCompleteData(ListView):
    model=Employee

    #variable name=modelname_list===>employee_list

    #html name=(modelname_list.html)==>employee_list.html


class ReadOneData(DetailView):
    model=Employee   


    #synatx:modelname or object ->employee
    #html-file:modelname_detail.html--->employee_detail.html


class InsertData(CreateView):
    model=Employee
    fields=('name','age','salary','city')




class UpdateData(UpdateView):
    model=Employee
    fields=('name','age','salary','city')



class DeleteData(DeleteView):
    model=Employee
    success_url=reverse_lazy('hello')





















