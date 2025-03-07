import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN, )

def dec2bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]

def num2dac(num):
    signal = dec2bin(num)
    GPIO.output(dac, signal)
    return signal

def adc():
    for i in range(256):
        num2dac(i)
        time.sleep(0.01)
        compVal = GPIO.input(comp)
        if compVal == 1:
            return i
    return 255

try:
    while True:
        val = adc()
        volt = float(val) * 3.3 / 256
        print("ADC: значение = {}, текущее напряжение = {:.2f}".format(num2dac(val), volt))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()