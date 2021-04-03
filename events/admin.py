from django.contrib import admin
from .models import Event,EventPhoto
# Register your models here.


@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/injectTiny.js',)

admin.site.register(EventPhoto)