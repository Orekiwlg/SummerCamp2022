import socket

udpSocket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination1 = ('10.10.0.3', 8888)
udpSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination2 = ('192.168.0.12', 8888)
udpSocket1.bind(destination1)
udpSocket2.bind(destination2)

while True:
    receive1 = udpSocket1.recvfrom(1024)
    data1 = receive1[0].decode('utf-8')
    address1 = str(receive1[1])
    print(data1, ' from ', address1)

    receive2 = udpSocket2.recvfrom(1024)
    data2 = receive2[0].decode('utf-8')
    address2 = str(receive2[1])
    print(data2, ' from ', address2)

    if data1 == 'quit':
        break

print('program finished')

udpSocket1.close()