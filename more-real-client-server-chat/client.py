import socket
import threading

HOST = '127.0.0.1'
PORT = 21002


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                print("Disconnected from the server.")
                break
            print(message)
        except:
            print("Connection to server lost.")
            break


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to the chat server.")

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
