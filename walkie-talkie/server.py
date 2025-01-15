# Server side
import socket

HOST = '0.0.0.0'
PORT = 21002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print(f"Error binding/listening: {msg}")
    s.close()
    exit(1)

conn, addr = s.accept()
with conn:
    print('Connection accepted from', addr)

    while True:
        message_received = ""
        while True:
            data = conn.recv(32)
            if data:
                message_received += data.decode()
                if message_received == "exit\n":
                    print("Joined user requested to exit. Closing connection.")
                    break
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break

        if message_received == "exit\n":
            break

        if message_received:
            print("Joined user:", message_received)
            message = input("Me: ")
            if message == "exit":
                conn.send(("exit\n").encode())
                print("Exiting the chat...")
                break

            conn.send((message + "\n").encode())

print("Server finished")
s.close()
