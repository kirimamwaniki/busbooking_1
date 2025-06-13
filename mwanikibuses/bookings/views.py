from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# testing function
def testing(request):
    cust = customer.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'cust' : cust,
    }

    return HttpResponse(template.render(context, request))
    # on testing it will be redirected to this url to display a list


# main.html view
def main(request):

    #getting fields from the form from main.html with method post
    if request.method == 'POST':
        customer_obj = customer(
            ticketno = request.POST['seat_no'] + request.POST['id_no'],
            Customer_name = request.POST['name'],
            destination = request.POST['Destination'],
            seatno = request.POST['seat_no'],
            Id_number = request.POST['id_no']
        )

        # saving the customer details to the customer model
        customer_obj.save()

        #redirecting to payment.html url
        return redirect('pay', id=customer_obj.Id_number)
    
    return render(request, 'main.html')

def success(request):
    #fetching success.html template
    return render(request, 'success.html')

def payment(request, id):
    #getting customer details from the main.html
    x = customer.objects.get(Id_number=id)

    # initiating a payment
    if x.status == "not paid":
        if request.method == "POST":
            x.status = "paid"
            x.save()

            #redirecting to success page
            return redirect('success') 

    return render(request, 'payment.html')

# Create your views here.
            