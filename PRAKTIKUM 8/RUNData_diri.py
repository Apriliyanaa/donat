import data_diri
#Fungsi yang menampilkan menu
def tampilkan_menu():
    print("Pilihan yang tersedia:")
    print("x: menampilkan bantuan ini")
    print("a: menampilkan Nama")
    print("b: menampilkan Fakultas")
    print("c: menampilkan Gender")
    print("d: menampilkan Status")
    print("e: menampilkan Kewarganegaraan")
    print("f: menampilkan Agama")
    print("g: menampilkan Alamat")

#ketika bernilai benar
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan : ")

    if pilihan == 'a':
        data_diri.tampilkan_nama()
    elif pilihan == 'b':
        data_diri.tampilkan_fakultas()
    elif pilihan == 'c':
        data_diri.tampilkan_gender()
    elif pilihan == 'd':
        data_diri.tampilkan_status()
    elif pilihan == 'e':
        data_diri.tampilkan_kewarganegaraan()
    elif pilihan == 'f':
        data_diri.tampilkan_agama()
    elif pilihan == 'g':
        data_diri.tampilkan_alamat()
    else:
        print("Perintah tidak dikenal")