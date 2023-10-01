from django.db import models
from django.db.models.signals import pre_save


from hrasc.utils import unique_slug_generator

# Create your models here.



class Carousel(models.Model):
    title=models.CharField(max_length=999)
    heading2=models.CharField(max_length=999)
    enable  = models.BooleanField(default=False)
    position  =models.IntegerField(blank=True, null=True,unique=True)

    text  =models.TextField(max_length=9999)
    IMG     = models.ImageField(upload_to='carousel/img1',null=True,blank=True)
    link_lable1 = models.CharField(max_length=9999,null=True,blank=True)
    link1 = models.CharField(max_length=9999,null=True,blank=True)
    link_lable2 = models.CharField(max_length=9999,null=True,blank=True)
    link2 = models.CharField(max_length=9999,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    slug  =models.SlugField(max_length=999,blank=True,null=True)

    def __str__(self):
        return str(self.title)

def RandSLUG(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =unique_slug_generator(instance)


pre_save.connect(RandSLUG,sender=Carousel)




class Client_review(models.Model):
    title=models.CharField(max_length=999)
    enable  = models.BooleanField(default=True)
    text  =models.TextField(max_length=9999)
    position  =models.IntegerField(blank=True, null=True,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    slug  =models.SlugField(max_length=999,blank=True,null=True)

    def __str__(self):
        return str(self.title)

def Client_reviewSLUG(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =unique_slug_generator(instance)


pre_save.connect(Client_reviewSLUG,sender=Client_review)