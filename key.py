from re import A
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

GPIO.setmode(GPIO.BCM)
gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)
servo = GPIO.PWM(gp_out, 50)
servo.start(0)

def servo_angle(degree):
    return int((degree + 90) * 9.5 / 180 + 2.5) ##角度をデューティ比に変換

def unlock():
    servo.ChangeDutyCycle(12) #0度に回転
    time.sleep(1) #3秒待つ 
    servo.ChangeDutyCycle(2.5) #90度に回転

def lock():
    servo.ChangeDutyCycle(servo_angle(90)) #90度に回転
    time.sleep(3) #3秒待つ 

unlock() #開ける
#lock()
servo.stop()
GPIO.cleanup()