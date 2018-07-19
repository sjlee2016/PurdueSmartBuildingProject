import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

UDP_IP = "192.168.20.92"
UDP_PORT = 5005
data = ' '
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
        data , addr = sock.recvfrom(1024)
        data=str(data)
        print("received message : ", data)
        print(data)
        print(type(data))
        print(data[2])
        if data[2]=='1':
                print("this if loop is entered")
                while True:
                        GPIO.output(7,1)
                        time.sleep(0.00015)
                        GPIO.output(7,0)
                       # data , addr = sock.recvfrom(1024)
                       # data = str(data)
                       # print(data)
                       # if data[2]=='0':
                        #        break

GPIO.cleanup()
