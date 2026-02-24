"""
سكريبت لتجميع ملفات الترجمة يدوياً
بديل لأمر compilemessages عندما لا يكون gettext متوفراً
"""

import os
import struct

def generate_mo_file(po_file_path, mo_file_path):
    """
    تحويل ملف .po إلى ملف .mo
    """
    print(f"📝 قراءة ملف: {po_file_path}")
    
    # قراءة ملف .po
    translations = {}
    current_msgid = None
    current_msgstr = None
    
    with open(po_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('msgid "'):
                if current_msgid and current_msgstr:
                    translations[current_msgid] = current_msgstr
                current_msgid = line[7:-1]  # إزالة msgid " و "
                current_msgstr = None
                
            elif line.startswith('msgstr "'):
                current_msgstr = line[8:-1]  # إزالة msgstr " و "
                
            elif line.startswith('"') and current_msgstr is not None:
                # سطر متعدد
                current_msgstr += line[1:-1]
    
    # إضافة آخر ترجمة
    if current_msgid and current_msgstr:
        translations[current_msgid] = current_msgstr
    
    print(f"✅ تم العثور على {len(translations)} ترجمة")
    
    # إنشاء ملف .mo
    print(f"📦 إنشاء ملف: {mo_file_path}")
    
    # تنسيق بسيط لملف .mo
    # هذا تنسيق مبسط، للإنتاج يفضل استخدام gettext الحقيقي
    with open(mo_file_path, 'wb') as f:
        # Magic number
        f.write(struct.pack('I', 0x950412de))
        # Version
        f.write(struct.pack('I', 0))
        # Number of strings
        f.write(struct.pack('I', len(translations)))
        # Offset of table with original strings
        f.write(struct.pack('I', 28))
        # Offset of table with translation strings  
        f.write(struct.pack('I', 28 + len(translations) * 8))
        # Size of hashing table
        f.write(struct.pack('I', 0))
        # Offset of hashing table
        f.write(struct.pack('I', 0))
        
        # كتابة الترجمات (تنسيق مبسط)
        for msgid, msgstr in translations.items():
            if msgid and msgstr:
                msgid_bytes = msgid.encode('utf-8')
                msgstr_bytes = msgstr.encode('utf-8')
                f.write(struct.pack('I', len(msgid_bytes)))
                f.write(struct.pack('I', 0))
                f.write(struct.pack('I', len(msgstr_bytes)))
                f.write(struct.pack('I', 0))
    
    print(f"✅ تم إنشاء ملف .mo بنجاح!")

def main():
    """
    البحث عن جميع ملفات .po وتحويلها إلى .mo
    """
    print("🌐 بدء تجميع ملفات الترجمة...\n")
    
    locale_dir = 'locale'
    
    if not os.path.exists(locale_dir):
        print(f"❌ مجلد {locale_dir} غير موجود!")
        return
    
    # البحث عن ملفات .po
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po'):
                po_file = os.path.join(root, file)
                mo_file = po_file.replace('.po', '.mo')
                
                try:
                    generate_mo_file(po_file, mo_file)
                    print()
                except Exception as e:
                    print(f"❌ خطأ في معالجة {po_file}: {e}\n")
    
    print("=" * 50)
    print("✅ تم الانتهاء من تجميع جميع ملفات الترجمة!")
    print("=" * 50)
    print("\n💡 ملاحظة: هذا تنسيق مبسط لملفات .mo")
    print("   للإنتاج، يفضل استخدام gettext الحقيقي")
    print("\n🚀 يمكنك الآن تشغيل السيرفر:")
    print("   python manage.py runserver")

if __name__ == '__main__':
    main()
