# Membuat list dataset sederhana (Analogi data Cybersecurity)
logs = ["Unauthorized Access", "Malware Detected", "SQL Injection"]

# 1. Menambah data (Append & Insert)
logs.append("DDoS Attack")
logs.insert(1, "Phishing Email")

# 2. Menghapus data (Pop & Remove)
logs.pop() # Menghapus data terakhir
logs.remove("Malware Detected")

# 3. List Comprehension (Sangat berguna untuk pengolahan data AI)
# Mengubah semua log menjadi huruf kapital
upper_logs = [log.upper() for log in logs]

print("Daftar Log:", logs)
print("Log Kapital:", upper_logs)
