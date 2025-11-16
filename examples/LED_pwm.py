from gpiozero import PWMLED
from time import sleep
from signal import pause
"""
ledPWM = PWMLED(18)
ledPWM.value = 0
sleep(1)
ledPWM.value = 0.2
sleep(1)
ledPWM.value = 0.35
sleep(1)
ledPWM.value = 0.5
sleep(1)
ledPWM.value = 0.8
sleep(1)
ledPWM.value = 1
sleep(1)"""

ledPWM = PWMLED(18)
ledPWM.pulse()
pause()