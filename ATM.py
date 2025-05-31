#Program untuk membuat ATM sederhana
pin_ATM = "4002" #pin untuk mengakses ATM
Saldo = 1000000 #saldo awal
def verifikasi_pin(pin): #digunakan untuk memverifikasi pin
    input_pin = input("Masukkan pin ATM Anda : ") #digunakan untuk memasukkan pin
    if input_pin == pin_ATM: #kode ini berarti jika input pin sama dengan pin ATM maka akan bernilai true/ benar
        return True
    else:
        print("Kode PIN salah. Silahkan coba lagi.") #jika salah maka akan menampilkan kata ini dan bernilai false
        return False                                #yang artinya pengguna harus memasukkan pin kembali
def menu(): #baris 11-16 digunakan untuk membuat menu pilihan yang nantinya akan digunakan dalam program selanjutnya
    print("Silahkan pilih menu dibawah ini :")
    print("1. Cek saldo")
    print("2. Tarik tunai")
    print("3. Setor tunai")
    print("4. keluar")

print("Selamat Datang di ATM.") #mencetak kata "Selamat Datang di ATM."

if verifikasi_pin(pin_ATM): #digunakan untuk memverifikasi pin jika bernilai true maka akan menjalankan program selanjutnya
    while True: # digunakan untuk membuat perulangan
        menu() #digunakan untuk memanggil menu
        pilihan = int(input("Masukkan pilihan Anda :")) #digunakan untuk memasukkan pilihan yang bernilai integer

        if pilihan == 1: #digunakan untuk menampilkan saldo
            print("Saldo Anda berjumlah Rp.", Saldo)
        elif pilihan == 2: #digunakan untuk tarik tunai
            Tarik_tunai = int(input("Masukkan jumlah uang yang ingin Anda tarik :Rp."))
            if Tarik_tunai > Saldo : #digunakan untuk mengecek apakah jumlah tarik tunai lebih besar dari saldo
                print("Maaf, saldo Anda tidak cukup.") #jika lebih besar maka akan menampilkan kata ini
            elif Tarik_tunai <= Saldo: #digunakan untuk mengecek apakah tarik tunai kurang dari atau sama dengan saldo
                Sisa_saldo = Saldo - Tarik_tunai #fungsi operasi untuk menghitung sisa saldo
                print("Tarik tunai berhasil, Saldo anda saat ini Rp.", Sisa_saldo)
        elif pilihan == 3: #digunakan untuk setor tunai
            Setor_tunai = int(input("Masukkan jumlah uang yang ingin Anda setor :Rp.")) #digunakan untuk memasukkan setor tunai
            if Setor_tunai % 50000 != 0: #digunakan untuk mengecek apakah jumlah setor tunai hanya kelipatan 50000
                print("Maaf, jumlah setor tunai hanya bisa kelipatan Rp. 50.000") #jika tidak maka akan menampilkan kata ini
            else:
                Setor_saldo = Saldo + Setor_tunai #fungsi operasi untuk menghitung setor tunai
                print("Setor tunai berhasil!, Saldo anda saat ini Rp.", Setor_saldo) #jika benar maka akan menampilkan kata ini dan menampilkan 
                #jumlah saldo terakhir setelah ditambahkan
        elif pilihan == 4: #digunakan untuk keluar dari program
            print("Terima kasih telah menggunakan layanan ATM kami.") #jika benar akan menampilkan kata ini sbg tanda berakhirnya program
            break