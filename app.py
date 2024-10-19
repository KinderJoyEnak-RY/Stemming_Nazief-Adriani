from flask import Flask, render_template, request
from stemming_function import stem_kalimat

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stem', methods=['POST'])
def stem():
    kalimat = request.form['kalimat']
    hasil_stemming = stem_kalimat(kalimat)

    # Split kalimat dan hasil stemming menjadi list
    kata_asli = kalimat.split()
    kata_dasar = hasil_stemming.split()

    # Gabungkan kedua list tersebut menjadi list pasangan
    detail_proses = list(zip(kata_asli, kata_dasar))

    return render_template('index.html', kalimat=kalimat, hasil_stemming=hasil_stemming, detail_proses=detail_proses)


if __name__ == '__main__':
    app.run(debug=True)
