import socket

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination = ('192.168.57.1', 8888)
tcpServerSocket.bind(destination)
tcpServerSocket.listen(8)

while True:
    clinetSocket, clinetAddr = tcpServerSocket.accept()
    print('connected with ', clinetAddr)

    while True:
        receive = clinetSocket.recvfrom(1024)
        data = receive[0].decode('utf-8')
        print(data)
        clinetSocket.send('received!'.encode('utf-8'))
        if data == 'quit':
            break

    clinetSocket.close()
    break

print('program finished')

tcpServerSocket.close()
