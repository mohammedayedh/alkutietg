from django.db import models

class Service(models.Model):
    """الخدمات التي تقدمها الشركة"""
    title_ar = models.CharField(max_length=200, verbose_name="العنوان بالعربية")
    title_en = models.CharField(max_length=200, verbose_name="العنوان بالإنجليزية")
    description_ar = models.TextField(verbose_name="الوصف بالعربية")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزية")
    icon = models.CharField(max_length=50, blank=True, verbose_name="أيقونة")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="صورة")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title_ar


class Partnership(models.Model):
    """الشراكات والتحالفات الدولية"""
    name_ar = models.CharField(max_length=200, verbose_name="اسم الشريك بالعربية")
    name_en = models.CharField(max_length=200, verbose_name="اسم الشريك بالإنجليزية")
    description_ar = models.TextField(verbose_name="الوصف بالعربية")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزية")
    country_ar = models.CharField(max_length=100, verbose_name="الدولة بالعربية")
    country_en = models.CharField(max_length=100, verbose_name="الدولة بالإنجليزية")
    logo = models.ImageField(upload_to='partnerships/', blank=True, null=True, verbose_name="الشعار")
    website = models.URLField(blank=True, verbose_name="الموقع الإلكتروني")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    
    class Meta:
        verbose_name = "شراكة"
        verbose_name_plural = "الشراكات"
        ordering = ['order', 'name_ar']
    
    def __str__(self):
        return self.name_ar
