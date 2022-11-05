from django.contrib import admin
from .models import *
# Register your models here.


class AdminSample(admin.ModelAdmin):
    list_display = ['username', 'email']#list_display should contain the exact attributes of the model


admin.site.register(Te1, AdminSample)
admin.site.register(Te2, AdminSample)
admin.site.register(Te3, AdminSample)

admin.site.register(Nte1, AdminSample)
admin.site.register(Nte2, AdminSample)
admin.site.register(Nte3, AdminSample)


