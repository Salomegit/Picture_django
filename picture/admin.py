from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Movie,MovieAdmin)