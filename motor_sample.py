import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO4を制御パルスの出力に設定
gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)

#「GPIO4出力」でPWMインスタンスを作成する。
#PWMの設定 サーボモータSG90の周波数は50[Hz]
#GPIO.PWM( [ピン番号] , [周波数Hz] )
#SG92RはPWMサイクル:20ms(=50Hz), 制御パルス:0.5ms〜2.4ms, (=2.5%〜12%)。
servo = GPIO.PWM(gp_out, 50)

#パルス出力開始。servo.start(デューティ比[0-100%])
servo.start(0)

def servo_angle(degree):
    return int((degree + 90) * 9.5 / 180 + 2.5)

for i in range(1):
    #デューティサイクルの値を変更することでサーボが回って角度が変わる。
    servo.ChangeDutyCycle(servo_angle(-90)) #-90度に回す
    time.sleep(0.5) #0.5秒間待つ

    servo.ChangeDutyCycle(servo_angle(90)) #+90度に回す
    time.sleep(0.5)

    servo.ChangeDutyCycle(servo_angle(0)) 
    time.sleep(0.5)

    servo.ChangeDutyCycle(servo_angle(-45)) 
    time.sleep(0.5)

    servo.ChangeDutyCycle(servo_angle(0)) 
    time.sleep(0.5)

servo.stop()
GPIO.cleanup()