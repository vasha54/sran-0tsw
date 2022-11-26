from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from accescontrol.models import UserDRPA,Role
# Register your models here.

class UserDRPAAdmin(UserAdmin):
    list_display  = ('username','first_name','last_name','email','is_active','typeAccount','numberPhone','numberMobile')
    search_fields = ('username','first_name','last_name','email','is_active','typeAccount','numberPhone','numberMobile')
    search_fields = ('text', )
    list_filter = ('typeAccount','is_active')

admin.site.register(UserDRPA,UserDRPAAdmin)
admin.site.register(Role,GroupAdmin)
