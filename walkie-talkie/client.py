# Client side
import socket

HOST = '127.0.0.1'
PORT = 21002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message = input("Me: ")
        if message == "exit":
            s.send(("exit\n").encode())
            print("Exiting the chat...")
            break

        s.send((message + "\n").encode())

        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                message_received += data.decode()
                if message_received == "exit\n":
                    print("Host user requested to exit. Closing connection.")
                    break
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break

        if message_received == "exit\n":
            break

        if message_received:
            print("Host user:", message_received)

print("Client finished")
