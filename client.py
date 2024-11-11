import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

print("Conectado ao chatbot. Digite uma pergunta ou 'Sair' para encerrar.")
while True:
    message = input("Você: ")
    
    client_socket.send(message.encode())
    
    data = client_socket.recv(1024).decode()
    print(f"Bot: {data}")
    
    if message == "Sair":
        break

client_socket.close()