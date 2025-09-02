from django.db import models
from django.contrib.auth.models import User


class Comite(models.Model):
    descripcion_comite = models.CharField(max_length=100)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "comite"

        
        
        
class Tareas(models.Model):
    estado = models.IntegerField(default=0)
    comite = models.ForeignKey(Comite, on_delete=models.CASCADE)
    descripcion_tarea = models.CharField(max_length=200)
    responsable = models.CharField(max_length=100)
    correo_responsable = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField(null=True, blank=True)
        
    class Meta:
        db_table = "tarea"
        
        
        
        
        
class Subtareas(models.Model):
    estado = models.IntegerField(default=0)
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    descripcion_subtarea = models.CharField(max_length=200)
    responsable = models.CharField(max_length=100)
    correo_responsable = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField(null=True, blank=True)
        
    class Meta:
        db_table = "sub_tarea"
        
        
        
        
class SubtareasAdicionales(models.Model):
    estado = models.IntegerField(default=0)
    subtarea = models.ForeignKey(Subtareas, on_delete=models.CASCADE)
    descripcion_subtarea_adicional = models.CharField(max_length=200)
    responsable = models.CharField(max_length=100)
    correo_responsable = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField(null=True, blank=True)
        
    class Meta:
        db_table = "subtarea_adicional"