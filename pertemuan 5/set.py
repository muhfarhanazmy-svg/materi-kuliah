# cara inisiasi set
# cara pertama
# 1 (kurung kurawal)
import sys
tokenWord = {"tidak", "bisa"}
print(tokenWord)
print(type(tokenWord))
print("ukuran memori set: ", sys.getsizeof(tokenWord))

# cara kedua
# 2 (set())

kataSambung = set(["kemudian", "lalu", "setelah"])
print(kataSambung)
print(type(kataSambung))
print("ukuran memori set: ", sys.getsizeof(kataSambung))

#pembuktian terkait tidak memiliki sistem indexing
#print(kataSambung[-1])

#Menghapus elemen pada set
kataSambung.remove("kemudian")
print(kataSambung)
tokenWord.discard("tidak")
print(tokenWord)

#menambahkan elemen pada set
tokenWord.add("bisa")
print(tokenWord)
tokenWord.update(["tidak", "bisa"])
print(tokenWord)

#mengubaha elemen pada set
tokenWord.remove("tidak")
print(tokenWord)
tokenWord.add("nanti ajah")
print(tokenWord)

#operasi pada set
setA ={1, 2, 3, 4}
setB = {3, 4, 5, 6}

#union
print(setA | setB)
#intersection
print(setA & setB)
#difference
print(setA - setB)
#symmetric difference
print(setA ^ setB)