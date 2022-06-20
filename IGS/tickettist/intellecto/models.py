from django.db import models

# Create your models here.


class User(models.Model):
    UserId = models.BigAutoField(primary_key =True)
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=15)
    IsProjectStarted = models.BooleanField()
    Description = models.TextField()
    Status = models.CharField(max_length=100)
    CreatedOn = models.DateField(auto_now=False, auto_now_add=False)
    UpdatedOn = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.UserName