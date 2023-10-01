from django.contrib import admin
from .models import ContactUs,Service,Gallary,licenses,Client,team

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Service)
admin.site.register(Gallary)
admin.site.register(licenses)
# admin.site.register(client_category)
admin.site.register(Client)
admin.site.register(team)