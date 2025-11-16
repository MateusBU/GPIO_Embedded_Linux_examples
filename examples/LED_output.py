from gpiozero import LED
from time import sleep

yellow_led = LED(18)
yellow_led.on()

sleep(1)

yellow_led.off()

sleep(1)

a = 0

while (a < 5):
    yellow_led.blink()
    sleep(1)
    a += 1