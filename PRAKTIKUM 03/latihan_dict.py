# 1. Membuat Dictionary (Analogi Profil User LinkedIn)
user_profile = {
    "username": "farhan_cyber",
    "role": "Researcher",
    "skills": ["Python", "BERT", "LSTM"],
    "is_active": True
}

# 2. Akses Data (O(1))
print(f"Mencari Role: {user_profile['role']}")
print(f"Apakah Aktif? {user_profile['is_active']}")
print(f"Skill Pertama: {user_profile['skills'][0]}")
print(f"Jumlah Skill: {len(user_profile['skills'])}")

# 3. Menambah/Update Data
user_profile["location"] = "Cirebon"
user_profile["role"] = "Senior Researcher"
print("role tambahan:", user_profile["role"])

# 4. Dictionary Comprehension (Efisien)
# Misal: Mengubah daftar skor menjadi status aman/tidak
scores = {"IP_1": 90, "IP_2": 45, "IP_3": 85}
security_status = {k: ("Aman" if v > 70 else "Bahaya") for k, v in scores.items()}

print("Status Keamanan:", security_status)