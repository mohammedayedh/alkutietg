from django.db import models

class CompanyInfo(models.Model):
    """معلومات الشركة الأساسية"""
    name_ar = models.CharField(max_length=200, verbose_name="اسم الشركة بالعربية")
    name_en = models.CharField(max_length=200, verbose_name="اسم الشركة بالإنجليزية")
    slogan_ar = models.CharField(max_length=200, verbose_name="الشعار بالعربية")
    slogan_en = models.CharField(max_length=200, verbose_name="الشعار بالإنجليزية")
    about_ar = models.TextField(verbose_name="نبذة عن الشركة بالعربية")
    about_en = models.TextField(verbose_name="نبذة عن الشركة بالإنجليزية")
    vision_ar = models.TextField(verbose_name="الرؤية بالعربية")
    vision_en = models.TextField(verbose_name="الرؤية بالإنجليزية")
    mission_ar = models.TextField(verbose_name="الرسالة بالعربية")
    mission_en = models.TextField(verbose_name="الرسالة بالإنجليزية")
    logo = models.ImageField(upload_to='company/', verbose_name="الشعار")
    hero_video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="فيديو الصفحة الرئيسية")
    
    class Meta:
        verbose_name = "معلومات الشركة"
        verbose_name_plural = "معلومات الشركة"
    
    def __str__(self):
        return self.name_ar


class Branch(models.Model):
    """فروع ومكاتب الشركة"""
    BRANCH_TYPES = [
        ('main', 'المقر الرئيسي'),
        ('regional', 'مكتب إقليمي'),
        ('partner', 'شريك استراتيجي'),
    ]
    
    name_ar = models.CharField(max_length=200, verbose_name="اسم الفرع بالعربية")
    name_en = models.CharField(max_length=200, verbose_name="اسم الفرع بالإنجليزية")
    branch_type = models.CharField(max_length=20, choices=BRANCH_TYPES, verbose_name="نوع الفرع")
    country_ar = models.CharField(max_length=100, verbose_name="الدولة بالعربية")
    country_en = models.CharField(max_length=100, verbose_name="الدولة بالإنجليزية")
    city_ar = models.CharField(max_length=100, verbose_name="المدينة بالعربية")
    city_en = models.CharField(max_length=100, verbose_name="المدينة بالإنجليزية")
    address_ar = models.TextField(verbose_name="العنوان بالعربية")
    address_en = models.TextField(verbose_name="العنوان بالإنجليزية")
    phone = models.CharField(max_length=50, blank=True, verbose_name="الهاتف")
    email = models.EmailField(blank=True, verbose_name="البريد الإلكتروني")
    description_ar = models.TextField(blank=True, verbose_name="الوصف بالعربية")
    description_en = models.TextField(blank=True, verbose_name="الوصف بالإنجليزية")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    
    class Meta:
        verbose_name = "فرع"
        verbose_name_plural = "الفروع"
        ordering = ['order', 'name_ar']
    
    def __str__(self):
        return f"{self.name_ar} - {self.country_ar}"


class CoreValue(models.Model):
    """القيم والميزات التنافسية"""
    title_ar = models.CharField(max_length=200, verbose_name="العنوان بالعربية")
    title_en = models.CharField(max_length=200, verbose_name="العنوان بالإنجليزية")
    description_ar = models.TextField(verbose_name="الوصف بالعربية")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزية")
    icon = models.CharField(max_length=50, blank=True, verbose_name="أيقونة")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    
    class Meta:
        verbose_name = "قيمة أساسية"
        verbose_name_plural = "القيم الأساسية"
        ordering = ['order']
    
    def __str__(self):
        return self.title_ar
