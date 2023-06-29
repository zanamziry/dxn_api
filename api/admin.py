from django.contrib import admin

from api.models import ServiceCenter,Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ServiceCenterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
# Register your models here.
admin.site.register(ServiceCenter, ServiceCenterAdmin)
admin.site.register(Product, ProductAdmin)