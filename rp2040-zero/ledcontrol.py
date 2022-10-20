import colors
import time
import ws2812

led = ws2812.WS2812(16, 1)


def led_on(color):
    led.pixels_fill(color)
    led.pixels_show()


def led_off():
    led.pixels_fill((0, 0, 0))
    led.pixels_show()


def cycle(i):
    while True:
        for item in i:
            yield item


def yoyo(i):
    while True:
        for item in i:
            yield item
        for item in reversed(i):
            yield item


def blink(interval=0.5):
    try:
        for color in cycle(colors.color_names):
            print(color)
            led_on(colors.colors[color])
            time.sleep(interval)
    finally:
        led_off()


def pulse(index=colors.RED, interval=0.1, base=(0, 0, 0), step=1):
    try:
        color = list(base)
        for i in yoyo(range(0, 255, step)):
            color[index] = i
            led_on(color)
            time.sleep(interval)
    finally:
        led_off()
