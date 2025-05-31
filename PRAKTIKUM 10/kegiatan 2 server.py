# sebagai server
import socket
import platform


COMMANDS = {
    "machine": platform.machine,
    "release": platform.release,
    "system": platform.system,
    "version": platform.version,
    "node": platform.node,
}

HOST = 'localhost'
PORT = 2004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server berjalan di {HOST}:{PORT}")
print("Menunggu koneksi dari client...")

client_socket, client_address = server.accept()
print(f"Koneksi diterima dari {client_address}")

while True:
    
    perintah = client_socket.recv(1024).decode().lower()
    print(f"Perintah diterima: {perintah}")

    if perintah in COMMANDS:
        
        response = COMMANDS[perintah]()
    elif perintah == "quit":
    
        response = "Sesi berakhir, terima kasih!"
        client_socket.send(response.encode())
        break
    else:

        response = "Perintah tidak dikenal."

    client_socket.send(response.encode())

client_socket.close()
server.close()
print("Server ditutup.")

