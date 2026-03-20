import time
import random

# Membuat dataset 1 juta data
N = 1_000_000
data_list = list(range(N))
data_dict = {i: f"Value {i}" for i in range(N)}

target = N - 1 # Target di posisi paling akhir

# Benchmark List (O(n))
start_list = time.perf_counter()
target in data_list
end_list = time.perf_counter()

# Benchmark Dictionary (O(1))
start_dict = time.perf_counter()
target in data_dict
end_dict = time.perf_counter()

print(f"Waktu List (O(n))      : {end_list - start_list:.8f} detik")
print(f"Waktu Dictionary (O(1)): {end_dict - start_dict:.8f} detik")
print(f"Kesimpulan: Dictionary jauh lebih cepat untuk pencarian data besar!")
