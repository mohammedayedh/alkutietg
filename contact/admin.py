from django.contrib import admin
from .models import ContactMessage, Newsletter

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'subject', 'message']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('معلومات المرسل', {
            'fields': ('full_name', 'email', 'phone', 'company')
        }),
        ('الرسالة', {
            'fields': ('subject', 'message')
        }),
        ('الإدارة', {
            'fields': ('status', 'notes', 'created_at', 'updated_at')
        }),
    )

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    list_editable = ['is_active']
    date_hierarchy = 'subscribed_at'
