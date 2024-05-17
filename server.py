# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
import pickle

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

functions = {
    'add': add,
    'subtract': subtract
}

def handle_client(client_socket):
    request_data = client_socket.recv(4096)
    request = pickle.loads(request_data)

    func_name = request['func_name']
    args = request['args']

    if func_name in functions:
        result = functions[func_name](*args)
        response = pickle.dumps(result)
    else:
        response = pickle.dumps(f"Function '{func_name}' not found")

    client_socket.send(response)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server listening on port 9999")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
