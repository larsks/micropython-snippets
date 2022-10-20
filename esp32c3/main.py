import board
import ledcolors

from common import colors
from machine import Timer

controller = ledcolors.Controller(board, brightness=0.1)
red_pulser = ledcolors.Pulser(controller, minval=10, step=10)
green_pulser = ledcolors.Pulser(controller, index=colors.GREEN, minval=10, step=10)
t0 = Timer(0)


def start_pulse(pulser):
    global t0
    t0.init(period=3, mode=Timer.PERIODIC, callback=pulser.tick)


def stop_pulse():
    global t0
    global controller
    t0.deinit()
    controller.all_off()


print("Use `stop_pulse()` to stop the timer")
start_pulse(red_pulser)
