import os
from datetime import datetime

# ══════════════════════════════════════════════════════════════════════════════
#  MASTER DATA
# ══════════════════════════════════════════════════════════════════════════════

MATKUL_LIST = [
    "Bahasa Indonesia",
    "Algoritma & Pemrograman (Alpro)",
    "Aljabar Linear",
    "Matematika Diskrit (Matdis)",
    "Bahasa Inggris",
    "Struktur Data",
    "Basis Data",
]

KELAS_LIST = ["A", "B", "C", "D"]

# Mahasiswa default per kelas (bisa di-edit manual dari menu)
DEFAULT_MAHASISWA = [
    "Farhan", "Taohid", "Ummi", "Alfin",
]

# ── Runtime Storage ────────────────────────────────────────────────────────────
# Semua data disimpen di dict ini selama program jalan
# Key utama: (matkul, kelas)
data_store = {}

def get_store(matkul, kelas):
    key = (matkul, kelas)
    if key not in data_store:
        data_store[key] = {
            "mahasiswa": list(DEFAULT_MAHASISWA),
            "absensi": [],          # list of { pertemuan, tanggal, records: {nama: status} }
            "tugas": [],            # list of { id, judul, deskripsi, deadline, pengumpul: [nama] }
            "pengumuman": [],       # list of { id, judul, isi, tanggal }
            "catatan": [],          # list of { pertemuan, tanggal, materi, catatan }
            "jadwal": [],           # list of { id, acara, tanggal, waktu, keterangan }
            "tugas_counter": 1,
            
            "pengumuman_counter": 1,
            "jadwal_counter": 1,
        }
    return data_store[key]

# ══════════════════════════════════════════════════════════════════════════════
#  HELPER
# ══════════════════════════════════════════════════════════════════════════════

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header(judul, sub=""):
    print("╔" + "═" * 53 + "╗")
    print(f"║  {judul:<51}║")
    if sub:
        print(f"║  {sub:<51}║")
    print("╚" + "═" * 53 + "╝")

def divider():
    print("─" * 55)

def kembali():
    input("\n  ↩  Tekan Enter untuk kembali...")

def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def today():
    return datetime.now().strftime("%d/%m/%Y")

# ══════════════════════════════════════════════════════════════════════════════
#  1. LOGIN
# ══════════════════════════════════════════════════════════════════════════════

def login():
    clear()
    header("SISTEM INFORMASI PJ MATKUL", "Khusus Penanggung Jawab Mata Kuliah")
    print()
    nama_pj = input("  Nama PJ     : ").strip()
    if not nama_pj:
        print("\n  [!] Nama tidak boleh kosong!")
        input("  Tekan Enter untuk coba lagi...")
        return login()

    print()
    print("  Pilih Mata Kuliah:")
    for i, mk in enumerate(MATKUL_LIST, 1):
        print(f"    [{i}] {mk}")
    print()
    try:
        mk_idx = int(input("  Pilih (1-7): ")) - 1
        if not (0 <= mk_idx < len(MATKUL_LIST)):
            raise ValueError
        matkul = MATKUL_LIST[mk_idx]
    except ValueError:
        print("\n  [!] Pilihan tidak valid!")
        input("  Tekan Enter untuk coba lagi...")
        return login()

    print()
    print("  Pilih Kelas  : ", end="")
    for i, k in enumerate(KELAS_LIST, 1):
        print(f"[{i}] {k}  ", end="")
    print()
    try:
        kls_idx = int(input("  Pilih (1-4): ")) - 1
        if not (0 <= kls_idx < len(KELAS_LIST)):
            raise ValueError
        kelas = KELAS_LIST[kls_idx]
    except ValueError:
        print("\n  [!] Pilihan tidak valid!")
        input("  Tekan Enter untuk coba lagi...")
        return login()

    print(f"\n  ✅ Login berhasil! Selamat datang, {nama_pj}.")
    print(f"     Anda adalah PJ  →  {matkul} | Kelas {kelas}")
    input("\n  Tekan Enter untuk masuk...")
    return nama_pj, matkul, kelas

# ══════════════════════════════════════════════════════════════════════════════
#  2. MENU UTAMA
# ══════════════════════════════════════════════════════════════════════════════

