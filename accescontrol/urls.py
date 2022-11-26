from django.contrib import admin
from django.urls import path, include

from accescontrol.views import ListViewAccesControl, AddUsserAccesControl, UpdateUsserAccesControl, DetailsUsserAccesControl, removeRolUsserAccesControl,changeStatusUsserAccesControl, removeUsserAccesControl, getRolesAviableThisUsserAccesControl, addRolesThisUsserAccesControl

app_name = 'accescontrol'

urlpatterns = [
    path('',ListViewAccesControl.as_view(), name='listAccesControl'),
    path('add',AddUsserAccesControl.as_view(), name='addUsserAccesControl'),
    path('update/<usuario_id>',UpdateUsserAccesControl.as_view(),name='updateUser'),
    path('detail/<usuario_id>',DetailsUsserAccesControl.as_view(),name='detailUser'),
    path('removerol/<rol>/<usuario_id>',removeRolUsserAccesControl,name='removeRol'),
    path('changestatus/<usuario_id>',changeStatusUsserAccesControl,name='changeStatus'),
    path('remove/<usuario_id>',removeUsserAccesControl,name='removeUser'),
    path('rolesaviables/<usuario_id>',getRolesAviableThisUsserAccesControl,name='rolesaviableUsser'),
    path('addrolesthisuser/<list_roles>/<usuario_id>',addRolesThisUsserAccesControl,name='addRolUser')
]