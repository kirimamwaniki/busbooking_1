from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def testing(request):
    cust = customer.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'customer' : cust,
    }

    return HttpResponse(template.render(context, request))
    # on testing it will be redirected to this url to display a list


def main(request):
    cust = customer.objects.all().values()
    if request.method == 'POST':
        customer_obj = customer(
            Customer_name = request.POST['name'],
            destination = request.POST['Destination'],
            seatno = request.POST['seat_no'],
            Id_number = request.POST['id_no']
        )
        customer_obj.save()
        return redirect('success.html')
    # saving the values entered by the customer
    context = {
        'customer': cust
    }
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))

def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render(request))
# Create your views here.
            