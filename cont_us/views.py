from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .form import ContactUS_form
from .models import Service, team, Client, ContactUs, Sector, licenses ,process_info

from job.models import Carousel, Client_review,Employer,Employee
from job.form import Employer_form,Employee_form

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


def service_details(request,slug):
    obj = Service.objects.get(slug=slug)

    context={"object":obj}
    return render(request,'services_details.html',context)

def Clients(request):
    Clients = Client.objects.all()
    context = {'Clients': Clients}
    return render(request, 'clients.html', context)

def process_info_view(request):
    process_ss= process_info.objects.filter(Enable=1).all().order_by('position')
    context = {'object':process_ss }
    return render(request, 'process.html', context)



def license_s(request):
    license_ = licenses.objects.all()

    context = {'licenses': license_}
    return render(request, 'licenses.html', context)


def about(request):
    teams = team.objects.all().order_by('position')
    Client_reviews = Client_review.objects.filter(enable=1).all().order_by('position')

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


class Emp(CreateView):
    model = Employer
    form_class = Employer_form
    template_name = 'Employer.html'
    success_url = reverse_lazy('Emp')

    def get_context_data(self, *args, **kwargs):
        context = super(Emp, self).get_context_data(*args, **kwargs)
        return context



class Empy(CreateView):
    model = Employee
    form_class = Employee_form
    template_name = 'Employee.html'
    success_url = reverse_lazy('Empy')

    def get_context_data(self, *args, **kwargs):
        context = super(Empy, self).get_context_data(*args, **kwargs)
        return context







