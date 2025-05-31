# sebagai client
#  nama berkas : praktikum 1.py
# TCP Server untuk client praktikum 1_server.py
import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 12345))
print('Mesin penjawab otomatis sudah siap')
while pesan.lower() != 'z':
    pesan = input('Pertanyaan: ')
    pesan = pesan.encode()
    s.send(pesan)
    if pesan.lower() != 'z':
        response = s.recv(1024)
        response = response.decode()
        print('Jawaban:', response)
s.close