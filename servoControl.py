import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.IN, pull_up_down = GPIO.PUD_UP)

try: 
	while True:
		input_status = GPIO.input(12)
		if input_status == False:
			print "button clicked"
			GPIO.output(7,1)
			time.sleep(0.0015)
			GPIO.output(7,0)

1
except KeyboardInterrupt:
	GPIO.cleanup()

