import socket
import threading

HOST = '0.0.0.0'
PORT = 21002

clients = []  # List to keep track of connected clients

class Client:
    def __init__(self, socket, username):
        self.socket = socket
        self.username = username

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    conn.send("Welcome to the chat server! Type 'exit' to leave.\n".encode())
    
    while True:
        try:
            message_received = ""
            while True:
                data = conn.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("Connection lost!")
                    break

            if message_received.strip().lower() == "exit":
                print(f"Client {addr} disconnected.")
                conn.send("Goodbye!\n".encode())
                break
            
            broadcast(f"Client {addr}: {message_received}", conn)
        except (ConnectionResetError, BrokenPipeError):
            print(f"Client {addr} unexpectedly disconnected.")
            break

    # Remove client from the list and close the connection
    clients.remove(conn)
    conn.close()


def broadcast(message, sender_conn=None):
    for client in clients:
        # print(type(client)) # socket.socket
        if client != sender_conn:  # Don't send the message to the sender
            try:
                client.send(f"{message}\n".encode())
            except:
                pass  # Ignore errors when sending to a disconnected client


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started and listening on {HOST}:{PORT}")

        while True: # accpet-clients
            conn, addr = server_socket.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    start_server()
