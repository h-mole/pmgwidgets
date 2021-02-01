import socket
import sys


def connect():
    address = ('127.0.0.1', 37789)  # 服务端地址和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(address)  # 尝试连接服务端
    except Exception:
        print('[!] Server not found ot not open')

    s.close()
if __name__=='__main__':
    connect()