# cont_us/templatetags/custom_filters.py
from django import template
from cont_us.models import Service,side_bar

register = template.Library()

@register.filter(name='services_list')
def services_list(value):
    services = Service.objects.filter(Enable=1).order_by('position')
    return services


@register.filter(name='side_bar_list')
def side_bar_list():
    side = side_bar.objects.all()
    return side
