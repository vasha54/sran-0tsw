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