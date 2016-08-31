import socket
import _thread as thread



HOST = ''
PORT = 8000
users = ['AmandaPanda', 'Kat']
addresses = {}
clients = set()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[--] Socket Created")
s.bind((HOST, PORT))
print("[--] Socket Bound to port " + str(PORT))

s.listen(10)
print("Listening...")


def client_thread(conn):
    for u, c in addresses.items():
            if c != addresses[username]:
                msg = username + ' is now online'
                msg = msg.encode()
                c.sendall(msg)

    while True:

        data = conn.recv(1024)
        print(type(data))
        if not data:
            break
        reply = b"" + data
        for u, c in addresses.items():
            c.sendall(reply)

    conn.close()

while True:
    conn, addr = s.accept()
    print("[--] Connected to " + addr[0] + ":" + str(addr[1]))
    data = conn.recv(1024)
    username = data.decode('utf-8')
    print(username+' has connected')
    if username in users:
        print('user is in the users list')
        addresses[username]= conn
        thread.start_new(client_thread, (conn,))

s.close()
