import uuid
import os

from django.db import models
from django.db.models import Q
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models


DEFAULT_LOCATION_POINT = Point(-104.9903, 39.7392)

from country.models import Municipality


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
            filter = Q(name__contains=_patterSearch)
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

class ManagerTouristAttraction(models.Manager):
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        typeProduct = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
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
 
class ManagerTypeService(models.Manager):
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        typeService = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
            filter = Q(filter | Q(description__contains=_patterSearch))
            typeService = self.filter(filter)
        else:
            typeService = self.all()
        
        return typeService
    
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
    
class ManagerSchedule(models.Manager):
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
    
    def existThisSchedule(self,_sTime,_eTime):
        exist = False
        count = self.filter(startTime=_sTime,endTime=_eTime).count()
        
        if count != 0:
            exist = True
        
        return exist

class ManagerInfrastructureAccess(models.Manager):
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        infrastruct = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
            infrastruct = self.filter(filter)
        else:
            infrastruct = self.all()
        
        return infrastruct
    
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
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        resourcetourists = None
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(name__contains=_patterSearch)
            filter = Q(filter | Q(description__contains=_patterSearch))
            filter = Q(filter | Q(comments__contains=_patterSearch))
            resourcetourists = self.filter(filter)
        else:
            resourcetourists = self.all()
        
        return resourcetourists
    
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

class TouristAttraction(models.Model):
    idTA = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=30,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerTouristAttraction()
    
    class Meta:
        verbose_name ='Atractivo turístico'    
        verbose_name_plural = 'Atractivos turísticos'
        ordering = ('name','description')
    
    def __str__(self):
        return f'{self.name}'
    
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

class TourismType(models.Model):
    idTT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=100,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=100,unique=True)
    
    objects = ManagerTourismType()
    
    class Meta:
        verbose_name ='Modalidad de Turismo'    
        verbose_name_plural = 'Modalidades de Turismo'
        ordering = ('name','description')
    
    def __str__(self):
        return f'{self.name}'
    
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

class TypeService(models.Model):
    idTS = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=30,default='')
    description = models.TextField("Descripción", null=False, blank=True, max_length=10000)
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerTypeService()
    class Meta:
        verbose_name = 'Tipo de servicio'
        verbose_name_plural = 'Tipos de servicios'
        ordering = ('name','description')
        
    def __str__(self):
        return f'{self.name}'
    
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
    
class Schedule(models.Model):
    idSchedule = models.UUIDField("id", primary_key= True, default=uuid.uuid4, editable = False)
    name = models.CharField(verbose_name="Nombre", max_length=50, null = False, blank=False)
    slug = models.SlugField("slug", max_length=50, null=False, blank=False, unique=True)
    startTime = models.TimeField("Hora de inicio", null = False, blank = False)
    endTime = models.TimeField("Hora de terminacion",null = False, blank = False)
    
    objects = ManagerSchedule()
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
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

class InfrastructureAccess(models.Model):
    idIA = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", null=False, blank=False,max_length=30,default='')
    slug = models.CharField("slug", null=False,max_length=30,unique=True)
    
    objects = ManagerInfrastructureAccess()
    class Meta:
        verbose_name = 'Infraestructura de acceso'
        verbose_name_plural = 'Infraestructuras de accesos'
        ordering = ('name',)
        
    def __str__(self):
        return f'{self.name}'

class ResourceTourist(models.Model):
    
     idRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     name = models.CharField("Nombre", null=False, blank=False,max_length=100,default='')
     slug = models.CharField("slug", null=False,max_length=100,unique=True)
     description = models.TextField("Descripción", null=False, blank=False, max_length=10000)
     address = models.TextField("Dirección", null=False, blank=False, max_length=10000)
     comments = models.TextField("Otros comentarios", null=False, blank=True, max_length=10000,default='')
     idMunicipality = models.ForeignKey(Municipality,related_name='resourcetourists',verbose_name="Municipio",on_delete=models.CASCADE)
     geoLocLat = models.DecimalField("Latitud",default=0.0,decimal_places=21, max_digits=25)
     geoLocLon = models.DecimalField("Longitud",default=0.0,decimal_places=21, max_digits=25)
     
     
     objects = ManagerResourceTourist()
     
     def __str__(self):
         return self.name
     
     def searchResourceTouristCloset(self):
         pass
     
     def countServices(self):
         return Service.objects.filter(idResourceTourist=self.pk).count()
     
    
     class Meta:
         verbose_name = 'Recurso turístico'
         verbose_name_plural = 'Recursos turísticos'
    
