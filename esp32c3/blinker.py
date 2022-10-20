try:
    import time
except ImportError:
    import utime as time

from machine import Pin


RED = Pin(3, Pin.OUT)
BLUE = Pin(5, Pin.OUT)
GREEN = Pin(4, Pin.OUT)
WHITE = Pin(19, Pin.OUT)
AMBER = Pin(18, Pin.OUT)

PINS = [RED, GREEN, BLUE, WHITE, AMBER]


def blink_pin(pin):
    for i in range(5):
        pin.on()
        time.sleep(0.5)
        pin.off()
        time.sleep(0.5)


# ensure everything is off to start
for pin in PINS:
    pin.off()

while True:
    for pin in PINS:
        blink_pin(pin)
