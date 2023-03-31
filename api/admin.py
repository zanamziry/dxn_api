from django.contrib import admin

from api.models import Agent,Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AgentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
# Register your models here.
admin.site.register(Agent, AgentAdmin)
admin.site.register(Product, ProductAdmin)