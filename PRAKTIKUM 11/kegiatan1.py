import tkinter as tk #digunakan untuk mengimpor modul tkinter

# Membuat jendela utama (judul)
window = tk.Tk()
window.title("Data Diri") #digunakan untuk membuat judul pada aplikasi utama

# membuat label-label
nama_label = tk.Label(window, text="Nama", font=("Arial", 12))
nama_value = tk.Label(window, text="Erbita Putri Apriliyana", font=("Arial", 12))
nim_label = tk.Label(window, text="NIM", font=("Arial", 12))
nim_value = tk.Label(window, text="L200240054", font=("Arial", 12))
buku_label = tk.Label(window, text="Buku favorit", font=("Arial", 12))
buku_value = tk.Label(window, text="Atomic Habit", font=("Arial", 12))
idola_label = tk.Label(window, text="Idola di kalangan sahabat", font=("Arial", 12))
idola_value = tk.Label(window, text="Umar bin Khattab", font=("Arial", 12))
motto_label = tk.Label(window, text="Motto", font=("Arial", 12))
motto_value = tk.Label(window, text="Jangan menunda-nunda pekerjaan jika ingin sukses", font=("Arial", 12))

# Buat tombol tutup
def tutup_aplikasi():
    window.quit()

tutup_button = tk.Button(window, text="Tutup", command=tutup_aplikasi)

# membuat pengaturan layout ( menggunakan grid)
nama_label.grid(row=0, column=0) #baris kode 26-36 digunakan untuk mengatur posisi label dan value kode 8-17
nama_value.grid(row=0, column=1) 
nim_label.grid(row=1, column=0)
nim_value.grid(row=1, column=1)
buku_label.grid(row=2, column=0)
buku_value.grid(row=2, column=1)
idola_label.grid(row=3, column=0)
idola_value.grid(row=3, column=1)
motto_label.grid(row=4, column=0)
motto_value.grid(row=4, column=1)
tutup_button.grid(row=5, column=1)

# Menjalankan aplikasi
window.mainloop() 