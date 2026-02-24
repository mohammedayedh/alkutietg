from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from company.models import CompanyInfo, Branch, CoreValue
from services.models import Service, Partnership
from contact.models import ContactMessage, Newsletter

def set_language(request):
    """تبديل اللغة"""
    if request.method == 'POST':
        language = request.POST.get('language', 'ar')
        next_url = request.POST.get('next', '/')
        
        # حفظ اللغة في الجلسة
        request.session['django_language'] = language
        
        return redirect(next_url)
    return redirect('home')

def home(request):
    """الصفحة الرئيسية"""
    context = {
        'company': CompanyInfo.objects.first(),
        'branches': Branch.objects.filter(is_active=True),
        'core_values': CoreValue.objects.filter(is_active=True),
        'services': Service.objects.filter(is_active=True)[:6],
        'partnerships': Partnership.objects.filter(is_active=True),
    }
    return render(request, 'home/index.html', context)

def about(request):
    """صفحة من نحن"""
    context = {
        'company': CompanyInfo.objects.first(),
        'branches': Branch.objects.filter(is_active=True),
        'core_values': CoreValue.objects.filter(is_active=True),
    }
    return render(request, 'home/about.html', context)

def services_page(request):
    """صفحة الخدمات"""
    context = {
        'services': Service.objects.filter(is_active=True),
        'partnerships': Partnership.objects.filter(is_active=True),
    }
    return render(request, 'home/services.html', context)

def contact_page(request):
    """صفحة التواصل"""
    if request.method == 'POST':
        try:
            ContactMessage.objects.create(
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                company=request.POST.get('company', ''),
                subject=request.POST.get('subject'),
                message=request.POST.get('message'),
            )
            messages.success(request, _('تم إرسال رسالتك بنجاح. سنتواصل معك قريباً.'))
            return redirect('contact')
        except Exception as e:
            messages.error(request, _('حدث خطأ أثناء إرسال الرسالة. يرجى المحاولة مرة أخرى.'))
    
    context = {
        'company': CompanyInfo.objects.first(),
        'branches': Branch.objects.filter(is_active=True),
    }
    return render(request, 'home/contact.html', context)

def newsletter_subscribe(request):
    """الاشتراك في النشرة البريدية"""
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.get_or_create(email=email)
            messages.success(request, _('تم الاشتراك في النشرة البريدية بنجاح.'))
        else:
            messages.error(request, _('يرجى إدخال البريد الإلكتروني.'))
    return redirect(request.META.get('HTTP_REFERER', 'home'))
