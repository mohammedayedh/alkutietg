# دليل نظام الترجمة المتعدد اللغات 🌐

## نظرة عامة

تم تفعيل نظام الترجمة المتعدد اللغات في الموقع لدعم اللغتين:
- 🇸🇦 العربية (ar) - اللغة الافتراضية
- 🇺🇸 الإنجليزية (en)

---

## ✅ ما تم إنجازه

### 1. تفعيل i18n في Django
- ✅ إضافة `LocaleMiddleware` في settings.py
- ✅ تفعيل `USE_I18N` و `USE_L10N`
- ✅ تحديد اللغات المدعومة في `LANGUAGES`
- ✅ إنشاء مجلد `locale` لملفات الترجمة

### 2. تحديث URLs
- ✅ إضافة `i18n_patterns` للمسارات
- ✅ إضافة مسار تبديل اللغة `/i18n/`
- ✅ دعم بادئة اللغة في الروابط (ar/, en/)

### 3. تحديث القوالب (Templates)
- ✅ إضافة `{% load i18n %}` في جميع الصفحات
- ✅ تحديث القالب الأساسي (base.html)
- ✅ إضافة زر تبديل اللغة في Navbar
- ✅ دعم RTL/LTR تلقائياً
- ✅ تحديث Bootstrap حسب اللغة

### 4. ترجمة المحتوى
- ✅ ترجمة جميع النصوص الثابتة
- ✅ ترجمة القوائم والأزرار
- ✅ ترجمة الرسائل (Messages)
- ✅ ترجمة لوحة الإدارة

### 5. ملفات الترجمة
- ✅ إنشاء ملف `locale/en/LC_MESSAGES/django.po`
- ✅ ترجمة أكثر من 60 نص

---

## 🎯 كيفية الاستخدام

### للمستخدم:
1. افتح الموقع
2. ابحث عن قائمة اللغة في أعلى الصفحة (Navbar)
3. اختر اللغة المطلوبة (العربية/English)
4. سيتم تحديث الصفحة تلقائياً

### للمطور:

#### إضافة نص جديد للترجمة:

**في القوالب (Templates):**
```django
{% load i18n %}
<h1>{% trans "النص بالعربية" %}</h1>
```

**في Python (Views/Models):**
```python
from django.utils.translation import gettext_lazy as _

message = _("النص بالعربية")
```

#### إضافة ترجمة جديدة:
1. افتح ملف `locale/en/LC_MESSAGES/django.po`
2. أضف الترجمة:
```po
msgid "النص بالعربية"
msgstr "English Text"
```
3. احفظ الملف
4. أعد تشغيل السيرفر

---

## 📂 هيكل الملفات

```
alkutietg/
├── locale/
│   └── en/
│       └── LC_MESSAGES/
│           └── django.po          # ملف الترجمة الإنجليزية
├── config/
│   ├── settings.py                # إعدادات i18n
│   └── urls.py                    # مسارات اللغة
└── templates/
    ├── base.html                  # زر تبديل اللغة
    └── home/
        ├── index.html             # صفحات مترجمة
        ├── about.html
        ├── services.html
        └── contact.html
```

---

## 🔧 الإعدادات المهمة

### في `config/settings.py`:
```python
LANGUAGE_CODE = 'ar'  # اللغة الافتراضية

LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

USE_I18N = True
USE_L10N = True
```

### في `config/urls.py`:
```python
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
)
```

---

## 🎨 التصميم المتجاوب مع اللغة

### RTL/LTR التلقائي:
```html
<html lang="{{ LANGUAGE_CODE }}" 
      dir="{% if LANGUAGE_CODE == 'ar' %}rtl{% else %}ltr{% endif %}">
```

### Bootstrap حسب اللغة:
```django
{% if LANGUAGE_CODE == 'ar' %}
    <link href="bootstrap.rtl.min.css" rel="stylesheet">
{% else %}
    <link href="bootstrap.min.css" rel="stylesheet">
{% endif %}
```

