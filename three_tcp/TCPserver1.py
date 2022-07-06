import socket

tcpServerSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServerSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination1 = ('192.168.0.12', 8888)
destination2 = ('10.10.0.3', 8888)
tcpServerSocket1.bind(destination1)
tcpServerSocket2.bind(destination2)
tcpServerSocket1.listen(8)
tcpServerSocket2.listen(8)

while True:
    clinetSocket1, clinetAddr1 = tcpServerSocket1.accept()
    clinetSocket2, clinetAddr2 = tcpServerSocket2.accept()

    print('connected with ', clinetAddr1)
    print('connected with ', clinetAddr2)
    while True:
        receive = clinetSocket1.recvfrom(1024)
        data1 = receive[0].decode('utf-8')
        print("Data from " , clinetAddr1 , ": " , data1)
        clinetSocket1.send('received!'.encode('utf-8'))

        receive = clinetSocket2.recvfrom(1024)
        data2 = receive[0].decode('utf-8')
        print("Data from " , clinetAddr2 , ": " , data2)
        clinetSocket2.send('received!'.encode('utf-8'))

        if data1 == 'quit':
            break

    clinetSocket1.close()
    break

print('program finished')

tcpServerSocket1.close()
