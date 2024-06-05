# -*- coding: utf-8 -*-
import socket
import os

# Función para recibir información del archivo
def receive_file_info(client_socket):
    file_info = client_socket.recv(1024).decode().split()
    filename = file_info[0]
    filesize = int(file_info[1])
    return filename, filesize

# Función para recibir el archivo
def receive_file(client_socket, filename, filesize):
    with open(filename, "wb") as f:
        total_received = 0
        while total_received < filesize:
            data = client_socket.recv(4096)
            total_received += len(data)
            f.write(data)
    print("File received successfully.")

# Función principal del servidor
def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening...")
    client_socket, client_address = server_socket.accept()
    print("Conectado con " + str(client_address))
    
    filename, filesize = receive_file_info(client_socket)
    receive_file(client_socket, filename, filesize)
    
    client_socket.send("File transfer complete".encode())
    client_socket.close()
    server_socket.close()

# Ejemplo de uso
if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    
    server(HOST, PORT)