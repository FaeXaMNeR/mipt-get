import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

pwm = GPIO.PWM(24, 1000) # 1000 Hz
pwm.start(0)

try:
    while True:
        koef = int(input())

        pwm.ChangeDutyCycle(koef)
        print(3.3*koef/100)

finally:
    pwm.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()