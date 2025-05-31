list = ["Nim : L200240054 \n","Tanggal_lahir : 20/04/2006 \n","Nama : Erbita Putri Apriliyana \n"]
file = open("L200240054","r")
all_lines = file.readlines()
print(all_lines[2])
print(all_lines[3], end=", ")
print(all_lines[1])
print(all_lines[0])
file.close()

