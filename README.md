# Faculty Scraper 📚

سكربت Python يقوم بسحب بيانات الهيئة التدريسية من موقع قسم هندسة الحاسوب في الجامعة الإسلامية، ومن ثم تخزينها في قاعدة بيانات SQL Server.

## ⚙️ المهام التي يقوم بها:

- Web Scraping باستخدام BeautifulSoup
- استخراج: الاسم، الرتبة، البريد الإلكتروني، رقم المكتب، الموقع الشخصي، ورقم التحويلة
- تخزين تلقائي في قاعدة بيانات SQL Server

## 🖥️ المتطلبات

- Python 3.10+
- SQL Server (يمكن تشغيله باستخدام Docker)
- مكتبات: `requests`, `beautifulsoup4`, `pyodbc`, `python-dotenv`

## 📦 التثبيت

```bash
git clone https://github.com/yourusername/faculty-scraper.git
cd faculty-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
