import socket

'''
Client side!

'''

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #client socket! tcp stream socket, byte-oriented
client_socket.connect(('localhost', 10000)) #establish connection to the server
role = client_socket.recv(1024) #receive role
print(role.decode())

if role == b"You have been assigned the advisee role!": #the servers has decided advisee role
    message = input("What is your question? ") #advice
    client_socket.send(message.encode())
    response = client_socket.recv(1024) #w8 for response
    print(f"The advice: {response.decode()}")

elif role == b"You have been given the responsibility of the advisor role! Be cautious when offering advice.": #hardcoded message received, so the clients know what role it is assigned from the server
    question = client_socket.recv(1024).decode()  #Receiv the echoed question
    print(f"Received question: {question}")
    message = input("What is your advice for this? ")
    client_socket.send(message.encode())
client_socket.close() #finished communicating

