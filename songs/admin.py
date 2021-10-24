from django.contrib import admin

# Register your models here.
from .models import Song, Performer

admin.site.register(Song)
admin.site.register(Performer)
