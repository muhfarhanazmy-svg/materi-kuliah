#membuat struktur data dictionary
userLogin = {"name": "Farhan ganteng banget", "age":18, "role":"rajajawa"}
print(type(userLogin))
# Mengakses Data

print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']} Tahun")
print(f"Role Akun : {userLogin['role']}")

#akses data seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

# Menambah Data kedalam dictionary big-O O(1)
userLogin["email"] = "farhangantengbanget@gmail.com"
print(userLogin)

# Menghapus Data dari dictionary big-O O(1)
userLogin.pop("age")
print(userLogin)

#mengubah data dalam dictionary big-O O(1)
userLogin["role"] = "raja uinssc"
print(userLogin)

#nested dictionary
dbUser = {"user1": {"name": "Farhankerenbgt", "age": 18, "role": "raja uinssc"},
          "user2": {"name": "Fahminormal", "age": 19, "role": "raja jawa"},
          "user3": {"name": "Fahribiasaaja", "age": 20, "role": "panglima jawa"}}

print(dbUser)

#akses value base key
print(dbUser["user1"])

#melakukan pencarian data dalam dictionary
finword = input("Masukkan nama user yang ingin dicari: ")
if finword in dbUser:
    print("Data ditemukan")
    print(dbUser[finword])
else:
    print("Data tidak ditemukan")