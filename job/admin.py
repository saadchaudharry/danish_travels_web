from django.contrib import admin
from .models import Carousel,Client_review

# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('title',"heading2",'text' )
    list_filter = ('enable', )
    list_display = ('title','position', )


admin.site.register(Carousel,CarouselAdmin)

# client
class Client_reviewAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('enable', )
    list_display = ('title','position', )

admin.site.register(Client_review,Client_reviewAdmin)