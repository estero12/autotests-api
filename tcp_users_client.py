import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost",12345))

message = "Привет, сервер!"

client.send(message.encode())

response = client.recv(1024).decode()

print(f'Ответ от сервера: {response}')

client.close()