import socket
import threading

def clientManager(connection, address, role, clients):
    connection.send(role)
    while True:
        message = connection.recv(1024)
        if not message:
            break

        # Forward message to the other role's client
        other_role = b"You have been assigned the advisee role!" if role == b"You have been given the responsibility of the advisor role! Be cautious when offering advice." else b"You have been given the responsibility of the advisor role! Be cautious when offering advice."
        if other_role in clients:
            clients[other_role].send(message)

    connection.close()
    del clients[role]

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 10000))
    server_socket.listen()

    connections = 0
    clients = {}  # Dictionary to store clients and their roles

    while True:
        connection, address = server_socket.accept()
        print(f"{address} connecte!")
        role = b"You have been assigned the advisee role!" if connections % 2 == 0 else b"You have been given the responsibility of the advisor role! Be cautious when offering advice."
        clients[role] = connection
        client_thread = threading.Thread(target=clientManager, args=(connection, address, role, clients))
        client_thread.start()
        connections += 1

if __name__ == '__main__':
    main()
