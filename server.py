import socket

HOST = 'daring.cwl.nl'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, Taw Thar')
    data = s.recv(1024)


print('Reveived', repr(data))