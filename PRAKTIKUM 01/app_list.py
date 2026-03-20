import streamlit as st

st.title("🛡️ Cybersecurity Log Manager")

if 'my_logs' not in st.session_state:
    st.session_state.my_logs = []

# Input data baru
new_log = st.text_input("Masukkan Log Baru:")
if st.button("Tambah ke List"):
    if new_log:
        st.session_state.my_logs.append(new_log)

# Menampilkan isi list
st.subheader("Daftar Urutan Log saat ini:")
st.write(st.session_state.my_logs)

# Statistik singkat
st.info(f"Total Log dalam RAM: {len(st.session_state.my_logs)}")
