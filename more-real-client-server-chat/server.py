import socket
import threading

HOST = '0.0.0.0'
PORT = 21002

clients = []  # List to keep track of connected clients

class Client:
    def __init__(self, username, socket, address):
        self.socket = socket
        self.username = username
        self.address = address

def handle_client(client): # Client type
    print(f"Client connected: {client.address}")
    client.socket.send("Welcome to the chat server! Type 'exit' to leave.\n".encode())
    
    while True:
        try:
            message_received = ""
            while True:
                data = client.socket.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("Connection lost!")
                    break

            if message_received.strip().lower() == "exit":
                print(f"Client {client.address} disconnected.")
                client.socket.send("Goodbye!\n".encode())
                break
            
            broadcast(f"Client {client.username.decode()}: {message_received}", client)
        except (ConnectionResetError, BrokenPipeError):
            print(f"Client {client.address} unexpectedly disconnected.")
            break

    # Remove client from the list and close the connection
    clients.remove(client)
    client.socket.close()


def broadcast(message, sender=None):
    for client in clients:
        # print(type(client)) # socket.socket
        print(client == sender)
        if client != sender:  # Don't send the message to the sender
            try:
                client.socket.send(f"{message}\n".encode())
            except:
                print("Error in broadcasting.")
                pass  # Ignore errors when sending to a disconnected client


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started and listening on {HOST}:{PORT}")

        while True: # accpet-clients
            conn, addr = server_socket.accept()
            username = conn.recv(1024) # receive username from client
            new_client = Client(username=username, socket=conn, address=addr)
            print(new_client.username, new_client.address)

            clients.append(new_client)
            thread = threading.Thread(target=handle_client, args=(new_client,))
            thread.start()


if __name__ == "__main__":
    start_server()
