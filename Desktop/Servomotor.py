import RPi.GPIO as GPIO
import time
cur_x = 0
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	global servo
	servo = GPIO.PWM(7,50)
	servo.start(2.5)
	servo.ChangeDutyCycle(2.5)

def servoUp():
	global cur_X
	cur_X +=2.5
	if cur_X > 12:
		cur_X = 12.5
	servo.ChangeDutyCycle(cur_X)
	time.sleep(1)

def servoDown():
	global cur_X
	cur_X -= 2.5
	if cur_X < 2.5:
		cur_X = 2.5
	servo.ChangeDutyCycle(cur_X)
def close():
	servo.stop()
if __name__ == '__main__':
	setup()
