from django.db import models
from django.db.models.signals import pre_save


from hrasc.utils import unique_slug_generator

from django.conf import settings
from django.core.mail import send_mail

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=999)
    heading2 = models.CharField(max_length=999)
    enable = models.BooleanField(default=False)
    position = models.IntegerField(blank=True, null=True, unique=True)
    text = models.TextField(max_length=9999, null=True, blank=True)
    IMG = models.ImageField(upload_to='carousel/img1', null=True, blank=True)
    link_lable1 = models.CharField(max_length=9999, null=True, blank=True)
    link1 = models.CharField(max_length=9999, null=True, blank=True)
    link_lable2 = models.CharField(max_length=9999, null=True, blank=True)
    link2 = models.CharField(max_length=9999, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)

    def __str__(self):
        return str(self.title)


def RandSLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(RandSLUG, sender=Carousel)


class Client_review(models.Model):
    title = models.CharField(max_length=999)
    enable = models.BooleanField(default=True)
    text = models.TextField(max_length=9999)
    name = models.CharField(max_length=9999)
    designation = models.CharField(max_length=9999)
    position = models.IntegerField(blank=True, null=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)

    def __str__(self):
        return str(self.title)


def Client_reviewSLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(Client_reviewSLUG, sender=Client_review)



class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.company_name + " - " + self.full_name


def Employer_signal(sender, instance, *args, **kwargs):
    subject = 'ENQUIRE FROM WEBSITE Employer'
    message = f'''
                Name         : {instance.first_name}
                Email        : {instance.email_address}
                Phone        : {instance.phone_number}
                company_name : {instance.company_name}
                occupation   : {instance.occupation}
                Message      : {instance.message}.
        '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saadchaudhary646@gmail.com', 'khalid@hr-asc.in ','Recruithr@hr-asc.in', 'Admin@hr-asc.in']
    send_mail(subject, message, email_from, recipient_list)


pre_save.connect(Employer_signal, sender=Employer)






class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name



def Employee_signal(sender, instance, *args, **kwargs):
    subject = 'ENQUIRE FROM WEBSITE Employee'
    message = f'''
                Name : {instance.first_name}
                Email : {instance.email}
                Phone : {instance.phone_number}
                Message :
                {instance.message}.
        '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saadchaudhary646@gmail.com', 'khalid@hr-asc.in ',
                      'Recruithr@hr-asc.in', 'Admin@hr-asc.in']
    send_mail(subject, message, email_from, recipient_list)


pre_save.connect(Employee_signal, sender=Employee)



























