from tkinter import Tk, Label, Entry, Button, StringVar#digunakan untuk mengimpor modul tkinter

# Membuat jendela kalkulator
kalkulator = Tk()
kalkulator.title("Kalkulator") #digunakan untuk membuat judul pada aplikasi utama

# Label dan entry untuk angka pertama
L1 = Label(kalkulator, text="Angka 1") #digunakan untuk membuat label dengan teks angka 1
L1.grid(row=0, column=0) #digunakan untuk mengatur posisi label diatas
angka1 = StringVar() #digunakan untuk menyimpan angka
E1 = Entry(kalkulator, textvariable=angka1) #digunakan untuk memasukkan angka
E1.grid(row=0, column=1, columnspan=3) #digunakan untuk mengatur posisi entry

# Label dan entry untuk angka kedua
L2 = Label(kalkulator, text="Angka 2") #digunakan untuk membuat label dengan teks angka 
L2.grid(row=1, column=0)#digunakan untuk mengatur posisi label diatas
angka2 = StringVar()#digunakan untuk menyimpan angka
E2 = Entry(kalkulator, textvariable=angka2)#digunakan untuk memasukkan angka
E2.grid(row=1, column=1, columnspan=3)#digunakan untuk mengatur posisi entry

# Fungsi untuk operasi penjumlahan
def tambah(): #kode baris 22-26 digunakan untuk membuat fungsi tambah
    a = float(angka1.get()) #menyimpan data dengan type float
    b = float(angka2.get()) #menyimpan data dengan type float
    hasil = a + b #operasi penjumlahan
    L.config(text=hasil) #mengatur posisi label hasil yang digunakan untuk menampilkan hasil penjumlahan

# Tombol penjumlahan
B1 = Button(kalkulator, text="+", command=tambah)
B1.grid(row=2, column=0)

# Fungsi untuk operasi pengurangan
def kurang():#kode baris 33-38 digunakan untuk membuat fungsi kurang
    a = float(angka1.get()) #menyimpan data dengan type float
    b = float(angka2.get())  #menyimpan data dengan type float
    L.config(text=hasil)
    hasil = a - b #operasi pengurangan
    L.config(text=hasil) #mengatur posisi label hasil yang digunakan untuk menampilkan hasil pengurangan

# Tombol pengurangan
B1 = Button(kalkulator, text="-", command=kurang) #digunakan untuk membuat tombol pengurangan
B1.grid(row=2, column=1) #digunakan untuk mengatur posisi tombol pengurangan

# Fungsi untuk operasi perkalian
def kali(): #kode baris 45-49 digunakan untuk membuat fungsi perkalian
    a = float(angka1.get()) #menyimpan data dengan type float
    b = float(angka2.get())#menyimpan data dengan type float
    hasil = a * b #operasi perkalian
    L.config(text=hasil) #mengatur posisi label hasil yang digunakan untuk menampilkan hasil perkalian

# Tombol perkalian
B1 = Button(kalkulator, text="x", command=kali) #digunakan untuk membuat tombol perkalian
B1.grid(row=2, column=2) #digunakan untuk mengatur posisi tombol perkalian

# Fungsi untuk operasi pembagian
def bagi():#kode baris 56-60 digunakan untuk membuat fungsi pembagian
    a = float(angka1.get())#menyimpan data dengan type float
    b = float(angka2.get())#menyimpan data dengan type float
    hasil = a / b#operasi pembagian
    hasil = a * b #operasi perkalian
    L.config(text=hasil)#mengatur posisi label hasil yang digunakan untuk menampilkan hasil pembagian

# Tombol pembagian
B1 = Button(kalkulator, text=":", command=bagi)#digunakan untuk membuat tombol pembagian
B1.grid(row=2, column=3)#digunakan untuk mengatur posisi tombol pembagian

# Label untuk menampilkan hasil
L = Label(kalkulator, text="Hasil") #digunakan untuk membuat label dengan teks hasil
L.grid(row=3, column=0, columnspan=4) #digunakan untuk mengaur posisi label diatas

kalkulator.mainloop() #digunakan untuk menjalankan aplikasi kalkulator