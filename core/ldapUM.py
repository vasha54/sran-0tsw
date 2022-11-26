
#Consulta para saber si existe un usuario en ldap  de la universidad usando directorio unico
#http://directoriounico.umcc.cu/api/getData.php?&f=json&t=DirectorioActivo&opt=count&c=usuario&w= usuario = 'luis.valido'

import ldap3
from ldap3.core.exceptions import LDAPException,LDAPBindError,LDAPSocketOpenError
from accescontrol.models import Role, UserDRPA
class LDAPUM:
    
    WORKER = Role.WORKER_UM
    STUDENT = Role.STUDENT_UM
    DOMAIN_EMAIL_STUDENT = '@est.umcc.cu'
    DOMAIN_EMAIL_WORKER = '@umcc.cu'
    
    def __init__(self):
        self.person={}
        self.IP_SERVER_LDAP='10.34.8.5'
        self.LIST_FIELDS_LDAP = ['mail', 'sn', 'givenName','displayName','description','Mobile','telephoneNumber']        
        self.ORGANIZATIONAL_UNITS_UM = 'OU=Usuarios,DC=umcc,DC=cu'
    
    def autenticateStudent(self,_username, _password):
        server = ldap3.Server('ldap://' + self.IP_SERVER_LDAP, get_info=ldap3.ALL)
        self.person = None
        try:
            conn = ldap3.Connection(server, user=_username+LDAPUM.DOMAIN_EMAIL_WORKER, password=_password, auto_bind=True)
            results = conn.search(self.ORGANIZATIONAL_UNITS_UM,
                                  "(&(objectClass=*)(sAMAccountName=" + _username + "))",
                                  ldap3.SUBTREE,
                                  attributes=self.LIST_FIELDS_LDAP)
            if results == True:
                entrie = conn.entries[0]
                self.person ={'rol':LDAPUM.STUDENT,
                              'aunteticate':True}
                for k,v in entrie.entry_attributes_as_dict.items():
                    self.person[k]=v
                if 'mail' in self.person.keys(): 
                    mails = self.person['mail']
                    for mail in mails:
                        print(mail)
                        if mail.endswith(LDAPUM.DOMAIN_EMAIL_STUDENT) == True:
                            return True
                return False
            else:
                return False
        except LDAPBindError as e:
            self.person ={'aunteticate':False}
            self.person['errorMessage']=str(e)
            return False 
        except LDAPSocketOpenError as f:
            self.person ={'aunteticate':False}
            self.person['errorMessage']=str(f)
            return False
        
           
    def autenticateWorker(self,_username, _password):
        server = ldap3.Server('ldap://' + self.IP_SERVER_LDAP, get_info=ldap3.ALL)
        self.person = None
        try:
            conn = ldap3.Connection(server, user=_username+LDAPUM.DOMAIN_EMAIL_WORKER, password=_password, auto_bind=True)
            results = conn.search(self.ORGANIZATIONAL_UNITS_UM,
                                  "(&(objectClass=*)(sAMAccountName=" + _username + "))",
                                  ldap3.SUBTREE,
                                  attributes=self.LIST_FIELDS_LDAP)
            if results == True:
                entrie = conn.entries[0]
                self.person ={'rol':LDAPUM.WORKER,
                              'aunteticate':True}
                for k,v in entrie.entry_attributes_as_dict.items():
                    self.person[k]=v
                
                if 'mail' in self.person.keys(): 
                    mails = self.person['mail']
                    for mail in mails:
                        if mail.endswith(LDAPUM.DOMAIN_EMAIL_WORKER) == True:
                            return True
                return False
            else:
                return False
        except LDAPBindError as e:
            self.person ={'aunteticate':False}
            self.person['errorMessage']=str(e)
            return False 
        except LDAPSocketOpenError as f:
            self.person ={'aunteticate':False}
            self.person['errorMessage']=str(f)
            return False
    
    def autenticatePersonUM(self,_username, _password):
        if self.autenticateWorker(_username,_password) == True:
            return True
        elif self.autenticateStudent(_username,_password) == True:
            return True
        elif UserDRPA.objects.existUsserWithAccountManual(_username,_password) == True:
            return True
        else:
            #TODO Si necesita que trabajar con el LDPA el retorno de abajo debe ser False en caso no quiera 
            # trabajar con el LDAP retorne True
            return False
    
    def getPerson(self):
        return self.person