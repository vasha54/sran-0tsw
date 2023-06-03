from django.forms import BaseFormSet
from urllib.parse import urlparse
from django.conf import settings as djangosettings
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.http import HttpResponseRedirect, HttpResponse
from core import settings
from PIL import Image, ImageDraw, ImageFont #Save and display the image


from unidecode import unidecode
import qrcode
import re


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

def generateQRTouristResource(_request,_resource,_web=True):
    fontFile = 'static/fonts/HelveticaBold.ttf'
    fontName = 'HelveticaBold.ttf'
    imageExt = '.png'
    
    captionText = 'From '
    
    if _web==True:
        captionText += 'Web'
    else:
        captionText += 'App'
    
    
    # Create qr code instance
    qr = qrcode.QRCode()
    
    domainWeb = _request.META['HTTP_HOST']
    protocol = 'http://'
    data=protocol+domainWeb
    strUIID = str(_resource.pk)
    if _web == False:
        data=data+'/api/v1'
    data=data+'/resource_tourist/'+strUIID
    
    print(data)
    
    # Add data
    qr.box_size = int(64)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    imgQR = qr.make_image()
    
    draw = ImageDraw.Draw(imgQR)
    QRwidth, QRheight = imgQR.size
    fontSize = 1 #starting font size
    img_fraction = 0.90 # portion of image width you want text width to be, I've had good luck with .90
    fontHeightMax = qr.border * qr.box_size - 10
    captionX = 0
    captionY = 0
    print('Font height max is set to: ' + str(fontHeightMax))
    font = ImageFont.truetype(fontFile, fontSize)
    while font.getsize(captionText)[0] < img_fraction*QRwidth and font.getsize(captionText)[1] < fontHeightMax:
        fontSize += 1
        font = ImageFont.truetype(fontFile, fontSize)
    captionX = int(QRwidth - font.getsize(captionText)[0]) / 2 #Center the label
    print('Offset: ' + str(captionX))
    draw.text((captionX, captionY), captionText, font=font)
    
    if _web==True:
        imgQR.save('medias/qr_resources/'+'web_'+strUIID+imageExt)
    else:
        imgQR.save('medias/qr_resources/'+'app_'+strUIID+imageExt)


    

def generateSLUG(_name):
    slug = str(_name)
    slug = unidecode(slug) #Convertir texto Unicode en ASCII para quitar tildes y eñes
    slug = re.sub(r'[^\w\s]', '', slug) #Elimino todos los caracteres no alfanumericos
    slug = slug.lower() #Convetir a minusculas  
    slug = re.sub(r"\s+", '-',slug) #Sustituir un espacio o una secuencias de espacio por un guion
    return  slug

class RequeridFormSet(BaseFormSet):
    def __init__(self,*args,**kwargs):
        super(RequeridFormSet,self).__init__(*args,**kwargs)
        for form in self.forms:
            form.empty_permitted = False
            



def set_language(request,idiom,*args,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    language = idiom
    
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get('HTTP_REFERER')).path)
        except Resolver404:
            view = None
        
        if view:
            break
        
    if view:
        translation.activate(language)
        next_url= reverse(view.url_name,args=view.args,kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(djangosettings.LANGUAGE_COOKIE_NAME,language)
        return response
    return HttpResponseRedirect(url)
    
    # if request.method == 'POST':
    #     language = 'es'
    #     next_url = '/admin/'
    #     if 'language' in request.POST.keys():
    #         language = request.POST['language']
        
    #     if 'next' in request.POST.keys():
    #         next_url = request.POST['next'] 
        
        
    #     for lang, _ in settings.LANGUAGES:
    #         translation.activate(lang)
    #         try:
    #             view = resolve(urlparse(request.META.get('HTTP_REFERER')).path)
    #         except Resolver404:
    #             view = None
                
    #         if view:
    #             break
        
    #     if view:
    #         translation.activate(language)
    #         next_url= reverse(view.url_name,args=view.args,kwargs=view.kwargs)
    #         response = HttpResponseRedirect(next_url)
    #         response.set_cookie(djangosettings.LANGUAGE_COOKIE_NAME,language)
    #     else:
    #         response = HttpResponseRedirect(next_url)
    #     return response
    # else:
    #     return HttpResponseRedirect(url)
           


