import streamlit as st
import sys

st.title("🔍 Analisis Sequence Data untuk BERT-LSTM")

# Input kalimat panjang
input_kalimat = st.text_area("Masukkan Kalimat Panjang:")
if st.button("Proses Kalimat"):
    if input_kalimat:
        # Memecah kalimat menjadi list kata
        list_kata = input_kalimat.split()
        
        # Membuat list baru dengan kata yang panjangnya lebih dari 3 karakter
        filtered_kata = [kata for kata in list_kata if len(kata) > 3]
        
        # Menghitung total penggunaan memori dari list hasil filter
        memori_digunakan = sys.getsizeof(filtered_kata)
        
        # Menampilkan hasil dalam dashboard Streamlit
        st.subheader("Hasil Filter Kata:")
        st.write(filtered_kata)
        st.info(f"Total Penggunaan Memori: {memori_digunakan} Bytes")
        #tes
#tes
#tes