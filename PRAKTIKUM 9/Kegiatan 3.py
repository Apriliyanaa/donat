#Menyimpan data dari berkas teks dan menyimpan ke shelve
import shelve
F = shelve.open("L200240054.data") #untuk membuka berkas yang dibuat
F["daftar"] = ['Nim :',
               'Tanggal_lahir :',
               'Nama :'] #menyimpan data
F["hasil"] = ('L200240054',
              '20-04-2006',
              'Erbita Putri Apriliyana')
F.close() #menutup berkas

F = shelve.open("L200240054.data") #membuka berkas
print("daftar:", F["daftar"]) #untuk membaca data daftar
print("hasil:", F["hasil"]) #membaca data hasil
print(F["daftar"][0], end=" ")
print(F["hasil"][0])
print(F["daftar"][1], end=" ")
print(F["hasil"][1])
print(F["daftar"][2], end=" ")
print(F["hasil"][2])
F.close()