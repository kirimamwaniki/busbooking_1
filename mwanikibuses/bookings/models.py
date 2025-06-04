from django.db import models

class bus(models.Model):
    busno = models.IntegerField(default=0, primary_key=True)
    busname = models.CharField(max_length=255)
    seats_available = models.IntegerField(default=30)
    Drivername = models.CharField(max_length=255)


class customer(models.Model):
    ticketno = models.IntegerField(primary_key=True)
    Customer_name = models.CharField(max_length=255)
    seatno = models.IntegerField(default=0)
    busno = models.IntegerField(default=0)
    destination = models.CharField(max_length=255, null=True)
    Id_number = models.IntegerField(max_length=8, null=True )


class tester(models.Model):
    name = models.CharField(max_length = 255)
    integer = models.IntegerField(primary_key=True)

# Create your models here.
