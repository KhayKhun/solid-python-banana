import socket
import threading

HOST = '127.0.0.1'
PORT = 21002


def receive_messages(sock):
    while True:
        try:
            message_received = ""
            while True:
                data = sock.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    break

            if message_received:
                print(message_received)
            else:
                print("Disconnected from the server.")
                break
        except:
            print("Connection to server lost.")
            break

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        valid_name = False
        client_socket.connect((HOST, PORT))
        print("Connected to the chat server.")
        while not valid_name:
            n = input("Enter your username: ").strip()
            if n:
                break

        client_socket.send(n.encode()) # send username to server

        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.start()

        while True:
            message = input("You: ")
            if message.lower() == "exit":
                client_socket.send("exit\n".encode())
                print("Exiting the chat.")
                break
            client_socket.send((message + "\n").encode())


if __name__ == "__main__":
    start_client()
