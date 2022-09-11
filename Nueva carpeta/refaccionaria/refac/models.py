from django.db import models

# Create your models here.
class Refaccion(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=True, blank=False)
    descripcion = models.CharField(max_length=100, unique=True, null=True, blank=False)
    modelo = models.CharField(max_length=100,  null=True, blank=False)
    precio = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "Refaccion"
    verbose_name_plural = "Refacciones"

def __str__(self):
    return self.nombre


class Agenda(models.Model):
    prducto = models.TextField()
    precio = models.IntegerField()
    fecha_encargo = models.DateField()
    fecha_carga = models.DateField()

class Meta:
    verbose_name = "Agenda"
    verbose_name_plural = "Agendas"

def __str__(self):
    return self.nombre


class Ticket(models.Model):
    servicio = models.TextField()
    precio = models.TextField()
    total = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField()


class Meta:
    verbose_name = "Ticket"
    verbose_name_plural = "Tickets"

def __str__(self):
    return self.nombre