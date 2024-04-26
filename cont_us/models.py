from django.db import models
from hrasc.utils import unique_slug_generator
from django.db.models.signals import pre_save

from django.conf import settings
from django.core.mail import send_mail
# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=999)
    email = models.EmailField()
    phone = models.CharField(max_length=999)
    msG = models.TextField(max_length=9999, verbose_name='message')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


def ContactUssignal(sender, instance, *args, **kwargs):
    subject = 'ENQUIRE FROM WEBSITE'
    message = f'''
                Name : {instance.name}
                Email : {instance.email}
                Phone : {instance.phone}
                Message :
                {instance.msG}.
        '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saadchaudhary646@gmail.com','khalid@hr-asc.in ','Recruithr@hr-asc.in','Admin@hr-asc.in']
    send_mail(subject, message, email_from, recipient_list)


pre_save.connect(ContactUssignal, sender=ContactUs)


class Service(models.Model):
    title = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="Service")
    thumbnail_white = models.ImageField(upload_to="Service/white")

    background = models.ImageField(upload_to="Service/bg")
    about = models.TextField(max_length=9999)
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

def Service_SLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(Service_SLUG, sender=Service)






class Gallary(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="Gallary")
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Gallary'
        verbose_name_plural = 'Gallarys'


class licenses(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="licenses")
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'license'
        verbose_name_plural = 'licenses'


class team(models.Model):
    name = models.CharField(max_length=999)
    designation = models.CharField(max_length=999)
    phone = models.CharField(max_length=999, blank=True, null=True)
    Email = models.CharField(max_length=999, blank=True, null=True)

    thumbnail = models.ImageField(upload_to="licenses")
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team member'


class Client(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="Gallary")
    index = models.BooleanField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class catagory(models.Model):
    image =models.ImageField()
    title  =models.CharField(max_length=100)
    slug  =models.SlugField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.title)

def catagorySLUG(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =unique_slug_generator(instance)


pre_save.connect(catagorySLUG,sender=catagory)



class Sector(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="Sector")
    index = models.BooleanField()
    # catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'


class process_info(models.Model):
    title = models.CharField(max_length=999)
    about = models.TextField(max_length=9999)
    Enable = models.BooleanField(default=True)
    position = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)

    img = models.ImageField(upload_to='svg_images/')

    def save(self, *args, **kwargs):
        # Perform any additional processing if needed
        super().save(*args, **kwargs)



    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'process_info'
        verbose_name_plural = 'Process'

def process_info_SLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(process_info_SLUG, sender=process_info)




class side_bar(models.Model):
    thumbnail = models.ImageField(upload_to="side_bar")
    name = models.CharField(max_length=999)
    url = models.CharField(max_length=999)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'side_bar'
        verbose_name_plural = 'side_bar'






