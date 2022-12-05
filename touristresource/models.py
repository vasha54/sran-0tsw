import uuid
import os

from django.db import models
from django.db.models import Q

# Create your models here.

def renameFile(instance,filename):
    ext = filename.split('.')[-1]
    filename="%s.%s" % (uuid.uuid4(),ext)
    return os.path.join(instance.directorySave,filename)

class TouristResourceManager (models.Manager):
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        
        touristResource = None 
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
            filter = Q(filter | Q(description__contains=_patterSearch))
            
            touristResource = self.filter(filter).order_by('last_name')
        else:
            touristResource = self.all().order_by('name')
        
        return touristResource
    
    
    
    

class TouristResource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=100)
    description = models.TextField("Descripción", null=False, blank=False, max_length=10000)
    
    objects = TouristResourceManager()
    class Meta:
        verbose_name = 'Recurso Turístico'
        verbose_name_plural = 'Recursos Turísticos'
        
    def descriptionShort(self):
        descriShort = ""
        words = self.description.split()
        countChars =0
        index =0
        while index < len(words) and countChars + len(words[index]) < 146:
            if index !=0 :
                descriShort = descriShort+ " "
            descriShort = descriShort + words[index]
            countChars = len(descriShort)
            index = index +1
        if index < len(words):
            descriShort = descriShort +" ..."
        return descriShort
    
class TouristResourceImage(models.Model):
    idTouristResource=models.ForeignKey(TouristResource,related_name='images',verbose_name="Recurso Turísticos",on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=True, blank=True, max_length=100)
    description = models.TextField("Descripción", null=True, blank=True, max_length=255)
    image= models.ImageField(verbose_name="Imagen del recurso",upload_to=renameFile,null=False)
    directorySave = 'images_resources'
    
    class Meta:
        verbose_name = 'Imagen del Recurso Turístico'
        verbose_name_plural = 'Imagenes del Recursos Turísticos'
    
