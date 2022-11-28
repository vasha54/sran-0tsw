import uuid
import os

from django.db import models

# Create your models here.

def renameFile(instance,filename):
    ext = filename.split('.')[-1]
    filename="%s.%s" % (uuid.uuid4(),ext)
    return os.path.join(instance.directorySave,filename)

class TouristResource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", blank=True, max_length=100)
    description = models.TextField("Descripción", null=False, blank=False, max_length=255)
    
    class Meta:
        verbose_name = 'Recurso Turístico'
        verbose_name_plural = 'Recursos Turísticos'
    
class TouristResourceImage(models.Model):
    idTouristResource=models.ForeignKey(TouristResource,verbose_name="Recurso Turísticos",on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", blank=True, max_length=100)
    description = models.TextField("Descripción", null=False, blank=False, max_length=255)
    image= models.ImageField("Logotipo",upload_to=renameFile,null=False, blank=False)
    directorySave = 'images_resources'
    
    class Meta:
        verbose_name = 'Imagen del Recurso Turístico'
        verbose_name_plural = 'Imagenes del Recursos Turísticos'
    
