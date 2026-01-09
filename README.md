# 🚀 LinkShrink: The Premium URL Shortener

> **Because long URLs are *so* 2010.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0%2B-green?style=for-the-badge&logo=django)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

Welcome to **LinkShrink**! We take your monstrously long, ugly URLs and magically transform them into sleek, bite-sized links. It's not just a tool; it's a lifestyle choice for your browser bar. ✨

Featuring a stunning **Glassmorphism UI** that looks so good, you might just shorten URLs for fun.

---

## 🌟 Features

*   **🎨 Beautiful UI**: A modern, responsive interface with floating blobs and frosted glass effects.
*   **⚡ Blazing Fast**: Shorten links in the blink of an eye.
*   **📋 One-Click Copy**: Because highlighting and pressing Ctrl+C is too much work.
*   **🤖 API Ready**: Built-in REST API for developers who want to crunch links programmatically.
*   **🛡️ Robust Error Handling**: We catch errors so you don't have to.
*   **🔒 Secure**: Built with Django's iron-clad security features.

---

## 🛠️ Installation & Setup

Ready to shrink some links? Follow these simple steps to get running on your local machine.

### Prerequisites

*   Python installed (because... obviously).
*   A terminal that you know how to love.

### 1. Clone the Repo
Grab the code from the repository:
```bash
git clone https://github.com/RakshitKashyap1/URL-Shortener.git
cd URL-Shortener
```

### 2. Set Up Virtual Environment (Optional but Recommended)
Keep things clean!
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Feed the beast:
```bash
pip install django djangorestframework django-cors-headers
```

### 4. Run Migrations
Set up the database (SQLite by default):
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Launch the Server 🚀
Ignition using port 8000 (or whichever you prefer):
```bash
python manage.py runserver
```

Now open your browser and navigate to `http://127.0.0.1:8000`. Behold the glory!

---

## 🤖 API Documentation

Want to integrate LinkShrink into your own app? We got you.

### **Endpoint: Shorten URL**
`POST /api/shorten/`

**Request Body (JSON):**
```json
{
    "long_url": "https://www.super-long-website-address.com/very/deep/path"
}
```

**Response (JSON):**
```json
{
    "short_code": "aX9d2",
    "long_url": "https://www.super-long-website-address.com/very/deep/path",
    "short_url": "http://127.0.0.1:8000/aX9d2",
    "created_at": "2026-01-09T10:00:00Z"
}
```

---

## 📸 Screenshots

*(Imagine a beautiful screenshot of a dark-themed, glass-effect UI here)*
*It looks amazing, trust us.*

---

## 🤝 Contributing

Found a bug? Want to add a sparkle effect? PRs are welcome!
1. Fork it.
2. Branch it (`git checkout -b feature/cool-sparkles`).
3. Commit it (`git commit -m "Added cool sparkles"`).
4. Push it (`git push origin feature/cool-sparkles`).
5. PR it.

Made with ❤️ and ☕ by [Rakshit Kashyap].
