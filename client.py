import socket
import json

HOST = '127.0.0.1'
PORT = 21001 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    s.sendall(b'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n')
    
    data = s.recv(1024)
    print('Raw data received:', data)

    # Decode the bytes to a string and parse the JSON
    json_response = json.loads(data.decode('utf-8'))
    print('Parsed JSON:', json_response)

    # Access specific parts of the JSON
    print('Message:', json_response["message"])
    print('Data value1:', json_response["data"]["value1"])
