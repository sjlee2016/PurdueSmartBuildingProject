import socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)


UDP_IP = "192.168.20.92"
UDP_PORT = 5005
MESSAGE = "7"

print "UDP target IP : ", UDP_IP
print "UDP target port :", UDP_PORT
print "message :" , MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
while True:
	GPIO.output(7,1)
	time.sleep(0.0015)
	GPIO.output(7,0)
