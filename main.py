from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Data 2 mahasiswa (object)
mahasiswa1 = {
    "nama": "Agam Al Hakim Hasibuan",
    "nim": "2455201016",
    "semester": "2",
    "sks": "2 SKS",
    "prodi": "Teknik Informatika",
    "dosen": "Dedy Gusman",
    "matkul": "Analisa dan Berorientasi Objek"
}

mahasiswa2 = {
    "nama": "Adit Pratama",
    "nim": "2455201050",
    "semester": "2",
    "sks": "2 SKS",
    "prodi": "Teknik Informatika",
    "dosen": "Dedy Gusman",
    "matkul": "Analisa dan Berorientasi Objek"
}

# Template HTML ditulis langsung di dalam file
template = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Sistem Akademik Mahasiswa</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-image: url('{{ url_for('static', filename='background.jpg') }}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            animation: fadeIn 2s ease-in-out;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        .container {
            max-width: 800px;
            margin: 60px auto;
            padding: 30px;
            background: rgba(255,255,255,0.85);
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(6px);
            transition: transform 0.3s ease;
        }

        .container:hover {
            transform: scale(1.01);
        }

        h1 {
            text-align: center;
            color: #2e3b55;
        }

        .mahasiswa {
            margin-bottom: 40px;
        }

        ul {
            list-style: none;
            padding: 0;
            font-size: 17px;
        }

        ul li {
            margin-bottom: 10px;
        }

        @media (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Informasi Akademik Mahasiswa</h1>

        <div class="mahasiswa">
            <h2>Mahasiswa 1</h2>
            <ul>
                <li><strong>Nama:</strong> {{ m1.nama }}</li>
                <li><strong>NIM:</strong> {{ m1.nim }}</li>
                <li><strong>Semester:</strong> {{ m1.semester }}</li>
                <li><strong>SKS:</strong> {{ m1.sks }}</li>
                <li><strong>Program Studi:</strong> {{ m1.prodi }}</li>
                <li><strong>Dosen:</strong> {{ m1.dosen }}</li>
                <li><strong>Mata Kuliah:</strong> {{ m1.matkul }}</li>
            </ul>
        </div>

        <div class="mahasiswa">
            <h2>Mahasiswa 2</h2>
            <ul>
                <li><strong>Nama:</strong> {{ m2.nama }}</li>
                <li><strong>NIM:</strong> {{ m2.nim }}</li>
                <li><strong>Semester:</strong> {{ m2.semester }}</li>
                <li><strong>SKS:</strong> {{ m2.sks }}</li>
                <li><strong>Program Studi:</strong> {{ m2.prodi }}</li>
                <li><strong>Dosen:</strong> {{ m2.dosen }}</li>
                <li><strong>Mata Kuliah:</strong> {{ m2.matkul }}</li>
            </ul>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(template, m1=mahasiswa1, m2=mahasiswa2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
