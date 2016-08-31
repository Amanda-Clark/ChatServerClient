import socket
import sys
import threading
import time
from prompt_toolkit import prompt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def Main():
        host = ''
        port = 8000
        username = sys.argv[1]
        mySocket = socket.socket()
        mySocket.connect((host, port))
        mySocket.send(username.encode())

        def recv_loop():
            while True:
                data = mySocket.recv(1024).decode()
                curTime = time.strftime("%c")
                print(curTime+': ' + data)
            mySocket.close()

        threading.Thread(target=recv_loop, daemon=True).start()

        message = ""
        while message != 'q':
            message = prompt(" -> ", patch_stdout=True)
            mySocket.send(message.encode())
        mySocket.close()

if __name__ == '__main__':
    Main()