from django.db import models

# Create your models here.

STATUS_CHOICES =(
    ('Unpaid','Unpaid'),
    ('Paid','Paid'),
    ('Cancelled','Cancelled')
)

class customer(models.Model):
    name = models.CharField(max_length= 50,blank=False,null= False)
    phone = models.CharField(max_length= 12)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class invoice(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length= 50,choices=STATUS_CHOICES)


    def __str__(self):
        return self.customer.name
