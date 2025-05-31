bangun_datar = {
    1: ("Segitiga", "L = 0.5*a*t"),
    2: ("Persegi", "L= s**2"),
    3: ("Persegi Panjang", "L = p * l"),
    4: ("Lingkaran", "L = pi * r ** 2"),
    5: ("Jajar Genjang", "L = a * t")
}

print("No  |Nama Bangun      |Rumus Luas ")
print("----|-----------------|-----------------")
for no, (bangun, rumus) in bangun_datar.items():
    print(f"{no:<4}|{bangun:<17}|{rumus}")