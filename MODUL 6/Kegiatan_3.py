nama = input("Masukkan nama saudara: ")
waktu_sekarang = float(input("Pukul berapa sekarang?: "))

# Menentukan waktu berdasarkan rentang jam
if 4 <= waktu_sekarang < 11:
    waktu = "pagi"
elif 11 <= waktu_sekarang < 15:
    waktu = "siang"
elif 15 <= waktu_sekarang < 18:
    waktu = "sore"
else:
    waktu = "malam"

print("Selamat " + waktu + " " + nama)