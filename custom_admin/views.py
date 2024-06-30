from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

from .views import *
from .forms import *

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.user.is_authenticated:
        print("User is already authenticated")
        redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return render(request,'login.html',{'error':'invalid username or password'})

    return render(request,'login.html')

def custom_logout(request):
    
    logout(request)
    request.session.flush()
    return redirect('login-view')


# class CustomerInvoiceListView(generics.ListAPIView):
    
#     queryset = customer.objects.all()
#     serializer_class = CustomerSerializer

#     def list(self,request,*args,**kwargs):
#         customers = self.get_queryset()
#         invoices = invoice.objects.all()

#         return render(request,'customer_invoice.html',{'customers':customers , 'invoices':invoices}) 
    
def customer_create(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm()
    return render(request,'customer_create.html',{'form':form})

def invoice_create(request):

    if request.method == 'POST':
        form = InvoiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('invoice-list')
    else:
        form = InvoiceForm()
    return render(request,'invoice_create.html',{'form':form})

@api_view(['GET'])
def customer_invoice_list(request):
    customers = customer.objects.all()
    invoices = invoice.objects.all()
    print(customers)
    customer_serializer = CustomerSerializer(customers, many=True)
    print(customer_serializer)
    invoice_serializer = InvoiceSerializer(invoices, many=True)
    return Response({
        'customers': customer_serializer.data,
        'invoices': invoice_serializer.data
    })

def customer_list_view(request):
    response = requests.get(f'{settings.API_URL}/api/customer-invoice/')
    data = response.json()
    return render(request, 'customer_list.html', {'customers': data['customers']})

def invoice_list_view(request):
    response = requests.get(f'{settings.API_URL}/api/customer-invoice/')
    data = response.json()
    return render(request, 'invoice_list.html', {'invoices': data['invoices']})

def update_customer(request,pk):
    customers = get_object_or_404(customer,pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST,instance= customers )
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm(instance = customers)

    return render(request,'update_customer.html',{'form':form})

def update_invoice(request,pk):
    invoices = get_object_or_404(invoice,pk=pk)

    if request.method == 'POST':
        form = InvoiceForm(request.POST,instance=invoices)
        if form.is_valid():
            form.save()
            return redirect('invoice-list')
    else:
        form = InvoiceForm(instance=invoices)

        return render(request,'update_invoice.html',{'form':form})
