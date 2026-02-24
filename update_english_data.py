#!/usr/bin/env python
"""
سكريبت لإضافة البيانات الإنجليزية إلى قاعدة البيانات
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from company.models import CompanyInfo, Branch, CoreValue
from services.models import Service, Partnership

def update_company_info():
    """تحديث معلومات الشركة"""
    company = CompanyInfo.objects.first()
    if company:
        company.name_en = "K. Trading & Importing Corporation"
        company.slogan_en = "Global Leadership.. Exceptional Quality"
        company.about_en = "From the heart of Yemen, we connect you to the sources of global trade. At K. Trading Corporation, we manage an integrated import system, relying on our strategic arms in the United States and the Gulf to provide quality supply solutions that exceed expectations."
        company.vision_en = "To remain the most reliable and distinguished Yemeni entity in connecting local needs with global solutions."
        company.mission_en = "To provide a unique business model that combines global leadership and exceptional quality, and contributes to the advancement of the import and supply sector through international strategic partnerships."
        company.save()
        print("✓ تم تحديث معلومات الشركة")

def update_branches():
    """تحديث معلومات الفروع"""
    branches_data = {
        'المقر الرئيسي - اليمن': {
            'name_en': 'Headquarters - Yemen',
            'country_en': 'Republic of Yemen',
            'city_en': 'Sana\'a',
            'address_en': 'Main Office, Sana\'a, Yemen',
            'description_en': 'Our main headquarters in Yemen, the center of our operations'
        },
        'الذراع الأمريكي': {
            'name_en': 'American Branch',
            'country_en': 'United States of America',
            'city_en': 'New York',
            'address_en': 'New York, USA',
            'description_en': 'Through our American company specialized in global auctions, we ensure direct access to major deals'
        },
        'المكتب الإقليمي - السعودية': {
            'name_en': 'Regional Office - Saudi Arabia',
            'country_en': 'Kingdom of Saudi Arabia',
            'city_en': 'Riyadh',
            'address_en': 'Riyadh, Saudi Arabia',
            'description_en': 'Our center in Riyadh represents a commercial pivot supporting the flow of supplies'
        },
        'المكتب الإقليمي - الإمارات': {
            'name_en': 'Regional Office - UAE',
            'country_en': 'United Arab Emirates',
            'city_en': 'Dubai',
            'address_en': 'Dubai, UAE',
            'description_en': 'Our center in Dubai represents a commercial pivot supporting the flow of supplies'
        }
    }
    
    for branch in Branch.objects.all():
        if branch.name_ar in branches_data:
            data = branches_data[branch.name_ar]
            for key, value in data.items():
                setattr(branch, key, value)
            branch.save()
            print(f"✓ تم تحديث: {branch.name_ar}")

def update_core_values():
    """تحديث القيم الأساسية"""
    values_data = {
        'الرسمية والموثوقية': {
            'title_en': 'Formality and Reliability',
            'description_en': 'A registered institution operating according to the highest official trade protocols'
        },
        'الانتقائية الفائقة': {
            'title_en': 'Superior Selectivity',
            'description_en': 'We adopt strict standards in selecting supply sources to ensure quality sustainability'
        },
        'الانتشار الجغرافي': {
            'title_en': 'Geographic Spread',
            'description_en': 'Field presence in Yemen, America, Saudi Arabia, and UAE ensures comprehensive and distinguished service'
        }
    }
    
    for value in CoreValue.objects.all():
        if value.title_ar in values_data:
            data = values_data[value.title_ar]
            value.title_en = data['title_en']
            value.description_en = data['description_en']
            value.save()
            print(f"✓ تم تحديث: {value.title_ar}")

def update_services():
    """تحديث الخدمات"""
    services_data = {
        'استيراد المعدات الثقيلة': {
            'title_en': 'Heavy Equipment Import',
            'description_en': 'We provide comprehensive solutions for importing heavy equipment and machinery from global sources'
        },
        'المزادات العالمية': {
            'title_en': 'Global Auctions',
            'description_en': 'Direct access to major global auctions through our American arm'
        },
        'التوريد المتخصص': {
            'title_en': 'Specialized Supply',
            'description_en': 'Specialized supply solutions that meet the needs of various sectors'
        },
        'الاستشارات التجارية': {
            'title_en': 'Trade Consulting',
            'description_en': 'Professional consulting services in the field of import and international trade'
        },
        'الخدمات اللوجستية': {
            'title_en': 'Logistics Services',
            'description_en': 'Integrated logistics solutions from source to final destination'
        },
        'إدارة سلاسل التوريد': {
            'title_en': 'Supply Chain Management',
            'description_en': 'Professional management of supply chains with the highest efficiency standards'
        }
    }
    
    for service in Service.objects.all():
        if service.title_ar in services_data:
            data = services_data[service.title_ar]
            service.title_en = data['title_en']
            service.description_en = data['description_en']
            service.save()
            print(f"✓ تم تحديث: {service.title_ar}")

def update_partnerships():
    """تحديث الشراكات"""
    # يمكن إضافة بيانات الشراكات هنا إذا كانت موجودة
    print("✓ لا توجد شراكات لتحديثها حالياً")

if __name__ == '__main__':
    print("بدء تحديث البيانات الإنجليزية...")
    print("-" * 50)
    
    update_company_info()
    update_branches()
    update_core_values()
    update_services()
    update_partnerships()
    
    print("-" * 50)
    print("✓ تم الانتهاء من تحديث جميع البيانات!")
