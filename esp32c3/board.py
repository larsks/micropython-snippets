from machine import Pin


LED_RED = Pin(3, Pin.OUT)
LED_BLUE = Pin(5, Pin.OUT)
LED_GREEN = Pin(4, Pin.OUT)
LED_WHITE = Pin(19, Pin.OUT)
LED_AMBER = Pin(18, Pin.OUT)

LEDS = [LED_RED, LED_GREEN, LED_BLUE, LED_WHITE, LED_AMBER]
