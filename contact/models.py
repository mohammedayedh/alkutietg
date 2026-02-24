from django.db import models

class ContactMessage(models.Model):
    """رسائل التواصل والاستفسارات"""
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('in_progress', 'قيد المعالجة'),
        ('resolved', 'تم الحل'),
        ('closed', 'مغلق'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name="الاسم الكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=50, verbose_name="رقم الهاتف")
    company = models.CharField(max_length=200, blank=True, verbose_name="اسم الشركة")
    subject = models.CharField(max_length=200, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="الحالة")
    notes = models.TextField(blank=True, verbose_name="ملاحظات إدارية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class Newsletter(models.Model):
    """الاشتراك في النشرة البريدية"""
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الاشتراك")
    
    class Meta:
        verbose_name = "مشترك في النشرة"
        verbose_name_plural = "المشتركون في النشرة"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email
