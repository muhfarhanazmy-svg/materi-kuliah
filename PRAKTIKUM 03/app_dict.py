import streamlit as st

st.title("🛡️ Network Threat Detector")

# Dictionary sebagai database signature serangan (Industri Nyata)
THREAT_DATABASE = {
    "192.168.1.50": "DDoS Attack Pattern",
    "10.0.0.12": "SQL Injection Attempt",
    "172.16.0.5": "Malware Callback"
}

st.subheader("Cek Integritas IP")
ip_input = st.text_input("Masukkan IP Address:")

if st.button("Scan IP"):
    # Pencarian O(1) - Langsung ketemu tanpa looping
    threat = THREAT_DATABASE.get(ip_input)
    
    if threat:
        st.error(f"⚠️ PERINGATAN: {threat} terdeteksi dari IP ini!")
    else:
        st.success("✅ IP ini bersih dari database ancaman.")

st.info("Sistem ini bekerja instan (O(1)) karena menggunakan Hash Table di RAM.")