def menu(nama_pj, matkul, kelas):
    store = get_store(matkul, kelas)
    while True:
        clear()
        header(f"PJ: {nama_pj}", f"Matkul: {matkul}  |  Kelas {kelas}")
        print()
        print("  [1]  📋  Absensi")
        print("  [2]  📝  Manajemen Tugas")
        print("  [3]  📢  Pengumuman")
        print("  [4]  📖  Catatan Perkuliahan")
        print("  [5]  📅  Jadwal & Agenda")
        print()
        print("  [6]  👥  Kelola Daftar Mahasiswa")
        print("  [0]  🚪  Logout")
        print()
        pilih = input("  Pilih menu: ").strip()

        if   pilih == "1": absensi(store, matkul, kelas)
        elif pilih == "2": manajemen_tugas(store, matkul, kelas)
        elif pilih == "3": pengumuman(store, matkul, kelas)
        elif pilih == "4": catatan_perkuliahan(store, matkul, kelas)
        elif pilih == "5": jadwal_agenda(store, matkul, kelas)
        elif pilih == "6": kelola_mahasiswa(store)
        elif pilih == "0":
            print(f"\n  Sampai jumpa, {nama_pj}! 👋\n")
            break
        else:
            print("\n  [!] Pilihan tidak valid.")
            input("  Tekan Enter...")

# ══════════════════════════════════════════════════════════════════════════════
#  3. ABSENSI
# ══════════════════════════════════════════════════════════════════════════════

def absensi(store, matkul, kelas):
    STATUS_OPT = {"1": "Hadir", "2": "Sakit", "3": "Izin", "4": "Alpha"}
    BATAS_ALPHA = 3

    while True:
        clear()
        header(f"ABSENSI  |  {matkul} Kelas {kelas}")
        print()
        print("  [1]  Buka Sesi Pertemuan Baru")
        print("  [2]  Lihat Rekap Kehadiran")
        print("  [3]  Lihat Sesi Sebelumnya")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        # ── Buka sesi baru ──────────────────────────────────────────────
        if pilih == "1":
            clear()
            header("BUKA SESI PERTEMUAN")
            pertemuan = input("\n  Pertemuan ke- : ").strip()
            tanggal   = input("  Tanggal (Enter = hari ini): ").strip() or today()
            print()
            divider()
            print(f"  {'No':<4} {'Nama':<18} Keterangan")
            divider()
            records = {}
            for i, nama in enumerate(store["mahasiswa"], 1):
                print(f"  {i:<4} {nama:<18} [1]Hadir [2]Sakit [3]Izin [4]Alpha")
                while True:
                    s = input(f"       Status: ").strip()
                    if s in STATUS_OPT:
                        records[nama] = STATUS_OPT[s]
                        break
                    print("       [!] Masukkan 1-4")

            store["absensi"].append({
                "pertemuan": pertemuan,
                "tanggal": tanggal,
                "records": records,
            })
            print(f"\n  ✅ Absensi Pertemuan {pertemuan} ({tanggal}) tersimpan!")
            kembali()

        # ── Rekap kehadiran ─────────────────────────────────────────────
        elif pilih == "2":
            clear()
            header("REKAP KEHADIRAN")
            if not store["absensi"]:
                print("\n  Belum ada data absensi.")
                kembali(); continue

            print(f"\n  {'Nama':<18} {'Hadir':>7} {'Sakit':>7} {'Izin':>7} {'Alpha':>7}  Flag")
            divider()
            for nama in store["mahasiswa"]:
                h = s = i = a = 0
                for sesi in store["absensi"]:
                    st = sesi["records"].get(nama, "-")
                    if st == "Hadir": h += 1
                    elif st == "Sakit": s += 1
                    elif st == "Izin": i += 1
                    elif st == "Alpha": a += 1
                flag = "⚠️  ALPHA ≥3" if a >= BATAS_ALPHA else ""
                print(f"  {nama:<18} {h:>7} {s:>7} {i:>7} {a:>7}  {flag}")
            kembali()

        # ── Lihat sesi lama ─────────────────────────────────────────────
        elif pilih == "3":
            clear()
            header("RIWAYAT SESI PERTEMUAN")
            if not store["absensi"]:
                print("\n  Belum ada data absensi.")
                kembali(); continue

            for sesi in store["absensi"]:
                print(f"\n  📅 Pertemuan {sesi['pertemuan']}  —  {sesi['tanggal']}")
                for nama, st in sesi["records"].items():
                    icon = "✅" if st == "Hadir" else "❌"
                    print(f"     {icon}  {nama:<18} {st}")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  4. MANAJEMEN TUGAS
