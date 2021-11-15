import FakeRPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
pwm=GPIO.PWM(7, 100)
pwm.start(0)
GPIO.output(3, True)
GPIO.output(5, False)
pwm.ChangeDutyCycle(50)
GPIO.output(7, True)
sleep(2)
GPIO.output(7, False)
GPIO.output(3, False)
GPIO.output(5, True)
pwm.ChangeDutyCycle(75)
GPIO.output(7, True)
sleep(3)
GPIO.output(7, False)
pwm.stop()
GPIO.cleanup()
