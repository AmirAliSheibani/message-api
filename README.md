# Django Chat API

یک API ساده برای ارسال و دریافت پیام با **Django + Django REST Framework**.

## ویژگی‌ها

* دریافت پیام متنی از کاربر (POST)
* ذخیره پیام‌ها در دیتابیس
* بازگرداندن لیست پیام‌ها (GET)
* پاسخ ساده‌ی سیستم هنگام ایجاد پیام
* ساختار تمیز و قابل فهم برای توسعه و گسترش
## پیش‌نیازها

* Python 3
* pip
* virtualenv یا venv

## نحوه اجرا (لوکال)

1. پروژه را کلون کنید:

```bash
git clone https://github.com/USERNAME/django-chat-api.git
cd django-chat-api
```

2. ساخت و فعال‌سازی virtualenv:

* لینوکس / macOS

```bash
python -m venv venv
source venv/bin/activate
```

* ویندوز (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

4. مایگریت‌ها و اجرای سرور:

```bash
python manage.py migrate
python manage.py runserver
```

5. باز کردن در مرورگر / تست با curl:

```
http://127.0.0.1:8000/api/chat/
```

## Endpoint ها

### GET `/api/chat/`

لیست تمام پیام‌ها را برمی‌گرداند.

**نمونه پاسخ**

```json
[
  {
    "id": 1,
    "sender": "user",
    "text": "سلام",
    "created_at": "2025-12-23T12:30:00Z"
  }
]
```

### POST `/api/chat/`

ارسال یک پیام جدید. بدنهٔ درخواست باید JSON و شامل فیلد `text` باشد.

**نمونه درخواست**

```json
{
  "text": "سلام"
}
```

**نمونه پاسخ**

```json
{
  "status": "success",
  "message": "پیام دریافت شد",
  "data": {
    "id": 2,
    "sender": "user",
    "text": "سلام",
    "created_at": "2025-12-23T12:35:00Z"
  }
}
```

**نمونه با curl**

```bash
curl -X POST http://127.0.0.1:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"text":"سلام"}'
```

## فایل‌ها و مسیرهای مهم

```
myproject/
├─ manage.py
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ myproject/          # تنظیمات پروژه
│  ├─ settings.py
│  └─ urls.py
└─ chat/               # اپ پیام‌ها
   ├─ models.py        # مدل Message
   ├─ serializers.py   # MessageCreateSerializer, MessageSerializer
   ├─ views.py         # MessageAPI
   ├─ urls.py
   └─ migrations/
```
