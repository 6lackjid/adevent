from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.



class UserAdmin(UserAdmin):
    ordering = ('id',)
    
    list_display = ['id','email']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ()}),
        (
            ('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (('Important dates'), {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2')
            
        }),
    )
    
    
admin.site.register(User, UserAdmin)