# 🚀 LinkShrink: The Premium URL Shortener

> **Experience the most elegant way to shorten and share your links.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0%2B-green?style=for-the-badge&logo=django)
![UI](https://img.shields.io/badge/UI-Modern%20Glass-purple?style=for-the-badge)

Welcome to **LinkShrink v2**! We transform your long, bulky URLs into sleek, bite-sized links with a premium user experience that feels as good as it looks.

---

## ✨ New in v2.0
- **💎 Premium Glassmorphism**: A fully revamped UI with deep frosted glass effects and high-fidelity blur.
- **🌌 Dynamic Background**: Interactive, floating background blobs with vibrant radial gradients.
- **📜 Link History**: Track your 5 most recently shortened links directly on the homepage.
- **✅ Instant Clipboard Feedback**: Smooth SVG animations for copy-to-clipboard actions.
- **📱 Ultra-Responsive**: Designed to look stunning on every device, from mobile to ultra-wide displays.

---

## 🌟 Key Features

*   **🎨 Stunning Aesthetics**: A dark-themed interface using a curated color palette (Violet, Pink, Cyan).
*   **⚡ Blazing Performance**: Instant URL generation powered by a robust Django backend.
*   **📋 Pro Copy Tools**: One-click sharing with visual confirmation and short-cut open buttons.
*   **🤖 Developer API**: Seamlessly integrate LinkShrink into your own ecosystem with a built-in REST API.
*   **🔒 Security First**: Built on top of Django 5.0's industry-grade security framework.

---

## 🛠️ Installation & Setup

Set up LinkShrink on your local machine in less than 2 minutes.

### 1. Clone the Repository
```bash
git clone https://github.com/RakshitKashyap1/URL-Shortener.git
cd URL-Shortener
```

### 2. Prepare the Environment
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install requirements
pip install django djangorestframework django-cors-headers
```

### 3. Initialize & Launch
```bash
# Run migrations
python manage.py migrate

# Start the premium experience
python manage.py runserver
```

Visit `http://127.0.0.1:8000` and start shrinking!

---

## 🤖 Developer API

Integrate link shortening directly into your workflows.

### **POST /api/shorten/**
**Request Body:**
```json
{
    "long_url": "https://www.example.com/very/long/path/to/resource"
}
```

**Response:**
```json
{
    "short_code": "xK8p2L",
    "long_url": "https://www.example.com/very/long/path/to/resource",
    "short_url": "http://127.0.0.1:8000/xK8p2L",
    "created_at": "2026-01-10T23:50:00Z"
}
```

---

## � Design Philosophy
LinkShrink is built on the principles of **visual excellence** and **interaction design**. Every hover state, transition, and animation is crafted to provide a premium feel, moving away from generic MVPs toward a state-of-the-art web application.

---

## 🤝 Contributing
We love sparks! Fork, branch, and PR your ideas.
1. `git checkout -b feature/amazing-feature`
2. `git commit -m "Add some amazing feature"`
3. `git push origin feature/amazing-feature`
4. Open a Pull Request.

Made with ❤️ and ☕ by [Rakshit Kashyap].
