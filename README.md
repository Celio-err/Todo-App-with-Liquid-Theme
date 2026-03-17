# 🌊 Todo App with Liquid Theme

A sophisticated Todo List application built with **Django** and **Tailwind CSS**, featuring a fluid "Liquid" UI design, Dark Mode persistence, and Timor-Leste localized time tracking.

## ✨ Fitur Utama
- **Liquid UI**: Desain modern menggunakan teknik glassmorphism dengan animasi blob.
- **Dark/Light Mode**: Pilihan tema yang tersimpan otomatis (LocalStorage).
- **Localized Time**: Pencatatan waktu selesai otomatis menggunakan zona waktu `Asia/Dili`.
- **Responsive**: Tampilan optimal di laptop maupun perangkat mobile.
- **CRUD**: Sistem pembuatan, penyelesaian, dan penghapusan tugas yang interaktif.

## 🚀 Teknologi yang Digunakan
- **Backend**: Python 3.x, Django 5.x
- **Frontend**: Tailwind CSS, JavaScript (Vanilla)
- **Database**: SQLite3

## 🛠️ Cara Menjalankan Proyek Secara Lokal
1. **Clone repositori ini:**
   git clone [https://github.com/Celio-err/Todo-App-with-Liquid-Theme.git](https://github.com/Celio-err/Todo-App-with-Liquid-Theme.git)

Buat dan aktifkan Virtual Environment:

python -m venv env
# Untuk Windows (Lenovo):
.\env\Scripts\activate
Instal Library yang dibutuhkan:


pip install django tzdata
Jalankan Migrasi Database:


python manage.py migrate
Jalankan Server:


python manage.py runserver
Buka http://127.0.0.1:8000 di browser Anda.

👤 Author
Celio Sousa Silva - Software Developer