# cont_us/templatetags/custom_filters.py
from django import template
from cont_us.models import Service

register = template.Library()

@register.filter(name='services_list')
def services_list(value):
    services = Service.objects.filter(Enable=1).order_by('position')
    return services
