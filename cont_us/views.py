from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .form import ContactUS_form
from .models import Service,team,Client,ContactUs

from job.models import Carousel,Client_review

# Create your views here.

def index(request):
    Carousels      =   Carousel.objects.filter(enable=1).all().order_by('position')
    Client_reviews =   Client_review.objects.filter(enable=1).all().order_by('position')
    Services       =   Service.objects.filter(index=1).all()
    teams          =   team.objects.filter(index=1).order_by('position')
    Clients        =   Client.objects.filter(index=1).all()
    context ={'Services':Services,"teams":teams,"Carousel":Carousels,"Client":Clients,'Client_review':Client_reviews}
    return render(request,'index.html',context)

def AllService(request):
    Services = Service.objects.all()
    context={'Services':Services}
    return render(request,'service.html',context)


def Clients(request):
    Clients = Client.objects.all()
    context={'Clients':Clients}
    return render(request,'Clients.html',context)



def about(request):
    teams =   team.objects.all().order_by('position')

    context= {"teams":teams}
    return render(request,'about_us.html',context)



class cont(CreateView):
    model = ContactUs
    form_class = ContactUS_form
    template_name = 'contact.html'
    success_url = reverse_lazy('cont')

    def get_context_data(self, *args,**kwargs):
        context = super(cont,self).get_context_data(*args, **kwargs)
        return context
