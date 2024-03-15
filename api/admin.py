from django.contrib import admin

from api.models import ServiceCenter,Product, SiteSetting
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.action(description="Mark as Available")
def mark_available(modeladmin, request, queryset):
    queryset.update(available=True)

@admin.action(description="Mark as Unavailable")
def mark_unavailable(modeladmin, request, queryset):
    queryset.update(available=False)

@admin.action(description="Hide Selected Products")
def hide_product(modeladmin, request, queryset):
        queryset.update(hide=True)

@admin.action(description="Show Selected Products")
def show_product(modeladmin, request, queryset):
        queryset.update(hide=False)

@admin.action(description="Clear Images")
def show_product(modeladmin, request, queryset):
        queryset.update(image=None)

class ServiceCenterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id","name"]

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id","name", "available","hide"]
    ordering = ["id"]
    actions = [mark_available, mark_unavailable, hide_product, show_product]
    
class SiteSettingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["dollarvalue"]
    ...

# Register your models here.
admin.site.register(ServiceCenter, ServiceCenterAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SiteSetting, SiteSettingAdmin)


admin.site.site_header = "Duhok DXN Control Panel"
admin.site.site_title = "Control Panel"
admin.site.index_title = "Welcome To DUHOK DXN Control Panel"