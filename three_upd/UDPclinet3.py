import socket
from threading import Timer
import time
import datetime

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = ('192.168.99.122', 8888)

i = 1
while True:
    sendData = 'hello' + str(i).zfill(4)
    udpSocket.sendto(sendData.encode('utf-8'), destination)
    print(datetime.datetime.now().strftime('%H:%M:%S.%f'))
    if i == 5:
        break
    i += 1
    time.sleep(1)

print('program finished')

udpSocket.close()