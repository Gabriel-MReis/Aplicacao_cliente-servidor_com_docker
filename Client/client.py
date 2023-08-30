import socket

def main():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(data)
        user_input = input()
        client_socket.send(user_input.encode())

    client_socket.close()

if __name__ == '__main__':
    main()