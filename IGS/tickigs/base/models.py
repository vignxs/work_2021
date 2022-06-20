import email
from django.db import models




class Technology(models.Model):
    TechnologyId = models.IntegerField(primary_key=True)
    TechnologyName = models.CharField(max_length=100)

    def __str__(self):
        return self.TechnologyName


# Create your models here.
class Customer(models.Model):
    CustomerId = models.BigAutoField(primary_key =True)
    CustomerName = models.CharField(max_length=100)
    EmailId = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=15)
    IsProjectStarted = models.BooleanField(default=False)
    Description = models.TextField()
    Status = models.CharField(max_length=100, default="Open")
    Technologies =models.ManyToManyField(Technology)
    CreatedOn = models.DateField(auto_now_add=True)
    UpdatedOn = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.CustomerName
    # class Meta:
    #     db_table = 'Customer'
    #     # Add verbose name
    #     verbose_name = 'Customer List'





# class CustomerTechnology(models.Model):
#     CustomerName  = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     TechnologyId = models.ForeignKey(Technology,related_name='Technology_Id', db_column= 'Technology_Id', on_delete=models.CASCADE)
#     TechnologyName = models.ForeignKey(Technology,related_name='Technology_Name',db_column= 'Technology_Name', on_delete=models.CASCADE)

    