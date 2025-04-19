from flask import Flask, render_template_string

app = Flask(__name__)

# Data
mahasiswa = {
    "nama": "Agam Al Hakim Hasibuan",
    "nim": "2455201016",
    "prodi": "Teknik Informatika",
    "semester": 2
}

dosen = {
    "nama": "Dedy Gusman",
    "mata_kuliah": "Analisa dan Berorientasi Objek"
}

mata_kuliah = {
    "kode": "IF303",
    "nama": "Analisa dan Berorientasi Objek",
    "sks": "2 SKS"
}

# Template HTML dengan efek morphing dan background foto
template = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Akademik</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('/static/SS AJA..png'); /* Gambar lokal di folder static */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 1rem;
            padding: 1.5rem;
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateX(20px);
        }
        .card-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .card-body {
            font-size: 1.1rem;
        }
        h1, h4 {
            text-align: center;
            font-weight: 700;
        }
        .container {
            max-width: 1200px;
            padding-top: 100px;
        }
        .slide-up {
            animation: slide-up 2s ease-in-out;
        }
        @keyframes slide-up {
            0% { transform: translateY(100%); }
            100% { transform: translateY(0); }
        }
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container py-5 slide-up">
        <h1 class="mb-4">Sistem Informasi Akademik</h1>
        <div class="row g-4">
            <div class="col-md-6 col-lg-4">
                <div class="card">
                    <h4 class="card-title">Data Mahasiswa</h4>
                    <div class="card-body">
                        <p><strong>Nama:</strong> {{ mahasiswa.nama }}</p>
                        <p><strong>NIM:</strong> {{ mahasiswa.nim }}</p>
                        <p><strong>Prodi:</strong> {{ mahasiswa.prodi }}</p>
                        <p><strong>Semester:</strong> {{ mahasiswa.semester }}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-4">
                <div class="card">
                    <h4 class="card-title">Data Dosen</h4>
                    <div class="card-body">
                        <p><strong>Nama:</strong> {{ dosen.nama }}</p>
                        <p><strong>Mata Kuliah:</strong> {{ dosen.mata_kuliah }}</p>
                    </div>
                </div>
            </div>
            <div class="col-12 col-lg-4">
                <div class="card">
                    <h4 class="card-title">Informasi Mata Kuliah</h4>
                    <div class="card-body">
                        <p><strong>Kode:</strong> {{ mata_kuliah.kode }}</p>
                        <p><strong>Nama:</strong> {{ mata_kuliah.nama }}</p>
                        <p><strong>SKS:</strong> {{ mata_kuliah.sks }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template, mahasiswa=mahasiswa, dosen=dosen, mata_kuliah=mata_kuliah)

if __name__ == '__main__':
    app.run(debug=True)
