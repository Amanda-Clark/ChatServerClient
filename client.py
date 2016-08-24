import socket
import sys
import threading
from prompt_toolkit import prompt

def Main():
        host = ''
        port = 8000
        username = sys.argv[1]
        #print(username)
        mySocket = socket.socket()
        mySocket.connect((host, port))
        mySocket.send(username.encode())


        def recv_loop():
            while True:
                data = mySocket.recv(1024).decode()
                print('Received from server: ' + data)
        threading.Thread(target=recv_loop, daemon=True).start()
        message = ""
        while message != 'q':
            message = prompt(" -> ", patch_stdout=True)
            mySocket.send(message.encode())
        #threading.Thread(target=recv_loop, daemon=True).start()


        mySocket.close()

if __name__ == '__main__':
    Main()