import socket

def server():
    messages = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("localhost",12345))

    server_socket.listen(10)
    print("Сервер запущен")

    while True:
        con,addr = server_socket.accept()
        print(f'Пользователь с адресом: {addr} подключился к серверу')

        message = con.recv(1024).decode()
        print(f'Пользователь с адресом: {addr} отправил сообщение: {message}')
        messages.append(message)

        con.send('\n'.join(messages).encode())

        con.close()

if __name__ == '__main__':
    server()