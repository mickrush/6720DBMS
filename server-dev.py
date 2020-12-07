import socket
import random
import math
import hashlib
import time
import sys
import parser


def main():
    args = sys.argv
    HOST = '127.0.0.1'
    PORT = 5879
    dbdestination = str(args[1])
    print("The chosen path is: ", dbdestination)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print("connected by", addr)
            while True:
                statement = conn.recv(1024).decode()
                print(parser.parse(statement))

                if not statement:
                    conn.close()


if __name__ == "__main__":
    main()
