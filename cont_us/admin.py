from django.contrib import admin
from .models import ContactUs,Service,Gallary,licenses,Client,team,Sector,process_info,catagory,side_bar

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Service)
admin.site.register(Gallary)
admin.site.register(licenses)
admin.site.register(Sector)
admin.site.register(Client)
admin.site.register(team)
admin.site.register(process_info)
admin.site.register(catagory)
admin.site.register(side_bar)

