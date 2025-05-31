#Tugas PBO
class Manusia:
    def __init__(self, Nama, Warna_rambut, Kecepatan_berlari, gender, ):
        self.Nama = Nama
        self.Warna_rambut = Warna_rambut
        self.Kecepatan_berlari = Kecepatan_berlari
        self.gender = gender

    def berjalan(self): #membuat method
        print("Bisa berjalan")
    def berlari(self):  #membuat method
        print("Bisa berlari")
    def membaca(self): #membuat method
        print("Bisa membaca")
#instansiasi object manusia
Putri = Manusia("Putri", "Hitam", "25 km/jam", "Perempuan")
Adam = Manusia("Adam", "Blonde", "30 km/jam", "Laki-laki")
Hawa = Manusia("Hawa", "Putih", "20 km/jam", "Perempuan")
#memanggil method yang telah dibuat
Putri.berjalan()
Putri.berlari()
Putri.membaca()
Adam.berjalan()
Adam.berlari()
Adam.membaca()
Hawa.berjalan()
Hawa.berlari()
Hawa.membaca()
#memanggil atribut orang
print("Nama:", Putri.Nama)
print("Warna rambut:", Putri.Warna_rambut)
print("Kecepatan berlari:", Putri.Kecepatan_berlari)
print("Gender:", Putri.gender)
print("Nama:", Adam.Nama)
print("Warna rambut:", Adam.Warna_rambut)
print("Kecepatan berlari:", Adam.Kecepatan_berlari)
print("Gender:", Adam.gender)
print("Nama:", Hawa.Nama)
print("Warna rambut:", Hawa.Warna_rambut)
print("Kecepatan berlari:", Hawa.Kecepatan_berlari)
print("Gender:", Hawa.gender)