### الأيقونات حسب الاتجاه:
```django
<i class="fas fa-icon {% if LANGUAGE_CODE == 'ar' %}me-2{% else %}ms-2{% endif %}"></i>
```

---

## 📝 قائمة النصوص المترجمة

### القوائم والتنقل:
- ✅ الرئيسية / Home
- ✅ من نحن / About Us
- ✅ خدماتنا / Our Services
- ✅ تواصل معنا / Contact Us

### الشعارات:
- ✅ مؤسسة الكتيع للتجارة والاستيراد
- ✅ ريادة عالمية.. بجودة استثنائية
- ✅ من قلب اليمن، نصلكم بمنابع التجارة العالمية

### الأقسام:
- ✅ شبكتنا العالمية / Our Global Network
- ✅ ميزاتنا التنافسية / Our Competitive Advantages
- ✅ قيمنا الأساسية / Our Core Values
- ✅ شراكاتنا الاستراتيجية / Our Strategic Partnerships

### النماذج:
- ✅ الاسم الكامل / Full Name
- ✅ البريد الإلكتروني / Email
- ✅ رقم الهاتف / Phone Number
- ✅ الموضوع / Subject
- ✅ الرسالة / Message
- ✅ إرسال الرسالة / Send Message

### الرسائل:
- ✅ تم إرسال رسالتك بنجاح
- ✅ حدث خطأ أثناء إرسال الرسالة
- ✅ تم الاشتراك في النشرة البريدية

---

## 🚀 التطوير المستقبلي

### المرحلة القادمة:
- [ ] ترجمة محتوى قاعدة البيانات (الخدمات، الفروع، إلخ)
- [ ] إضافة لغات إضافية (فرنسي، ألماني، إلخ)
- [ ] تحسين SEO للصفحات المترجمة
- [ ] إضافة Sitemap متعدد اللغات
- [ ] ترجمة رسائل البريد الإلكتروني

### ترجمة محتوى قاعدة البيانات:

يمكن استخدام حزمة `django-modeltranslation` لترجمة محتوى النماذج:

```bash
pip install django-modeltranslation
```

```python
# في translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Service

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Service, ServiceTranslationOptions)
```

---

## 🐛 استكشاف الأخطاء

### المشكلة: الترجمة لا تظهر
**الحل:**
1. تأكد من وجود `{% load i18n %}` في أعلى القالب
2. تأكد من استخدام `{% trans "النص" %}` بشكل صحيح
3. أعد تشغيل السيرفر

### المشكلة: اتجاه النص خاطئ
**الحل:**
1. تأكد من وجود `dir="{% if LANGUAGE_CODE == 'ar' %}rtl{% else %}ltr{% endif %}"` في `<html>`
2. تأكد من استخدام Bootstrap RTL للعربية

### المشكلة: زر تبديل اللغة لا يعمل
**الحل:**
1. تأكد من وجود `path('i18n/', include('django.conf.urls.i18n'))` في urls.py
2. تأكد من وجود `LocaleMiddleware` في MIDDLEWARE

---

## 📚 مصادر إضافية

- [Django Internationalization Documentation](https://docs.djangoproject.com/en/stable/topics/i18n/)
- [Django Translation Documentation](https://docs.djangoproject.com/en/stable/topics/i18n/translation/)
- [Bootstrap RTL](https://getbootstrap.com/docs/5.3/getting-started/rtl/)

---

## ✅ قائمة التحقق

عند إضافة صفحة جديدة:
- [ ] إضافة `{% load i18n %}` في أعلى القالب
- [ ] استخدام `{% trans "النص" %}` لجميع النصوص
- [ ] إضافة الترجمات في `locale/en/LC_MESSAGES/django.po`
- [ ] اختبار الصفحة باللغتين
- [ ] التأكد من RTL/LTR يعمل بشكل صحيح
- [ ] التأكد من الأيقونات في الاتجاه الصحيح

---

**مؤسسة الكتيع: ريادة عالمية.. بجودة استثنائية** 🌍✨
