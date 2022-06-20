from django.contrib import admin
from . models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('CustomerName' ,'IsProjectStarted', 'EmailId', 'MobileNumber', "Description" , 'Status','CreatedOn', 'UpdatedOn')
    list_filter = ('CreatedOn',)

    
admin.site.site_header = "tickIGS"    
admin.site.register(Customer, CustomerAdmin )
admin.site.register(Technology)
