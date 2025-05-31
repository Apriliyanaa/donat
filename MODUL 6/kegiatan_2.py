password = "Erbita"
akses = 0

while akses < 3:
    inputan = input("Masukkan password: ")
    if inputan == password:
        print("Anda berhasil login")
        break  # Keluar dari perulangan jika password benar
    else:
        print("Maaf, anda salah memasukkan password.")
        akses += 1

if akses == 3:
    print("Anda telah mencoba 3 kali. Akses anda ditolak.")