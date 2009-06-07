# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = raw_input("Digite o comando a enviar: ")

    if data == 'Q':
        break		

    s.send(data)

s.close()