# ══════════════════════════════════════════════════════════════════════════════

def manajemen_tugas(store, matkul, kelas):
    while True:
        clear()
        header(f"MANAJEMEN TUGAS  |  {matkul} Kelas {kelas}")
        print()
        print("  [1]  Tambah Tugas Baru")
        print("  [2]  Lihat Semua Tugas")
        print("  [3]  Update Pengumpulan Tugas")
        print("  [4]  Hapus Tugas")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        # ── Tambah tugas ────────────────────────────────────────────────
        if pilih == "1":
            clear()
            header("TAMBAH TUGAS BARU")
            judul   = input("\n  Judul Tugas  : ").strip()
            desk    = input("  Deskripsi    : ").strip()
            deadline = input("  Deadline     : ").strip()
            if not judul:
                print("  [!] Judul tidak boleh kosong!"); kembali(); continue

            tid = store["tugas_counter"]
            store["tugas"].append({
                "id": tid, "judul": judul,
                "deskripsi": desk, "deadline": deadline,
                "pengumpul": [],
            })
            store["tugas_counter"] += 1
            print(f"\n  ✅ Tugas #{tid} '{judul}' berhasil ditambahkan!")
            kembali()

        # ── Lihat tugas ─────────────────────────────────────────────────
        elif pilih == "2":
            clear()
            header("DAFTAR TUGAS")
            if not store["tugas"]:
                print("\n  Belum ada tugas."); kembali(); continue

            total_mhs = len(store["mahasiswa"])
            for t in store["tugas"]:
                terkumpul = len(t["pengumpul"])
                belum = [m for m in store["mahasiswa"] if m not in t["pengumpul"]]
                print(f"\n  #{t['id']}  {t['judul']}")
                print(f"      Deskripsi : {t['deskripsi']}")
                print(f"      Deadline  : {t['deadline']}")
                print(f"      Terkumpul : {terkumpul}/{total_mhs}")
                if belum:
                    print(f"      Belum     : {', '.join(belum)}")
            kembali()

        # ── Update pengumpulan ──────────────────────────────────────────
        elif pilih == "3":
            clear()
            header("UPDATE PENGUMPULAN")
            if not store["tugas"]:
                print("\n  Belum ada tugas."); kembali(); continue

            for t in store["tugas"]:
                print(f"  [{t['id']}] {t['judul']}  (deadline: {t['deadline']})")
            print()
            try:
                tid = int(input("  Pilih ID tugas: "))
                tugas_item = next((t for t in store["tugas"] if t["id"] == tid), None)
                if not tugas_item:
                    print("  [!] ID tidak ditemukan."); kembali(); continue
            except ValueError:
                print("  [!] Input harus angka."); kembali(); continue

            print(f"\n  Tugas: {tugas_item['judul']}")
            print("  Tandai yang sudah mengumpul (nama mahasiswa):")
            for i, m in enumerate(store["mahasiswa"], 1):
                sudah = "✅" if m in tugas_item["pengumpul"] else "  "
                print(f"  {sudah} [{i:>2}] {m}")
            print()
            raw = input("  Masukkan nomor (pisah koma, misal: 1,3,5): ").strip()
            try:
                indices = [int(x.strip()) - 1 for x in raw.split(",")]
                for idx in indices:
                    nama = store["mahasiswa"][idx]
                    if nama not in tugas_item["pengumpul"]:
                        tugas_item["pengumpul"].append(nama)
                print(f"\n  ✅ Data pengumpulan diperbarui!")
            except (ValueError, IndexError):
                print("  [!] Input tidak valid.")
            kembali()

        # ── Hapus tugas ─────────────────────────────────────────────────
        elif pilih == "4":
            clear()
            header("HAPUS TUGAS")
            if not store["tugas"]:
                print("\n  Belum ada tugas."); kembali(); continue
            for t in store["tugas"]:
                print(f"  [{t['id']}] {t['judul']}")
            print()
            try:
                tid = int(input("  Masukkan ID tugas yang dihapus: "))
                sebelum = len(store["tugas"])
                store["tugas"] = [t for t in store["tugas"] if t["id"] != tid]
                if len(store["tugas"]) < sebelum:
                    print(f"  ✅ Tugas #{tid} berhasil dihapus!")
                else:
                    print("  [!] ID tidak ditemukan.")
            except ValueError:
                print("  [!] Input harus angka.")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  5. PENGUMUMAN
