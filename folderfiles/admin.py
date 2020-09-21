from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from .models import File


# Register your models here.
admin.site.register(File, DraggableMPTTAdmin)