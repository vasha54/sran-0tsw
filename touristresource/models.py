import uuid
import os

from django.db import models
from django.db.models import Q

# Create your models here.

def renameFile(instance,filename):
    ext = filename.split('.')[-1]
    filename="%s.%s" % (uuid.uuid4(),ext)
    return os.path.join(instance.directorySave,filename)


class ManagerTourismType(models.Manager):
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        typeProduct = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(type__contains=_patterSearch)
            filter = Q(filter | Q(description__contains=_patterSearch))
            typeProduct = self.filter(filter)
        else:
            typeProduct = self.all()
        
        return typeProduct
    
    def existThisSLUG(self, _slug,_pk=None):
        exist = False
        count = 0
        
        if _pk == None:
            count = self.filter(slug = _slug).count()
        else:
            count = self.exclude(pk=_pk).filter(slug = _slug).count()    
        
        if count != 0:
            exist = True
        return exist

class TourismType(models.Model):
    idTT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField("Tipo de turismo", null=False, blank=False,max_length=30,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerTourismType()
    
    class Meta:
        verbose_name ='Tipo de Turismo'    
        verbose_name_plural = 'Tipos de Turismo'
        ordering = ('type',)
    
    def __str__(self):
        return f'{self.type}'
    
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
