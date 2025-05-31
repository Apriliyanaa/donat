# sebagai server
# nama berkas : praktikum 1_server.py
# TCP Server untuk client praktikum 1_server.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 12345))
s.listen(1)
print("server siap menjawab pertanyaan")

data = ''
biodata = {'Nama':'Erbita Putri Apriliyana',
            'NIM' : 'L200240054',
            'Angkatan' : '2024'}
while data.lower() != 'z' :
    komm, addr = s.accept()
    while data.lower() != 'z' :
        data = komm.recv(1024)
        data = data.decode()
        if data.lower() == 'z':
            s.close()
            break
        print ('Pertanyaan:'), data
        if data in biodata :
            komm.send(biodata[data].encode())
        else :
            komm.send('Maaf, perintah tidak dimengerti')

        



