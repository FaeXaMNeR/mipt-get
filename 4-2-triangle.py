import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def dec2bin(num):
    number = [0 for i in range(len(dac))]
    d_num = num % 256
    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])
        i -= 1

    return number

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

flag = 1
x = 0

try:
    period = float(input())

    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            flag = 1
        elif x == 255:
            flag = 0

        if flag == 1:
            x = x + 1
        else:
            x = x - 1

        sleep(period / 512)

except ValueError:
    print("Неправильный период")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()