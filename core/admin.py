from django.contrib import admin
from .models import Genero, Pelicula
# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion', 'año', 'genero']
    search_fields = ['nombre', 'año']
    list_filter = ['genero']


admin.site.register(Genero)
admin.site.register(Pelicula, PeliculaAdmin)