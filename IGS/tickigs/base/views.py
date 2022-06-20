import mailbox
from re import template
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import Customer, Technology
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os

#Email Confirmation part
def send_email(request):
    
    template = render_to_string('base/email_template.html', {'name': request.data['CustomerName'] , "email": request.data['EmailId']})
    # temp = strip_tags(template)
    

    email = EmailMultiAlternatives(
        'Thanks',
        template,
        settings.EMAIL_HOST_USER,
        [request.data["EmailId"]],
    )
    email.mixed_subtype = 'related'
    
    
    email.content_subtype = 'html'
    email.fail_silently =False
    email.send()
    print('email sent ')



# Create your views here.
@api_view(['GET'])
def ShowAll(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def Tech(request):
    Tech  = Technology.objects.only('TechnologyName')
    serializer = TechnologySerializer(Tech, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowOne(request, pk):
    customer1= Customer.objects.get(CustomerId = pk)
    serializer = CustomerSerializer(customer1, many =False)
    return Response(serializer.data)

@api_view(['POST'])
def Createcustomer(request):
    mail = request.data["EmailId"]
    name = request.data["CustomerName"]
    
    send_email(request)

    serializer = CustomerSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def Update(request, pk):
    customer = customer.objects.get(customerId = pk)
    serializer = CustomerSerializer(instance=customer,  data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def Delete(request, pk):
    customer = customer.objects.get(customerId = pk)
    customer.delete()
    serializer = CustomerSerializer(customer, many =False)
    return Response("Item Deleted Successfully")