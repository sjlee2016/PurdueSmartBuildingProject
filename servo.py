import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
try: 
	while True:
		GPIO.output(7,1)
		time.sleep(0.00015)
		GPIO.output(7,0)
	#time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()


