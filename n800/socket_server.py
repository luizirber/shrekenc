#Echo server program
import socket
import robot

import time

HOST = '' 
PORT = 50007 

commands = ['F', 'R', 'L']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()

while 1:
    data = conn.recv(1024)

    if not data: 
        time.sleep(1)

    print data 
    #if data in commands:	
    #    robot.move(data)

conn.close()

