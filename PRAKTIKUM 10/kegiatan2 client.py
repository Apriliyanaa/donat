#sebagai client
import socket

HOST = 'localhost'
PORT = 2004

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Terhubung ke server.")
print("Masukkan perintah (machine, release, system, version, node, quit):")

while True:
    
    perintah = input(">> ").lower()

  
    client.send(perintah.encode())

    
    response = client.recv(1024).decode()
    print(f"Respons: {response}")

    if perintah == "quit":
        print("Keluar dari sesi.")
        break

client.close()