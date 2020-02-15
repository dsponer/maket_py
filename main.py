import RPi.GPIO as maket_pin
import time

maket_pin.setmode(maket_pin.BOARD)

maket_pin.setup(16, maket_pin.OUT)
maket_pin.setup(18, maket_pin.OUT)

maket_pin.output(16, 1)
maket_pin.output(18, 1)
time.sleep(10)
maket_pin.output(16, 0)
maket_pin.output(18, 0)
time.sleep(1)
maket_pin.cleanup()

