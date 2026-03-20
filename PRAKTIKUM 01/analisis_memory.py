import sys

def cek_memori():
    data = []
    print(f"{'Jumlah Item':<12} | {'Ukuran Memori (Bytes)':<20}")
    print("-" * 35)
    
    for i in range(20):
        n = len(data)
        b = sys.getsizeof(data)
        print(f"{n:<12} | {b:<20}")
        data.append(i)

if __name__ == "__main__":
    cek_memori()
#memori bertambah hanya ketika jumlah anggota list mencapai kapasitas tertentu, analogi seperti kursi warteg yang sudaah disiapkan untuk 4 orang, ketika ada pelanggan ke 5 datang, maka warteg harus menambah kursi baru. Begitu juga dengan list di Python, ketika jumlah anggota mencapai kapasitas tertentu, Python akan membuat list baru dengan kapasitas yang lebih besar dan menyalin data lama ke list baru tersebut.