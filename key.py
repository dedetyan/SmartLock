from re import A
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
import sys

GPIO.setmode(GPIO.BCM)
gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)
servo = GPIO.PWM(gp_out, 50)
servo.start(0)

args = sys.argv
args = int(args[1])

def servo_angle(degree):
    return int((degree + 90) * 9.5 / 180 + 2.5)

def unlock():
    servo.ChangeDutyCycle(servo_angle(args))
    time.sleep(0.2) 
    #servo.ChangeDutyCycle(servo_angle(90))

def lock():
    servo.ChangeDutyCycle(servo_angle(90)) 
    time.sleep(0.2) 
    servo.ChangeDutyCycle(servo_angle(0))

unlock()
servo.stop()
GPIO.cleanup()