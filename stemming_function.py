from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def stem_kalimat(kalimat):
    # Melakukan stemming pada kalimat
    hasil = stemmer.stem(kalimat)
    return hasil
