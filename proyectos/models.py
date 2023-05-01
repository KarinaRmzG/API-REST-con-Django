from django.db import models

# Create your models here.

'''
    models.CharField()      ->  Es un campo de modelo en Django que se utiliza para representar una cadena 
                                de texto de longitud limitada en una base de datos.
    models.TexField()       ->  Es un campo de modelo en Django que se utiliza para representar texto sin 
                                límite de longitud en una base de datos. A diferencia de models.CharField, 
                                models.TextField no tiene una longitud máxima predeterminada, lo que significa 
                                que puede almacenar grandes cantidades de texto.  
    models.DateTimeField()  ->  Es un campo de modelo en Django que se utiliza para representar una fecha y 
                                hora en una base de datos. Este campo se utiliza comúnmente para almacenar 
                                información temporal como la fecha y hora en que se creó o actualizó un 
                                objeto en la base de datos.
                                El formato de fecha y hora que se utiliza por defecto es el formato ISO 8601, 
                                pero se puede especificar un formato personalizado si se desea.               
'''
class Proyecto(models.Model):
    #nombreColumna = Tipo de dato que guardará
    titulo = models.CharField(max_length=200)
    description = models.TextField()
    tecnologia = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
