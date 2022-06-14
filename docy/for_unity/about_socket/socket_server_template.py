import socket
import time


def main():
    HOST = '127.0.0.1'
    PORT = 8000

    # socket()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind()
    server_socket.bind((HOST, PORT))

    # listen()
    server_socket.listen()
    print("Listening...")

    # accept()
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

    t = 0
    while t < 1000:
        msg = "hello world " + str(t)
        client_socket.sendall(msg.encode())
        print('send 완료 ' + str(t))
        t += 1
        time.sleep(2)

        '''
        무한 루프를 돌면서 2초에 한번씩 데이터를 송신함.
        만약 종료 조건을 넣고 싶다면 여기에 넣으면 됨
        '''

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
