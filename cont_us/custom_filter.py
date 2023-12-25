# cont_us/templatetags/custom_filters.py
from django import template
from cont_us.models import Service

register = template.Library()

@register.filter
def services_list(value):
    services = Service.objects.filter(enable=1).order_by('position').all()
    return services
