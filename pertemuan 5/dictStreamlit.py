import streamlit as st

st.title("Aplikasi Dictionary")
st.subheader("hitung kata dalam paragraph")

textinput = st.text_area("Masukkan Paragraf:",height=200)

if st.button("Hitung Analisis"):
    words = textinput.lower().split()
    count = {}
    
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    st.subheader("Hasil Analisis Kata:")
    st.write(count)
    st.bar_chart(count)

