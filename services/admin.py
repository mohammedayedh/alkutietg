from django.contrib import admin
from .models import Service, Partnership

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title_ar', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    list_editable = ['order', 'is_active']
    date_hierarchy = 'created_at'

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'country_ar', 'order', 'is_active']
    list_filter = ['country_ar', 'is_active']
    search_fields = ['name_ar', 'name_en']
    list_editable = ['order', 'is_active']
