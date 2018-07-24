import RPi.GPIO as GPIO
import time


def servo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    
    #p= GPIO.PWM(7,50)
    #p.start(7.5)
    try: 
            while True:
                    GPIO.output(7,1)
                    time.sleep(0.00015)
                    GPIO.output(7,0)
            #time.sleep(1)

    except KeyboardInterrupt:
            #p.stop()
            GPIO.cleanup()
