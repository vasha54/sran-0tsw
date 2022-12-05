from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import AbstractUser, Group, UserManager
from django.core.validators import RegexValidator
from django.db.models import Q

import os
import uuid

def renameFile(instance,filename):
    ext = filename.split('.')[-1]
    filename="%s.%s" % (uuid.uuid4(),ext)
    return os.path.join(instance.directorySave,filename)

# Create your models here.
class UserDRPAManager(UserManager):
    
    def registerPersonUM(self,_person):
        if 'aunteticate' in _person.keys() and _person['aunteticate']==True:
            tusername = ''
            tfirst_name = ' '
            tlast_name = ' '
            temail = ' '
            tis_staff = 0
            tis_active = 1
            ttypeAccount =''
            tnumberPhone =''
            tnumberMobile =''
            tpassword = ''
            rol =Role.INVITED
            
            if 'username' in _person.keys():
                tusername=_person['username']
            if 'password' in _person.keys():
                tpassword=_person['password']
            if 'givenName' in _person.keys():
                tfirst_name = tfirst_name.join(_person['givenName']) 
            if 'sn' in _person.keys():
                tlast_name = tlast_name.join(_person['sn'])   
            if 'mail' in _person.keys():
                temail = temail.join(_person['mail'])
            if 'typeAccount' in _person.keys():
                ttypeAccount = _person['typeAccount']
            if 'rol' in _person.keys():
                rol = _person['rol']
                
            usser = UserDRPA(username=tusername,is_staff=tis_staff,
                             is_active=tis_active,first_name=tfirst_name,last_name=tlast_name,email=temail,
                             typeAccount=ttypeAccount,numberMobile=tnumberMobile,numberPhone=tnumberPhone)
            usser.password = make_password(tpassword)
            usser.save()
            groupUser = Role.objects.get(name=rol)
            if groupUser !=None: 
                groupUser.user_set.add(usser)
            
    def existUsserWithAccountManual(self,_user,_password):
        exist = False
        if self.existUsserWithAccount(_user,_password) == True:
            usserOBJ = self.get(username=_user)
            if usserOBJ!=None and usserOBJ.typeAccount == UserDRPA.MANUAL:
                exist = True
            
        return exist
    
    def existUsserWithAccount(self, _user, _password):
        exist = False
        try:
            matchcheck= self.get(username=_user)
            if matchcheck != None:
                exist = True
        except UserDRPA.DoesNotExist:
            exist = False
        return exist
    
    def searchPattern(self,_patterSearch=None):
        _patterSearch = str(_patterSearch).strip()
        
        usser = None 
        
        if _patterSearch != None and len(_patterSearch)!=0:
            filter = Q(username__contains=_patterSearch)
            filter = Q(filter | Q(first_name__contains=_patterSearch))
            filter = Q(filter | Q(last_name__contains=_patterSearch))
            usser = self.filter(filter).order_by('last_name','first_name')
        else:
            usser = self.all().order_by('last_name','first_name')
        
        return usser
    
    def listRolesAviablesForThisUser(self, _username):
        rolesAviables = []
        try:
            user = self.get(username=_username)
            groups = user.groups.values_list('name',flat = True)
            rolesUser = list(groups)
            
            allRoles = list(Role.objects.all().values_list('name',flat=True))
            
            for rol in allRoles:
                if rol not in rolesUser:
                    rolesAviables.append(rol)
            
        except UserDRPA.DoesNotExist:
            pass
        return rolesAviables
    
    def addRolesThisUser(self,_roles,_username):
        try:
            user = self.get(username=_username)
            for rol in _roles:
                groupUser = Role.objects.get(name=rol)
                if groupUser !=None:
                    groupUser.user_set.add(user)
        except UserDRPA.DoesNotExist:
            pass
        

class UserDRPA(AbstractUser):
    MANUAL = 'manual'
    LDAP = 'ldap'
    TYPE_ACCOUNT_CHOICES = [
        (MANUAL,'Cuenta manual'),
        (LDAP,'Cuenta ldap')
    ]
    
    numberPhoneValidator = RegexValidator(r"^\d+$", 'Los campos de números de teléfono y móvil admite solamente dígitos')
   
    numberPhone = models.CharField('Número de teléfono',max_length=11,validators=[numberPhoneValidator],blank=True,default='')
    numberMobile = models.CharField('Número del móvil',max_length=11,validators=[numberPhoneValidator],blank=True,default='')
    typeAccount = models.CharField('Tipo de cuenta',max_length=6,choices=TYPE_ACCOUNT_CHOICES,default=MANUAL)
    logo= models.ImageField("Logotipo",upload_to=renameFile,null=False, default="avatar/photo-profile-default.png")
    directorySave = 'avatar'
    
    objects = UserDRPAManager()
    
    def nameCompleted(self):
        return self.first_name+" "+self.last_name
    
    def getRoles(self):
        groups = self.groups.values_list('name',flat = True) # QuerySet Object
        roles = list(groups)
        return roles
    
    def getRol(self):
        rol = self.groups.order_by().values_list('name',flat = True)[0]
        return rol
    
    class Meta:
        verbose_name ='Usuario'
        verbose_name_plural = 'Usuarios'
    
class Role(Group):
    ADMIN       = 'admin'
    MANAGER_CONTENT = 'gestorContenido'
    INVITED     = 'invitado'
    WORKER_UM   = 'trabajadorUM'
    WORKER_DRPA = 'trabajadorDRPA'
    STUDENT_UM  = 'estudianteUM'
    
    ROLES_SYSTEM = [ADMIN,MANAGER_CONTENT,WORKER_DRPA,WORKER_UM,STUDENT_UM,INVITED]
    class Meta:
        verbose_name ='Rol'
        verbose_name_plural = 'Roles'
    