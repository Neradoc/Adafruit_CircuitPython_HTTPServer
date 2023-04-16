import socket

IP = "192.168.1.28"
socket.setdefaulttimeout(5)

def receive_all(sock):
    chunks = []
    while chunk := sock.recv(1024):
        chunks.append(chunk)
    return b''.join(chunks)

def load(path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((IP, 80))
        sock.sendall(b'GET '+path.encode()+b' HTTP/1.1 \r\n\r\n')
        data = receive_all(sock)
    print(data.decode())

load("../boot_out.txt")
load("../..")
