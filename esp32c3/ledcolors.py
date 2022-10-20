import time

from common import colors
from common import itertools

from machine import PWM


class Controller:
    def __init__(self, board, brightness=1.0):
        self.leds = [
            PWM(board.LED_RED),
            PWM(board.LED_GREEN),
            PWM(board.LED_BLUE),
        ]

        self.brightness = brightness

        self.all_off()

    def set_color_rgb(self, r, g, b):
        for led, val in zip(self.leds, [int(x * self.brightness) for x in [r, g, b]]):
            led.duty(val)

    def set_color_name(self, name):
        self.set_color_rgb(*colors.colors[name])

    def all_off(self):
        self.set_color_rgb(0, 0, 0)

    def pulse(
        self,
        index=colors.RED,
        interval=0.1,
        base=(0, 0, 0),
        step=1,
        minval=0,
        maxval=255,
    ):
        try:
            color = list(base)
            for i in itertools.yoyo(range(minval, maxval, step)):
                color[index] = i
                self.set_color_rgb(*color)
                time.sleep(interval)
        finally:
            self.all_off()

    def set_brightness(self, brightness):
        self.brightness = brightness


class Pulser:
    def __init__(
        self,
        controller,
        index=colors.RED,
        base=(0, 0, 0),
        step=1,
        minval=0,
        maxval=255,
    ):
        self.controller = controller
        self.index = index
        self.base = base
        self.step = step

        self.val = itertools.yoyo(range(minval, maxval))

    def tick(self, _):
        color = list(self.base)
        color[self.index] = next(self.val)
        self.controller.set_color_rgb(*color)