# ══════════════════════════════════════════════════════════════════════════════

def pengumuman(store, matkul, kelas):
    while True:
        clear()
        header(f"PENGUMUMAN  |  {matkul} Kelas {kelas}")
        print()
        print("  [1]  Tambah Pengumuman")
        print("  [2]  Lihat Semua Pengumuman")
        print("  [3]  Hapus Pengumuman")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            clear()
            header("TAMBAH PENGUMUMAN")
            judul = input("\n  Judul : ").strip()
            isi   = input("  Isi   : ").strip()
            if not judul:
                print("  [!] Judul tidak boleh kosong!"); kembali(); continue

            pid = store["pengumuman_counter"]
            store["pengumuman"].append({
                "id": pid, "judul": judul,
                "isi": isi, "tanggal": now(),
            })
            store["pengumuman_counter"] += 1
            print(f"\n  ✅ Pengumuman #{pid} berhasil ditambahkan!")
            kembali()

        elif pilih == "2":
            clear()
            header("DAFTAR PENGUMUMAN")
            if not store["pengumuman"]:
                print("\n  Belum ada pengumuman."); kembali(); continue
            for p in reversed(store["pengumuman"]):   # terbaru di atas
                print(f"\n  📢 #{p['id']}  {p['judul']}")
                print(f"      {p['tanggal']}")
                print(f"      {p['isi']}")
            kembali()

        elif pilih == "3":
            clear()
            header("HAPUS PENGUMUMAN")
            if not store["pengumuman"]:
                print("\n  Belum ada pengumuman."); kembali(); continue
            for p in store["pengumuman"]:
                print(f"  [{p['id']}] {p['judul']}")
            print()
            try:
                pid = int(input("  Masukkan ID yang dihapus: "))
                sebelum = len(store["pengumuman"])
                store["pengumuman"] = [p for p in store["pengumuman"] if p["id"] != pid]
                if len(store["pengumuman"]) < sebelum:
                    print(f"  ✅ Pengumuman #{pid} dihapus!")
                else:
                    print("  [!] ID tidak ditemukan.")
            except ValueError:
                print("  [!] Input harus angka.")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  6. CATATAN PERKULIAHAN
# ══════════════════════════════════════════════════════════════════════════════

def catatan_perkuliahan(store, matkul, kelas):
    while True:
        clear()
        header(f"CATATAN PERKULIAHAN  |  {matkul} Kelas {kelas}")
        print()
        print("  [1]  Tambah Catatan Pertemuan")
        print("  [2]  Lihat Semua Catatan")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            clear()
            header("TAMBAH CATATAN PERTEMUAN")
            pertemuan = input("\n  Pertemuan ke- : ").strip()
            tanggal   = input("  Tanggal (Enter = hari ini): ").strip() or today()
            materi    = input("  Materi yang dibahas       : ").strip()
            catatan   = input("  Catatan tambahan (opsional): ").strip()

            store["catatan"].append({
                "pertemuan": pertemuan,
                "tanggal": tanggal,
                "materi": materi,
                "catatan": catatan,
            })
            print(f"\n  ✅ Catatan Pertemuan {pertemuan} tersimpan!")
            kembali()

        elif pilih == "2":
            clear()
            header("RIWAYAT CATATAN PERKULIAHAN")
            if not store["catatan"]:
                print("\n  Belum ada catatan."); kembali(); continue
            for c in store["catatan"]:
                print(f"\n  📖 Pertemuan {c['pertemuan']}  —  {c['tanggal']}")
                print(f"      Materi  : {c['materi']}")
                if c["catatan"]:
                    print(f"      Catatan : {c['catatan']}")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  7. JADWAL & AGENDA
# ══════════════════════════════════════════════════════════════════════════════

