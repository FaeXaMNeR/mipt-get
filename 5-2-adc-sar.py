import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN, )

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    num = 0
    for bit in range(7, -1, -1):
        num += 2**bit
        num2dac(num)
        time.sleep(0.05)
        compVal = GPIO.input(comp)
        if compVal == 1:
            num -= 2**bit
    return num

try:
    while(True):
        val = adc()
        volt = float(val)/256*3.3
        print("ADC: значение = {}, входное напряжение = {:.2f}".format(num2dac(val), volt))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()