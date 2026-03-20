import streamlit as st

st.title("🔍 Analisis Frekuensi Kata dari Paragraf")
# Input paragraf teks panjang
input_paragraf = st.text_area("Masukkan Paragraf Teks Panjang:")
if st.button("Hitung Frekuensi Kata"):
    if input_paragraf:
        # Bersihkan teks dari simbol
        simbol = ".,!?;:\"'/%$#@&*()[]{}<>-"
        for s in simbol:
            input_paragraf = input_paragraf.replace(s, "")

        # Gunakan dictionary untuk menghitung frekuensi kemunculan setiap kata
        word_count = {}
        for kata in input_paragraf.split():
            kata = kata.lower()  # Normalisasi ke huruf kecil
            if kata in word_count:
                word_count[kata] += 1
            else:
                word_count[kata] = 1
        # Tampilkan daftar kata unik dan jumlahnya dalam tabel Streamlit
        st.subheader("Frekuensi Kata Unik:")
        st.table({"Kata": list(word_count.keys()), "Frekuensi": list(word_count.values())})
