#kode program untuk membuat tahun kabisat dan tidak tahun kabisat
print("PROGRAM MENENTUKAN TAHUN KABISAT DAN BUKAN TAHUN KABISAT")#menampilkan kalimat ini
print("Selamat Datang di program ini!") #menampilkan kalimat ini
def kabisat(n): #digunakan untuk menentukan tahun kabisat
    if n % 400 == 0: #digunakan untuk mengecek apakah tahun kabisat jika bisa dibagi 400
        return True #jika bisa dibagi 400 maka tahun kabisat akan bernilai true
    if n % 100 == 0: #digunakan untuk mengecek apakah tahun kabisat jika bisa dibagi 100
        return False #jika bisa dibagi 100 maka tahun kabisat akan bernilai false
    if n %  4 == 0: #digunakan untuk mengecek apakah tahun kabisat jika bisa dibagi 4
        return True #jika bisa dibagi 4 maka tahun kabisat akan bernilai true
    else:
        return False #jika tidak memenuhi syarat 3 diatas maka tahun kabisat akan bernilai false
while True: #digunakan untuk membuat perulangan memasukkan tahun
    Tahun = input("Masukkan Tahun :") #digunakan untuk memasukkan tahun
    if Tahun.lower() == "keluar": #digunakan untuk keluar dari program apabila saya memasukkan kata keluar
        print("Anda telah keluar dari program. Terima kasih!") #program akan menampilkan kata ini
        break #setelah itu program akan berhenti
    Tahun = int(Tahun) #digunakan untuk memasukkan tahun yang bernilai integer
    if kabisat(Tahun): #digunakan untuk mengecek apakah tahun kabisat
        print(Tahun ,"adalah tahun kabisat") #jika benar tahun kabisat maka akan menampilkan kata ini
    if not kabisat(Tahun): #digunakan untuk mengecek apakah tahun kabisat
        print(Tahun, "bukan tahun kabisat") #jika bukan tahun kabisat maka akan menampilkan kata ini