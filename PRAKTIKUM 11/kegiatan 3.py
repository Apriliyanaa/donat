from tkinter import Tk, Label, Entry, Button, StringVar
# Membuat jendela utama aplikasi
app = Tk()
app.title("Bangun Geometri") #digunakan untuk mengatur judul pada aplikasi utama

# Membuat label judul
judul = Label(app, text="Bangun Geometri Luas Persegi", font=("Arial", 24)) #untuk mengatur font serta ukurannya
judul.grid(row=0, sticky="w") #mengatur posisi judul label

# Membuat label deskripsi
deskripsi = Label(app, text="Bangun geometri persegi memiliki rumus luas =sisi x sisi.")
#membuat label dengan kalimat deskripsi tentang bangun geometri
deskripsi.grid(row=2, sticky="w") #mengatur posisi label deskripsi tentang bangun geometri.

# Label dan entry untuk sisi 1
label_parameter1 = Label(app, text="Parameter 1:") #membuat label dengan teks alas agar nantinya bisa dimasukan angka
label_parameter1.grid(row=3, sticky="w") #digunakan untuk mengatur posisi label diatas
parameter_1 = StringVar() #digunakan untuk menyimpan angka
entry_sisi = Entry(app, textvariable=parameter_1) #kode ini digunakan untuk memasukkan angka
entry_sisi.grid(row=3, column=1) #digunakan untuk mengatur posisi entry

# Label dan entry untuk sisi 2
label_parameter2 = Label(app, text="Parameter 2:") ##membuat label dengan teks alas agar nantinya bisa dimasukan angka
label_parameter2.grid(row=4, sticky="w") #digunakan untuk mengatur posisi label diatas
parameter_2 = StringVar() #digunakan untuk menyimpan angka
entry_parameter2 = Entry(app, textvariable=parameter_2) #kode ini digunakan untuk memasukkan angka
entry_parameter2.grid(row=4, column=1) #digunakan untuk mengatur posisi entry

# Fungsi untuk menghitung luas segitiga
def luas_persegi():
    a = int(parameter_1.get())
    b = int(parameter_2.get())
    hasil = (a * b)
    label_hasil.config(text=hasil)

# Tombol untuk menghitung luas
hitung_luas = Button(app, text="Hitung Luas", command=luas_persegi) #digunakan untuk membuat tombol hitung luas
hitung_luas.grid(row=5, column=0) #mengatur posisi tombol hitung luas

# Label untuk menampilkan hasil
label_hasil = Label(app, text="Luas = ") #digunakan untuk membuat label untuk menampilkan hasil perhitungan
label_hasil.grid(row=6, sticky="w") #digunakan untuk mengatur posisi label hasil

app.mainloop() #digunakan untuk menjalankan aplikasi