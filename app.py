"""
Japanese Learning App - Backend Flask
Aplikasi pembelajaran Bahasa Jepang dari Zero to N4
"""

from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Data materi pembelajaran (nanti bisa dipindah ke database)
LEARNING_MATERIALS = {
    "fase-fondasi": {
        "name": "Fase Fondasi",
        "description": "Dasar-dasar Bahasa Jepang untuk pemula",
        "color": "#FF6B6B",
        "lessons": [
            {"id": "hiragana", "title": "Hiragana", "completed": False},
            {"id": "katakana", "title": "Katakana", "completed": False},
            {"id": "basic-greetings", "title": "Salam Dasar", "completed": False},
        ]
    },
    "n5": {
        "name": "Level N5",
        "description": "Materi JLPT N5 - Level Dasar",
        "color": "#4ECDC4",
        "lessons": [
            {"id": "particles-basic", "title": "Partikel Dasar (は、が、を)", "completed": False},
            {"id": "verbs-present", "title": "Kata Kerja Bentuk Sekarang", "completed": False},
            {"id": "numbers", "title": "Angka dan Hitungan", "completed": False},
        ]
    },
    "n4": {
        "name": "Level N4",
        "description": "Materi JLPT N4 - Level Menengah Awal",
        "color": "#95E1D3",
        "lessons": [
            {"id": "verbs-past", "title": "Kata Kerja Bentuk Lampau", "completed": False},
            {"id": "te-form", "title": "Te-form dan Penggunaannya", "completed": False},
            {"id": "adjectives", "title": "Kata Sifat (い-adjective & な-adjective)", "completed": False},
        ]
    }
}

# Sample lesson content (nanti bisa dipindah ke database atau file JSON)
LESSON_CONTENT = {
    "hiragana": {
        "title": "Hiragana - Aksara Jepang Dasar",
        "category": "fase-fondasi",
        "content": """
        <h2>Apa itu Hiragana?</h2>
        <p>Hiragana (ひらがな) adalah salah satu dari tiga sistem penulisan bahasa Jepang. 
        Hiragana digunakan untuk menulis kata-kata asli Jepang dan partikel tata bahasa.</p>
        
        <h3>Vokal Dasar (あいうえお)</h3>
        <div class="hiragana-grid">
            <div class="char-item">
                <span class="hiragana">あ</span>
                <span class="romaji">a</span>
            </div>
            <div class="char-item">
                <span class="hiragana">い</span>
                <span class="romaji">i</span>
            </div>
            <div class="char-item">
                <span class="hiragana">う</span>
                <span class="romaji">u</span>
            </div>
            <div class="char-item">
                <span class="hiragana">え</span>
                <span class="romaji">e</span>
            </div>
            <div class="char-item">
                <span class="hiragana">お</span>
                <span class="romaji">o</span>
            </div>
        </div>
        
        <h3>Konsonan K (かきくけこ)</h3>
        <div class="hiragana-grid">
            <div class="char-item">
                <span class="hiragana">か</span>
                <span class="romaji">ka</span>
            </div>
            <div class="char-item">
                <span class="hiragana">き</span>
                <span class="romaji">ki</span>
            </div>
            <div class="char-item">
                <span class="hiragana">く</span>
                <span class="romaji">ku</span>
            </div>
            <div class="char-item">
                <span class="hiragana">け</span>
                <span class="romaji">ke</span>
            </div>
            <div class="char-item">
                <span class="hiragana">こ</span>
                <span class="romaji">ko</span>
            </div>
        </div>
        
        <p><strong>Tips:</strong> Latih menulis setiap karakter 10-20 kali untuk mengingat dengan baik!</p>
        """,
        "quiz": [
            {
                "question": "Bagaimana cara membaca 'あ'?",
                "options": ["a", "i", "u", "e"],
                "correct": 0
            },
            {
                "question": "Hiragana untuk 'ka' adalah?",
                "options": ["き", "か", "く", "け"],
                "correct": 1
            },
            {
                "question": "Bagaimana cara membaca 'こ'?",
                "options": ["ka", "ki", "ku", "ko"],
                "correct": 3
            }
        ]
    }
}


# ============= ROUTES =============

@app.route('/')
def landing():
    """Landing page - halaman utama"""
    return render_template('landing.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard materi - menampilkan semua kategori dan lesson"""
    return render_template('dashboard.html', materials=LEARNING_MATERIALS)


@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    """Halaman belajar - menampilkan materi dan quiz"""
    lesson_data = LESSON_CONTENT.get(lesson_id)
    
    if not lesson_data:
        return "Lesson not found", 404
    
    return render_template('lesson.html', lesson=lesson_data, lesson_id=lesson_id)


# ============= API ENDPOINTS =============

@app.route('/api/progress', methods=['GET', 'POST'])
def progress():
    """
    API untuk manajemen progress
    GET: Ambil progress user (dari LocalStorage di frontend)
    POST: Update progress user (ke LocalStorage di frontend)
    """
    if request.method == 'POST':
        # Untuk future: simpan ke database
        data = request.json
        return jsonify({"status": "success", "message": "Progress saved"})
    
    # Untuk future: ambil dari database
    return jsonify({"status": "success", "progress": {}})


@app.route('/api/materials')
def get_materials():
    """API untuk mendapatkan semua materi pembelajaran"""
    return jsonify(LEARNING_MATERIALS)


@app.route('/api/lesson/<lesson_id>')
def get_lesson(lesson_id):
    """API untuk mendapatkan detail lesson"""
    lesson_data = LESSON_CONTENT.get(lesson_id)
    
    if not lesson_data:
        return jsonify({"error": "Lesson not found"}), 404
    
    return jsonify(lesson_data)


if __name__ == '__main__':
    # Jalankan server di localhost:5000
    # Debug mode aktif untuk development
    app.run(debug=True, host='0.0.0.0', port=5000)