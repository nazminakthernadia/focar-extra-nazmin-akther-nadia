# focar.py - functions for controlling the FoCar movement and LED
from machine import Pin, PWM
from time import sleep

# Motor pins (E = speed PWM, M = direction)
e1 = PWM(Pin(28)); m1 = Pin(27, Pin.OUT)   # right motor
e2 = PWM(Pin(26)); m2 = Pin(22, Pin.OUT)   # left motor
e1.freq(1000)
e2.freq(1000)

# LED: Pico W onboard LED. Change if FoCar has an external LED
led = Pin("LED", Pin.OUT)

SPEED = 40000   # 0 - 65535, adjust for your car


def _set(right_dir, left_dir, speed):
    m1.value(right_dir)
    m2.value(left_dir)
    e1.duty_u16(speed)
    e2.duty_u16(speed)


def forward(seconds, speed=SPEED):
    _set(1, 1, speed)
    sleep(seconds)
    stop()


def backward(seconds, speed=SPEED):
    _set(0, 0, speed)
    sleep(seconds)
    stop()


def turn_right(seconds, speed=SPEED):
    _set(0, 1, speed)
    sleep(seconds)
    stop()


def turn_left(seconds, speed=SPEED):
    _set(1, 0, speed)
    sleep(seconds)
    stop()


def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)


def led_flash(times=3, delay=0.3):
    for _ in range(times):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)