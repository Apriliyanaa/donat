import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(('localhost', 1100))
print("Terhubung ke server. Masukkan panjang, lebar, dan tinggi dipisahkan dengan koma (contoh: 10,5,4):")

while True:
    data = input(">> ")
    if data.lower() == "keluar":
        print("Keluar dari sesi.")
        break

    client.send(data.encode())

    response = client.recv(1024).decode()
    print(f"Server: {response}")

client.close()