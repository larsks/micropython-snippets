import machine
from micropython import const

PIN_P11 = const(17)
PIN_P10 = const(16)
PIN_P9 = const(14)
PIN_P8 = const(12)
PIN_P7 = const(13)
PIN_P6 = const(15)
PIN_P5 = const(4)
PIN_P4 = const(1)
PIN_P3 = const(3)
PIN_P2 = const(0)
PIN_P1 = const(5)
PIN_P0 = const(2)

PIN_RX = PIN_P3
PIN_TX = PIN_P4

PIN_SCL = const(PIN_P2)
PIN_SDA = const(PIN_P0)
PIN_WAKE = const(PIN_P10)
PIN_SCLK = const(PIN_P9)
PIN_MISO = const(PIN_P8)
PIN_MOSI = const(PIN_P7)
PIN_CS = const(PIN_P6)

LED_BUILTIN = PIN_P1

PIN_A0 = PIN_P11


class I2C(machine.I2C):
    def __init__(self):
        super().__init__(machine.Pin(PIN_SCL), machine.Pin(PIN_SDA))
