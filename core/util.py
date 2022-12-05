from django.forms import BaseFormSet
import qrcode

def limitPagesShow(_min,_current,_max):
    limits=[]
    if _current - 2 >=_min:
        limits.append(_current - 2)
    else:
        limits.append(_min)
    
    limits.append(min(limits[0]+4,_max))
    
    if(limits[1]-limits[0]<4):
        i=limits[1]
        while limits[1]-limits[0]<4 and i <= _max:
            limits[1]=i
            i=i+1
            
        i=limits[0]
        while limits[1]-limits[0]<4 and i >= _min:
            limits[0]=i
            i=i-1
            
    return limits

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def canRemoveUserDRPA(_user):
    canRemove = True
    #TODO Falta definir bajo que criterios vamos a eliminar los usuarios
    return canRemove

def generateQRTouristResource(_request,_resource):
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4)
    domainWeb = _request.META['HTTP_HOST']
    protocol = 'http://'
    suffix ='/api/v1/touristresource/post/'
    strUIID = str(_resource.id)
    url = protocol+domainWeb+suffix+strUIID
    info = url
    print(url)
    # Agregamos la informacion
    qr.add_data(info)
    qr.make(fit=True)
    # Creamos una imagen para el objeto código QR
    imagen = qr.make_image()
    #Guardemos la imagen con la extension que queramos
    
    imagen.save('medias/qr_resources/'+strUIID+'.svg')
    

class RequeridFormSet(BaseFormSet):
    def __init__(self,*args,**kwargs):
        super(RequeridFormSet,self).__init__(*args,**kwargs)
        for form in self.forms:
            form.empty_permitted = False


