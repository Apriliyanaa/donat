import socket


def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1100))  
server.listen(5)
print("Server sedang berjalan, menunggu koneksi...")

while True:
    conn, addr = server.accept()
    print(f"Koneksi diterima dari {addr}")

    data = conn.recv(1024).decode()
    if not data:
        break

    try:
        panjang, lebar, tinggi = map(float, data.split(","))
        volume = hitung_volume_balok(panjang, lebar, tinggi)
        conn.send(f"Volume balok adalah: {volume}".encode())
    except ValueError:
        conn.send("Input tidak valid, masukkan tiga angka dipisahkan dengan koma.".encode())
    
    conn.close()