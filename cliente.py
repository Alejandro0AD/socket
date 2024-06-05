# -*- coding: utf-8 -*-
import socket
import os

# Función para enviar información del archivo al servidor
def send_file_info(client_socket, filename):
    filesize = os.path.getsize(filename)
    client_socket.send("{} {}".format(filename, filesize).encode())

# Función para enviar el archivo al servidor
def send_file(client_socket, filename):
    with open(filename, "rb") as f:
        for _ in iter(lambda: f.read(4096), b""):
            client_socket.send(_)

# Función principal del cliente
def client(host, port, filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    send_file_info(client_socket, filename)
    send_file(client_socket, filename)
    
    response = client_socket.recv(1024).decode()
    print(response)
    
    client_socket.close()

# Ejemplo de uso
if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    FILENAME = "/home/bk/Escritorio/serv/archivo.txt"
    
    client(HOST, PORT, FILENAME)