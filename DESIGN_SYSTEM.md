# نظام التصميم - مؤسسة الكتيع للتجارة والاستيراد

## 🎨 نظام الألوان (Color Palette)

### الألوان الأساسية

#### 1. بني نحاسي داكن (Primary Brand Color)
```css
--primary-color: #5A3A22
```
- الاستخدام: العناوين الرئيسية، الشعار، النصوص المهمة
- الخصائص: لون قوي يعكس الاحترافية والثقة

#### 2. بني متوسط (Primary Medium)
```css
--primary-medium: #7B5233
```
- الاستخدام: العناوين الثانوية، الأيقونات
- الخصائص: لون متوازن بين القوة والدفء

#### 3. ذهبي نحاسي (Highlight / Gradient)
```css
--secondary-color: #B07A3F
```
- الاستخدام: الأزرار، التدرجات، العناصر التفاعلية
- الخصائص: لون مميز يجذب الانتباه

#### 4. بيج دافئ (Background Light)
```css
--bg-light: #F3EEE8
```
- الاستخدام: خلفيات الأقسام، البطاقات
- الخصائص: لون هادئ يوفر راحة بصرية

#### 5. رمادي داكن للنصوص
```css
--text-dark: #2E2E2E
```
- الاستخدام: النصوص الأساسية، المحتوى
- الخصائص: لون محايد سهل القراءة

---

## 🎨 التدرجات (Gradients)

### التدرج الرسمي
```css
background: linear-gradient(135deg, #5A3A22, #B07A3F);
```
- الاستخدام: الأزرار الرئيسية، الهيدر، أقسام CTA
- الاتجاه: 135 درجة (من أعلى اليسار لأسفل اليمين)

### تدرج خفيف للخلفيات
```css
background: linear-gradient(135deg, #F3EEE8 0%, #ffffff 100%);
```
- الاستخدام: Hero Section، خلفيات الصفحات

---

## 📝 نظام الخطوط (Typography)

### للغة العربية

#### العناوين الكبيرة
- الخط: **Cairo Bold** (700-800)
- الحجم: 2.5rem - 4rem
- الاستخدام: عناوين الصفحات الرئيسية

#### العناوين الثانوية
- الخط: **Cairo SemiBold** (600)
- الحجم: 1.5rem - 2rem
- الاستخدام: عناوين الأقسام

#### النصوص العادية
- الخط: **Cairo Regular** (400)
- الحجم: 1rem
- الاستخدام: المحتوى الأساسي

### للغة الإنجليزية
- **Montserrat** أو **Poppins** أو **Inter**
- نفس أوزان الخطوط العربية

---

## 🎯 أسلوب التصميم (Design Direction)

### الشخصية البصرية
- ✅ Minimal - تصميم بسيط وواضح
- ✅ مساحات بيضاء واسعة
- ✅ خطوط مستقيمة ونظيفة
- ✅ زوايا متوسطة (border-radius: 6px)
- ✅ ظلال خفيفة فقط

### المبادئ الأساسية
1. **البساطة**: تجنب التعقيد الزائد
2. **الوضوح**: كل عنصر له هدف واضح
3. **التناسق**: استخدام نفس الأنماط في كل الصفحات
4. **الاحترافية**: تصميم يعكس مكانة الشركة

---

## 🔲 العناصر الأساسية (Components)

### الأزرار (Buttons)

#### الزر الأساسي
```css
.btn-primary {
    background: linear-gradient(135deg, #5A3A22, #B07A3F);
    color: white;
    padding: 0.75rem 2rem;
    border-radius: 6px;
    font-weight: 600;
}
```

#### الزر الثانوي
```css
.btn-outline-primary {
    border: 2px solid #5A3A22;
    color: #5A3A22;
    background: transparent;
    border-radius: 6px;
}
```

### البطاقات (Cards)
```css
.card {
    border-radius: 6px;
    border: none;
    box-shadow: 0 2px 10px rgba(90, 58, 34, 0.08);
}

.card:hover {
    box-shadow: 0 8px 25px rgba(90, 58, 34, 0.12);
}
```

### الظلال (Shadows)
- خفيفة: `box-shadow: 0 2px 10px rgba(90, 58, 34, 0.08);`
- متوسطة: `box-shadow: 0 4px 15px rgba(90, 58, 34, 0.10);`
- قوية: `box-shadow: 0 8px 25px rgba(90, 58, 34, 0.12);`

---

## 📐 المسافات (Spacing)

### نظام المسافات
- xs: 0.25rem (4px)
- sm: 0.5rem (8px)
- md: 1rem (16px)
- lg: 1.5rem (24px)
- xl: 2rem (32px)
- xxl: 3rem (48px)

### الأقسام (Sections)
- Padding عمودي: 5rem (80px)
- Padding أفقي: Container Bootstrap

---

## 🎭 الحركات والتأثيرات (Animations)

### التأثيرات الأساسية
```css
transition: all 0.3s ease;
```

### الحركة العائمة
```css
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
```

### تأثير الـ Hover
```css
.hover-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(90, 58, 34, 0.15);
}
```

---

## 📱 التصميم المتجاوب (Responsive Design)

### نقاط التوقف (Breakpoints)
- Mobile: < 576px
- Tablet: 576px - 768px
- Desktop: 768px - 992px
- Large Desktop: > 992px

### القواعد
- Mobile First Approach
- تقليل حجم الخطوط على الشاشات الصغيرة
- تكديس العناصر عمودياً على الموبايل

---

## 🎨 أمثلة الاستخدام

### Hero Section
```html
<section style="background: linear-gradient(135deg, #F3EEE8 0%, #ffffff 100%);">
    <h1 style="color: var(--primary-color);">العنوان</h1>
    <h3 style="color: var(--secondary-color);">الشعار</h3>
    <a href="#" class="btn btn-primary">تواصل معنا</a>
</section>
```

### Card Component
```html
<div class="card hover-card" style="background: white;">
    <div class="card-body">
        <i class="fas fa-icon" style="color: var(--secondary-color);"></i>
        <h5 style="color: var(--primary-color);">العنوان</h5>
        <p class="text-muted">المحتوى</p>
    </div>
</div>
```

---

## ✅ قائمة التحقق (Checklist)

عند إضافة صفحة أو عنصر جديد، تأكد من:

- [ ] استخدام الألوان من نظام الألوان المعتمد
- [ ] استخدام خط Cairo للعربية
- [ ] border-radius: 6px للعناصر
- [ ] ظلال خفيفة فقط
- [ ] تأثيرات Hover سلسة
- [ ] التصميم متجاوب مع جميع الشاشات
- [ ] مسافات متناسقة
- [ ] تباين جيد للنصوص

---

## 🚀 التطوير المستقبلي

### المرحلة القادمة
- إضافة Dark Mode
- تحسين الحركات والتأثيرات
- إضافة المزيد من المكونات القابلة لإعادة الاستخدام
- تحسين الأداء والسرعة

---

**مؤسسة الكتيع: ريادة عالمية.. بجودة استثنائية** 🌍✨
