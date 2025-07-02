from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import base64


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

def payment(request, id):
    #getting customer details from the main.html
    x = customer.objects.get(Id_number=id)

    # initiating a payment
    if x.status == "not paid":
        if request.method == "POST":
            x.status = "paid"
            x.save()

            #redirecting to success page
            return redirect('details', id=x.Id_number) 

    return render(request, 'payment.html')

def details(request, id):
    #getting customer number
    data = customer.objects.get(Id_number=id)
    qr_data = f"Ticket: {data.ticketno}, Name: {data.Customer_name}, ID: {data.Id_number}, seatno: {data.seatno}, busno: {data.busno}"

    #generating qrcode
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'details.html', {'qr_code': img_str})

# Create your views here.
            