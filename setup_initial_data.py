"""
سكريبت لإدخال البيانات الأولية للموقع
قم بتشغيله باستخدام: python manage.py shell < setup_initial_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from company.models import CompanyInfo, Branch, CoreValue
from services.models import Service, Partnership

# إنشاء معلومات الشركة
company, created = CompanyInfo.objects.get_or_create(
    id=1,
    defaults={
        'name_ar': 'مؤسسة الكتيع للتجارة والاستيراد',
        'name_en': 'K. Trading & Importing Corp',
        'slogan_ar': 'ريادة عالمية.. بجودة استثنائية',
        'slogan_en': 'Global Leadership.. Exceptional Quality',
        'about_ar': '''من قلب اليمن، نصلكم بمنابع التجارة العالمية. نحن في مؤسسة الكتيع ندير منظومة استيراد متكاملة، مستندين إلى أذرعنا الاستراتيجية في الولايات المتحدة والخليج لتقديم حلول توريد نوعية تتجاوز التوقعات.
        
تعد مؤسسة الكتيع كياناً تجارياً رسمياً رائداً يقع مقره الرئيسي في الجمهورية اليمنية. انطلقنا برؤية تهدف إلى إعادة صياغة معايير الاستيراد والتوريد، معتمدين على شبكة دولية واسعة تمتد من أمريكا إلى الشرق الأوسط. نحن نمثل الجسر الموثوق الذي يربط السوق المحلي بأرقى الفرص التجارية العالمية، مع التزامنا التام بالاحترافية العالية والنزاهة المهنية.''',
        'about_en': 'From the heart of Yemen, we connect you to the sources of global trade...',
        'vision_ar': 'أن نظل الكيان اليمني الأكثر موثوقية وتميزاً في ربط الاحتياجات المحلية بالحلول العالمية.',
        'vision_en': 'To remain the most reliable and distinguished Yemeni entity...',
        'mission_ar': 'تقديم نموذج تجاري فريد يجمع بين الريادة العالمية والجودة الاستثنائية، ويسهم في رقي قطاع الاستيراد والتوريد عبر الشراكات الاستراتيجية الدولية.',
        'mission_en': 'To provide a unique business model...',
    }
)
print(f"✓ تم {'إنشاء' if created else 'تحديث'} معلومات الشركة")

# إنشاء الفروع
branches_data = [
    {
        'name_ar': 'المقر الرئيسي',
        'name_en': 'Main Headquarters',
        'branch_type': 'main',
        'country_ar': 'اليمن',
        'country_en': 'Yemen',
        'city_ar': 'صنعاء',
        'city_en': 'Sanaa',
        'address_ar': 'الجمهورية اليمنية',
        'address_en': 'Republic of Yemen',
        'description_ar': 'المقر الرئيسي لمؤسسة الكتيع في قلب اليمن',
        'description_en': 'Main headquarters in the heart of Yemen',
        'order': 1,
    },
    {
        'name_ar': 'الذراع الأمريكي',
        'name_en': 'American Branch',
        'branch_type': 'regional',
        'country_ar': 'الولايات المتحدة الأمريكية',
        'country_en': 'United States',
        'city_ar': 'نيويورك',
        'city_en': 'New York',
        'address_ar': 'الولايات المتحدة الأمريكية',
        'address_en': 'United States of America',
        'description_ar': 'شركتنا الأمريكية المتخصصة في المزادات العالمية، نضمن لعملائنا الوصول المباشر إلى الصفقات الكبرى والمعدات النوعية من منشئها الأصلي',
        'description_en': 'Our American company specialized in global auctions',
        'order': 2,
    },
    {
        'name_ar': 'مكتب الرياض',
        'name_en': 'Riyadh Office',
        'branch_type': 'regional',
        'country_ar': 'المملكة العربية السعودية',
        'country_en': 'Saudi Arabia',
        'city_ar': 'الرياض',
        'city_en': 'Riyadh',
        'address_ar': 'الرياض، المملكة العربية السعودية',
        'address_en': 'Riyadh, Saudi Arabia',
        'description_ar': 'مركزنا في الرياض يمثل نقطة ارتكاز تجاري تدعم تدفق التوريدات',
        'description_en': 'Our center in Riyadh represents a commercial pivot',
        'order': 3,
    },
    {
        'name_ar': 'مكتب دبي',
        'name_en': 'Dubai Office',
        'branch_type': 'regional',
        'country_ar': 'الإمارات العربية المتحدة',
        'country_en': 'United Arab Emirates',
        'city_ar': 'دبي',
        'city_en': 'Dubai',
        'address_ar': 'دبي، الإمارات العربية المتحدة',
        'address_en': 'Dubai, UAE',
        'description_ar': 'مركزنا في دبي يدعم توطين الخبرات التجارية الدولية في السوق اليمني',
        'description_en': 'Our center in Dubai supports localization of international expertise',
        'order': 4,
    },
]

for branch_data in branches_data:
    branch, created = Branch.objects.get_or_create(
        name_ar=branch_data['name_ar'],
        defaults=branch_data
    )
    print(f"✓ تم {'إنشاء' if created else 'تحديث'} فرع: {branch.name_ar}")

# إنشاء القيم الأساسية
core_values_data = [
    {
        'title_ar': 'الرسمية والموثوقية',
        'title_en': 'Formality and Reliability',
        'description_ar': 'مؤسسة مسجلة تعمل وفق أرقى بروتوكولات التجارة الرسمية',
        'description_en': 'Registered institution operating according to the highest official trade protocols',
        'icon': 'certificate',
        'order': 1,
    },
    {
        'title_ar': 'الانتقائية الفائقة',
        'title_en': 'Superior Selectivity',
        'description_ar': 'نعتمد معايير صارمة في اختيار مصادر التوريد لضمان استدامة الجودة',
        'description_en': 'We adopt strict standards in selecting supply sources',
        'icon': 'star',
        'order': 2,
    },
    {
        'title_ar': 'الانتشار الجغرافي',
        'title_en': 'Geographic Spread',
        'description_ar': 'قوة ميدانية في (اليمن، أمريكا، السعودية، الإمارات) تضمن شمولية الخدمة وتميزها',
        'description_en': 'Field presence in Yemen, America, Saudi Arabia, and UAE',
        'icon': 'globe',
        'order': 3,
    },
]

for value_data in core_values_data:
    value, created = CoreValue.objects.get_or_create(
        title_ar=value_data['title_ar'],
        defaults=value_data
    )
    print(f"✓ تم {'إنشاء' if created else 'تحديث'} قيمة: {value.title_ar}")

# إنشاء الخدمات
services_data = [
    {
        'title_ar': 'الاستيراد من أمريكا',
        'title_en': 'Import from America',
        'description_ar': 'نوفر خدمات استيراد متكاملة من الولايات المتحدة الأمريكية عبر شركتنا المتخصصة في المزادات العالمية',
        'description_en': 'We provide comprehensive import services from the United States',
        'icon': 'shipping-fast',
        'order': 1,
    },
    {
        'title_ar': 'التوريد من الخليج',
        'title_en': 'Supply from Gulf',
        'description_ar': 'حلول توريد سريعة وموثوقة من دول الخليج العربي عبر مكاتبنا في السعودية والإمارات',
        'description_en': 'Fast and reliable supply solutions from Gulf countries',
        'icon': 'truck',
        'order': 2,
    },
    {
        'title_ar': 'المزادات العالمية',
        'title_en': 'Global Auctions',
        'description_ar': 'الوصول المباشر إلى أكبر المزادات العالمية والحصول على أفضل الصفقات',
        'description_en': 'Direct access to the largest global auctions',
        'icon': 'gavel',
        'order': 3,
    },
    {
        'title_ar': 'الاستشارات التجارية',
        'title_en': 'Trade Consulting',
        'description_ar': 'نقدم استشارات متخصصة في مجال الاستيراد والتوريد والتجارة الدولية',
        'description_en': 'We provide specialized consulting in import and supply',
        'icon': 'handshake',
        'order': 4,
    },
    {
        'title_ar': 'الخدمات اللوجستية',
        'title_en': 'Logistics Services',
        'description_ar': 'حلول لوجستية متكاملة من الشحن والتخليص الجمركي حتى التوصيل',
        'description_en': 'Comprehensive logistics solutions from shipping to delivery',
        'icon': 'boxes',
        'order': 5,
    },
    {
        'title_ar': 'ضمان الجودة',
        'title_en': 'Quality Assurance',
        'description_ar': 'فحص وتقييم المنتجات قبل الشحن لضمان أعلى معايير الجودة',
        'description_en': 'Product inspection and evaluation before shipping',
        'icon': 'check-circle',
        'order': 6,
    },
]

for service_data in services_data:
    service, created = Service.objects.get_or_create(
        title_ar=service_data['title_ar'],
        defaults=service_data
    )
    print(f"✓ تم {'إنشاء' if created else 'تحديث'} خدمة: {service.title_ar}")

print("\n✅ تم إدخال جميع البيانات الأولية بنجاح!")
print("\nيمكنك الآن:")
print("1. تشغيل السيرفر: python manage.py runserver")
print("2. إنشاء حساب مدير: python manage.py createsuperuser")
print("3. زيارة لوحة الإدارة: http://127.0.0.1:8000/admin/")
