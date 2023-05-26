from django.db import models
from django.db.models import Q

import uuid
import os
# Create your models here.

class ManagerProvince(models.Manager):
    
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

class ManagerMunicipality(models.Manager):
    
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


class Province (models.Model):
    idProvince = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=50,default='')
    slug = models.CharField("slug", null=False,max_length=50,unique=True)
    
    objects = ManagerProvince()
    
    class Meta:
        verbose_name ='Provincia'    
        verbose_name_plural = 'Provincias'
        
    def __str__(self):
        return f'{self.name}'
        
    def countMunicipality(self):
        return Municipality.objects.filter(idProvince=self).count()
        
class Municipality(models.Model):
    idMunicipality = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=50,default='')
    slug = models.CharField("slug", null=False,max_length=50,unique=True)
    idProvince=models.ForeignKey(Province,related_name='municipalitys',verbose_name="Provincia",on_delete=models.CASCADE)
    
    objects = ManagerMunicipality()
    
    class Meta:
        verbose_name ='Municipio'    
        verbose_name_plural = 'Municipios'
        
    def __str__(self):
        return f'{self.name}'