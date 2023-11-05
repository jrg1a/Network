import socket
from cryptography.fernet import Fernet

key = b'YOUR_GENERATED_KEY_FROM_SERVER'  # Use the key printed by the server here
cipher = Fernet(key)

server = ('127.0.0.1', 9999)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server)

while True:
    cmd = input("Enter command: ")
    if not cmd:
        continue
    
    encrypted_cmd = cipher.encrypt(cmd.encode())
    client.send(encrypted_cmd)
    
    encrypted_output = client.recv(2048)
    output = cipher.decrypt(encrypted_output).decode('utf-8')
    print(output)
    
    if cmd == "exit":
        break

client.close()
