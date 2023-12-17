from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .form import ContactUS_form
from .models import Service, team, Client, ContactUs, Sector, licenses

from job.models import Carousel, Client_review

# Create your views here.


def index(request):
    Carousels = Carousel.objects.filter(enable=1).all().order_by('position')
    Services = Service.objects.filter(index=1).all()

    context = {'Services': Services, "Carousel": Carousels}
    return render(request, 'index.html', context)


def AllService(request):
    Services = Service.objects.all()
    Sectors = Sector.objects.all()

    context = {'Services': Services, 'Sector': Sectors}
    return render(request, 'services.html', context)


def Clients(request):
    Clients = Client.objects.all()
    context = {'Clients': Clients}
    return render(request, 'clients.html', context)


def license_s(request):
    license_ = licenses.objects.all()
    context = {'licenses': license_}
    return render(request, 'licenses.html', context)


def about(request):
    teams = team.objects.all().order_by('position')
    Client_reviews = Client_review.objects.filter(
        enable=1).all().order_by('position')

    context = {"teams": teams, 'Client_review': Client_reviews}
    return render(request, 'about.html', context)


class cont(CreateView):
    model = ContactUs
    form_class = ContactUS_form
    template_name = 'contact.html'
    success_url = reverse_lazy('cont')

    def get_context_data(self, *args, **kwargs):
        context = super(cont, self).get_context_data(*args, **kwargs)
        return context