class TouristAttractionResourceTourist(models.Model):
    
    idTART = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist, verbose_name="Recurso turístico",related_name='attractions', on_delete=models.CASCADE) 
    idTouristAttraction = models.ForeignKey(TouristAttraction, verbose_name="Atractivo turístico", on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.idResourceTourist)+' ( '+str(self.idTouristAttraction)+' )'
    class Meta:
        verbose_name = 'Atractivo del recurso turístico'
        verbose_name_plural = 'Atractivos del recurso turístico'
        ordering = ('idResourceTourist','idTouristAttraction')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idTouristAttraction'], 
                name='unique_attraction',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
class TourismTypeResourceTourist(models.Model):
    
    idTTRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist, verbose_name="Recurso turístico",related_name='type_tourism', on_delete=models.CASCADE) 
    idTourismType = models.ForeignKey(TourismType, verbose_name="Tipo de turismo", on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.idResourceTourist)+' ( '+str(self.idTourismType)+' )'
    class Meta:
        verbose_name = 'Modalidad de turismo del recurso turístico'
        verbose_name_plural = 'Modalidades de turismo del recurso turístico'
        ordering = ('idResourceTourist','idTourismType')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idTourismType'], 
                name='unique_tourismtype',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
class InfrastructureAccessResourceTourist(models.Model):
    
    idIART = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist, verbose_name="Recurso turístico",related_name='infrastructure_access', on_delete=models.CASCADE) 
    idInfrastructureAccess = models.ForeignKey(InfrastructureAccess, verbose_name="Infraestructura de acceso", on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.idResourceTourist)+' ( '+str(self.idInfrastructureAccess)+' )'
    
    class Meta:
        verbose_name = 'Infraestructura de acceso del recurso turístico'
        verbose_name_plural = 'Infraestructuras de accesos del recurso turístico'
        ordering = ('idResourceTourist','idInfrastructureAccess')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idInfrastructureAccess'], 
                name='unique_infrastructure_access_tourist',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
class Service(models.Model):
    idService = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist,verbose_name="Recurso turístico",related_name='services',on_delete=models.CASCADE)
    idTypeService = models.ForeignKey(TypeService,verbose_name="Tipo de servicio",related_name='type_service',on_delete=models.CASCADE)
    idSchedule = models.ForeignKey(Schedule,verbose_name="Horario del servicio",related_name='schedule',on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.idResourceTourist)+' ( '+str(self.idTypeService)+', '+str(self.idSchedule)+' )'
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ('idResourceTourist','idTypeService','idSchedule')
        constraints = [
            models.UniqueConstraint(
                fields=['idResourceTourist', 'idTypeService','idSchedule'], 
                name='unique_service',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
        
class MediaResourceTourist(models.Model):
    idMediaRT = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idResourceTourist = models.ForeignKey(ResourceTourist,verbose_name="Recurso turístico",related_name='medias',on_delete=models.CASCADE)
    
    
    def __str__(self):
         return ' '
    class Meta:
        verbose_name = 'Media del Recurso Turístico'
        verbose_name_plural = 'Medias de los Recursos Turísticos'

class MediaImageRT(MediaResourceTourist):
    image= models.ImageField(verbose_name="Imagen del recurso",upload_to=renameFile,null=False)
    directorySave = 'images_resources'
    
    def __str__(self):
         return self.image.url
    
    class Meta:
        verbose_name = 'Imagen del Recurso Turístico'
        verbose_name_plural = 'Imágenes del Recurso Turístico'
    
class ResourceTouristCloset(models.Model):
    idResourceTouristCloset = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idRTSource=models.ForeignKey(ResourceTourist,related_name='id_rt_source', verbose_name="Recurso Turístico origen",on_delete=models.CASCADE)
    idRTTo = models.ForeignKey(ResourceTourist,related_name='id_rt_to',verbose_name="Recurso Turistico destino",on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Recurso Turístico cercano'
        verbose_name_plural = 'Recursos Turísticos cercanos'
        ordering = ('idResourceTouristCloset','idRTSource','idRTTo')
        constraints = [
            models.UniqueConstraint(
                fields=['idRTSource','idRTTo'], 
                name='unique_resource_tourist_closet',
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
    





