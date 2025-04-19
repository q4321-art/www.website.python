from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, semester, sks, prodi, dosen, matkul):
        self.nama = nama
        self.nim = nim
        self.semester = semester
        self.sks = sks
        self.prodi = prodi
        self.dosen = dosen
        self.matkul = matkul

# Object Mahasiswa
mhs1 = Mahasiswa("Agam Al Hakim Hasibuan", "2455201016", 2, "2 SKS", "Teknik Informatika", "Dedy Gusman", "Analisa dan Berorientasi Objek")
mhs2 = Mahasiswa("Budi Santoso", "2455201020", 2, "2 SKS", "Teknik Informatika", "Dedy Gusman", "Analisa dan Berorientasi Objek")

# Template HTML langsung di dalam file
template = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Sistem Akademik</title>
    <style>
        * {
            margin: 0; padding: 0; box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', sans-serif;
            background-image: url('{{ url_for('static', filename='ss aja.png') }}');
            background-size: cover;
            background-attachment: fixed;
            color: white;
            padding: 20px;
            animation: fadeIn 1.5s ease-in-out;
        }
        .container {
            background: rgba(0,0,0,0.6);
            padding: 30px;
            border-radius: 15px;
            max-width: 700px;
            margin: 50px auto;
            box-shadow: 0 0 20px rgba(255,255,255,0.2);
            transition: all 0.3s ease;
        }
        .mahasiswa {
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            transition: transform 0.3s ease;
        }
        .mahasiswa:hover {
            transform: scale(1.02);
            background: rgba(255,255,255,0.15);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Informasi Mahasiswa</h1>

        <div class="mahasiswa">
            <h3>{{ mhs1.nama }}</h3>
            <p><strong>NIM:</strong> {{ mhs1.nim }}</p>
            <p><strong>Semester:</strong> {{ mhs1.semester }}</p>
            <p><strong>SKS:</strong> {{ mhs1.sks }}</p>
            <p><strong>Prodi:</strong> {{ mhs1.prodi }}</p>
            <p><strong>Dosen:</strong> {{ mhs1.dosen }}</p>
            <p><strong>Mata Kuliah:</strong> {{ mhs1.matkul }}</p>
        </div>

        <div class="mahasiswa">
            <h3>{{ mhs2.nama }}</h3>
            <p><strong>NIM:</strong> {{ mhs2.nim }}</p>
            <p><strong>Semester:</strong> {{ mhs2.semester }}</p>
            <p><strong>SKS:</strong> {{ mhs2.sks }}</p>
            <p><strong>Prodi:</strong> {{ mhs2.prodi }}</p>
            <p><strong>Dosen:</strong> {{ mhs2.dosen }}</p>
            <p><strong>Mata Kuliah:</strong> {{ mhs2.matkul }}</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(template, mhs1=mhs1, mhs2=mhs2)

if __name__ == '__main__':
    app.run(debug=True)
