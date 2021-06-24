from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


# python manage.py makemigrations <------ lee  el archivo modelo  y crea  un archivo  migracion
# python manage.py migrate <----- tomar las migraciones y volcarlas en la bbdd
# python manafe.py createsuperuser

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField()
    año = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre