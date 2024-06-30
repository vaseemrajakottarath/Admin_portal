
from django.urls import path
from .views import *

urlpatterns = [
    
    path('home',home,name='home'),
    path('admin2/',login_view, name='login-view'),
    path('logout',custom_logout,name ='custom-logout'),

    # path('customer-invoice/', CustomerInvoiceListView.as_view(), name='customer-invoice-list'),
    
    path('api/customer-invoice/', customer_invoice_list, name='customer-invoice-list-api'),

    path('customers/', customer_list_view, name='customer-list'),
    path('invoices/', invoice_list_view, name='invoice-list'),

    path('customer-create',customer_create,name='customer-create'),
    path('invoice-create',invoice_create,name='invoice-create'),

    path('customer-update/<int:pk>/',update_customer,name ='customer-update'),
    path('invoice-update/<int:pk>/',update_invoice,name ='invoice-update'),

]
