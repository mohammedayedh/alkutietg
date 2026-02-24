from django.contrib import admin
from .models import CompanyInfo, Branch, CoreValue

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'name_en']
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name_ar', 'name_en', 'slogan_ar', 'slogan_en', 'logo', 'hero_video')
        }),
        ('نبذة عن الشركة', {
            'fields': ('about_ar', 'about_en')
        }),
        ('الرؤية والرسالة', {
            'fields': ('vision_ar', 'vision_en', 'mission_ar', 'mission_en')
        }),
    )

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'branch_type', 'country_ar', 'city_ar', 'is_active', 'order']
    list_filter = ['branch_type', 'country_ar', 'is_active']
    search_fields = ['name_ar', 'name_en', 'city_ar', 'city_en']
    list_editable = ['order', 'is_active']

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ['title_ar', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title_ar', 'title_en']