def jadwal_agenda(store, matkul, kelas):
    while True:
        clear()
        header(f"JADWAL & AGENDA  |  {matkul} Kelas {kelas}")
        print()
        print("  [1]  Tambah Agenda")
        print("  [2]  Lihat Semua Agenda")
        print("  [3]  Hapus Agenda")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            clear()
            header("TAMBAH AGENDA")
            acara      = input("\n  Nama Acara    : ").strip()
            tanggal    = input("  Tanggal       : ").strip()
            waktu      = input("  Waktu         : ").strip()
            keterangan = input("  Keterangan    : ").strip()
            if not acara:
                print("  [!] Nama acara tidak boleh kosong!"); kembali(); continue

            jid = store["jadwal_counter"]
            store["jadwal"].append({
                "id": jid, "acara": acara,
                "tanggal": tanggal, "waktu": waktu,
                "keterangan": keterangan,
            })
            store["jadwal_counter"] += 1
            print(f"\n  ✅ Agenda '{acara}' berhasil ditambahkan!")
            kembali()

        elif pilih == "2":
            clear()
            header("DAFTAR AGENDA")
            if not store["jadwal"]:
                print("\n  Belum ada agenda."); kembali(); continue
            for j in store["jadwal"]:
                print(f"\n  📅 #{j['id']}  {j['acara']}")
                print(f"       {j['tanggal']}  {j['waktu']}")
                if j["keterangan"]:
                    print(f"       📝 {j['keterangan']}")
            kembali()

        elif pilih == "3":
            clear()
            header("HAPUS AGENDA")
            if not store["jadwal"]:
                print("\n  Belum ada agenda."); kembali(); continue
            for j in store["jadwal"]:
                print(f"  [{j['id']}] {j['acara']}  —  {j['tanggal']}")
            print()
            try:
                jid = int(input("  Masukkan ID yang dihapus: "))
                sebelum = len(store["jadwal"])
                store["jadwal"] = [j for j in store["jadwal"] if j["id"] != jid]
                if len(store["jadwal"]) < sebelum:
                    print(f"  ✅ Agenda #{jid} dihapus!")
                else:
                    print("  [!] ID tidak ditemukan.")
            except ValueError:
                print("  [!] Input harus angka.")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  8. KELOLA MAHASISWA
# ══════════════════════════════════════════════════════════════════════════════

def kelola_mahasiswa(store):
    while True:
        clear()
        header("KELOLA DAFTAR MAHASISWA")
        print()
        print("  [1]  Lihat Daftar Mahasiswa")
        print("  [2]  Tambah Mahasiswa")
        print("  [3]  Hapus Mahasiswa")
        print("  [0]  Kembali")
        print()
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            clear()
            header("DAFTAR MAHASISWA")
            print()
            for i, m in enumerate(store["mahasiswa"], 1):
                print(f"  {i:>3}. {m}")
            print(f"\n  Total: {len(store['mahasiswa'])} mahasiswa")
            kembali()

        elif pilih == "2":
            nama = input("\n  Nama mahasiswa baru: ").strip()
            if nama and nama not in store["mahasiswa"]:
                store["mahasiswa"].append(nama)
                print(f"  ✅ '{nama}' berhasil ditambahkan!")
            elif nama in store["mahasiswa"]:
                print("  [!] Nama sudah ada di daftar.")
            else:
                print("  [!] Nama tidak boleh kosong.")
            kembali()

        elif pilih == "3":
            clear()
            header("HAPUS MAHASISWA")
            for i, m in enumerate(store["mahasiswa"], 1):
                print(f"  [{i}] {m}")
            print()
            try:
                idx = int(input("  Nomor yang dihapus: ")) - 1
                if 0 <= idx < len(store["mahasiswa"]):
                    hapus = store["mahasiswa"].pop(idx)
                    print(f"  ✅ '{hapus}' berhasil dihapus!")
                else:
                    print("  [!] Nomor tidak valid.")
            except ValueError:
                print("  [!] Input harus angka.")
            kembali()

        elif pilih == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    while True:
        nama_pj, matkul, kelas = login()
        menu(nama_pj, matkul, kelas)
        ulang = input("\n  Login lagi? (y/n): ").strip().lower()
        if ulang != "y":
            print("\n  Keluar dari sistem. Goodbye! 👋\n")
            break