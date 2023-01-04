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
    
class ManagerValueTouristic(models.Manager):
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        valueTouristic = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(value__contains=_patterSearch)
            filter = Q(filter | Q(description__contains=_patterSearch))
            valueTouristic = self.filter(filter)
        else:
            valueTouristic = self.all()
        
        return valueTouristic
    
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

class ManagerScheduleService(models.Manager):
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        scheduleClass = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
            scheduleClass = self.filter(filter)
        else:
            scheduleClass = self.all()
        
        return scheduleClass
    
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

class ManagerResourceTourist(models.Manager):
    pass

class ManagerTouristResourceImage(models.Manager):
    pass

class ManagerTouristResourceVideo(models.Manager):
    pass

class ManagerTypeService(models.Manager):
    pass

class ManagerService(models.Manager):
    pass

class TourismType(models.Model):
    idTT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField("Tipo de turismo", null=False, blank=False,max_length=30,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerTourismType()
    
    class Meta:
        verbose_name ='Tipo de turismo'    
        verbose_name_plural = 'Tipos de turismo'
        ordering = ('type','description')
    
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

class ValueTouristic(models.Model):
    
    idVT = models.UUIDField("ID",primary_key=True, default=uuid.uuid4, editable=False)
    value = models.CharField("Valor", null=False, blank=False,max_length=40,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.SlugField("slug", null=False,max_length=40)
    
    objects = ManagerValueTouristic()
    
    class Meta:
        verbose_name = 'Valor turístico'
        verbose_name_plural = 'Valores turísticos'
        ordering = ('value','description')
        
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
    
    def __str__(self):
        return f'{self.value}'

class ScheduleService(models.Model):
    idScheduleClass = models.UUIDField("id", primary_key= True, default=uuid.uuid4, editable = False)
    name = models.CharField(verbose_name="Nombre", max_length=50, null = False, blank=False)
    slug = models.SlugField("slug", max_length=50, null=False, blank=False, unique=True)
    startTime = models.TimeField("Hora de inicio", null = False, blank = False)
    endTime = models.TimeField("Hora de terminacion",null = False, blank = False)
    
    objects = ManagerScheduleService()
    class Meta:
        verbose_name = 'Horario de servicio'
        verbose_name_plural = 'Horarios de servicio'
        ordering = ('startTime','endTime','name')
        constraints = [
            models.UniqueConstraint(
                fields=['startTime', 'endTime'], 
                name='unique_range_time',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
    def __str__(self):
        return f'{self.name} ({self.startTime}-{self.endTime})'

class TypeService(models.Model):
    idTS = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField("Tipo de servicio", null=False, blank=False,max_length=30,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerTypeService()
    class Meta:
        verbose_name = 'Tipo de servicio'
        verbose_name_plural = 'Tipos de servicios'
        ordering = ('type','description')
        
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
  
class ResourceTourist(models.Model):
    idRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=100)
    description = models.TextField("Descripción", null=False, blank=False, max_length=100000)
    history = models.TextField("Historia", null=False, blank=False, max_length=100000)
    siteWeb =  models.URLField("Sitio Web",max_length=50, null = True, blank=True)
    slug = models.CharField("slug", null=False,max_length=100,unique=True)
    
    objects = ManagerResourceTourist()
    
    class Meta:
        verbose_name = 'Recurso turístico'
        verbose_name_plural = 'Recursos turísticos'

class TouristResourceImage(models.Model):
    idTRI = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idTouristResource=models.ForeignKey(ResourceTourist,related_name='images',verbose_name="Recurso Turísticos",on_delete=models.CASCADE)
    name = models.CharField("Nombre", null=True, blank=True, max_length=100)
    description = models.TextField("Descripción", null=True, blank=True, max_length=255)
    image= models.ImageField(verbose_name="Imagen del recurso",upload_to=renameFile,null=False)
    slug = models.CharField("slug", null=False,max_length=100,unique=True)
    directorySave = 'images_resources'
    
    objects = ManagerTouristResourceImage()
    class Meta:
        verbose_name = 'Imagen del recurso turístico'
        verbose_name_plural = 'Imágenes del recurso turístico'

class TouristResourceVideo(models.Model):
    idTRV = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    objects = ManagerTouristResourceVideo()
    class Meta:
        verbose_name = 'Video del recurso turístico'
        verbose_name_plural = 'Videos del recurso turístico'

class Service(models.Model):
    idService = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist,verbose_name="Recurso turístico",on_delete=models.CASCADE)
    idTypeService = models.ForeignKey(TypeService,verbose_name="Tipo de servicio",on_delete=models.CASCADE)
    idScheduleService = models.ForeignKey(ScheduleService,verbose_name="Horario del servicio",on_delete=models.CASCADE)
    
    objects = ManagerService()
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ('idResourceTourist','idTypeService','idScheduleService')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idTypeService','idScheduleService'], 
                name='unique_service',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
class ValueResourceTourist(models.Model):
    idVRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist, verbose_name="Recurso turístico", on_delete=models.CASCADE) 
    idValueTouristic = models.ForeignKey(ValueTouristic, verbose_name="Valor turístico del recurso", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Valor del recurso turístico'
        verbose_name_plural = 'Valores del recurso turístico'
        ordering = ('idResourceTourist','idValueTouristic')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idValueTouristic'], 
                name='unique_value_tourist',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]

class TourismTypeResourceTourist(models.Model):
    
    idTTRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist, verbose_name="Recurso turístico", on_delete=models.CASCADE) 
    idTourismType = models.ForeignKey(TourismType, verbose_name="Tipo de turismo", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Tipo de turismo del recurso turístico'
        verbose_name_plural = 'Tipos de turismo del recurso turístico'
        ordering = ('idResourceTourist','idTourismType')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idTourismType'], 
                name='unique_type_tourist',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]