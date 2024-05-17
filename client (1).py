# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:31:30 2024

@author: Enesi
"""

import socket
import pickle

def rpc_call(func_name, args):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    request = {
        'func_name': func_name,
        'args': args
    }

    client_socket.send(pickle.dumps(request))
    response_data = client_socket.recv(4096)
    response = pickle.loads(response_data)

    client_socket.close()
    return response

if __name__ == "__main__":
    result = rpc_call('add', (10, 5))
    print("Result of add(10, 5):", result)

    result = rpc_call('subtract', (10, 5))
    print("Result of subtract(10, 5):", result)
