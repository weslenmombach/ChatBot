import socket

responses = {
    "Tudo bem?": "Sim, tudo ótimo!",
    "Quais filmes estão em cartaz?": "Hoje, está em cartaz o filme da Patrulha Canina.",
    "Quanto custa o Aerolin?": "O Aerolin custa R$29,00.",
    "Sair": "Obrigado por utilizar nosso sistema!"
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("Servidor de chatbot iniciado. Aguardando conexão...")

connection, address = server_socket.accept()
print(f"Conexão estabelecida com {address}")

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    
    response = responses.get(data, "Desculpe, não entendi sua pergunta. Pode reformular?")
    print(f"Cliente: {data}")
    print(f"Bot: {response}")
    
    connection.send(response.encode())
    
    if data == "Sair":
        break

connection.close()
server_socket.close()