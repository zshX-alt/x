# 🇯🇵 Japanese Learning App (Zero to N4)

Website pembelajaran Bahasa Jepang dari level pemula hingga N4.

## 📁 Struktur Folder

```
japanese-learning-app/
│
├── app.py                 # Backend Flask (main application)
├── requirements.txt       # Dependencies Python
│
├── static/               # File statis (CSS, JS, Images)
│   ├── css/
│   │   ├── main.css      # Style utama
│   │   ├── landing.css   # Style landing page
│   │   ├── dashboard.css # Style dashboard materi
│   │   └── lesson.css    # Style halaman belajar
│   │
│   ├── js/
│   │   ├── main.js       # JavaScript utama
│   │   ├── progress.js   # Manajemen progress (LocalStorage)
│   │   └── quiz.js       # Logika quiz/latihan
│   │
│   └── images/           # Gambar dan aset visual
│
└── templates/            # HTML Templates (Flask)
    ├── base.html         # Template dasar
    ├── landing.html      # Landing page
    ├── dashboard.html    # Dashboard materi
    └── lesson.html       # Halaman belajar
```

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Server
```bash
python app.py
```

### 3. Buka Browser
```
http://localhost:5000
```

## ✨ Fitur

- ✅ Landing page yang modern dan responsive
- ✅ Dashboard dengan 3 kategori materi (Fase Fondasi, N5, N4)
- ✅ Halaman belajar dengan layout split (materi + quiz)
- ✅ Progress tracking dengan LocalStorage
- ✅ Desain clean dan mobile-friendly

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python/Flask
- **Storage**: LocalStorage (untuk progress user)

## 📝 Catatan

- Progress disimpan di browser (LocalStorage), jadi data tidak hilang saat refresh
- Desain responsive, bisa dibuka di HP dengan nyaman
- Kode modular dan mudah dikembangkan