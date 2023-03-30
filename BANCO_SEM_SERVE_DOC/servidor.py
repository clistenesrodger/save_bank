import socket
import threading

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        response = data.decode().upper().encode()
        conn.send(response)

    print(f"Conexão encerrada com {addr}")
    conn.close()

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Servidor iniciado em {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    start_server('127.0.0.1', 8000)