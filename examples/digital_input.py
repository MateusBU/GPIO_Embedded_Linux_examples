from gpiozero import Button, LED
from signal import pause

button = Button(2)
"""while True:
    if(button.is_pressed):
        print('Button is pressed')
    else:
        print('Button is not pressed')
"""
"""
button.wait_for_press()
print('Button was pressed')

def say_hello():
    print('Hello')

def say_goodbye():
    print('Goodbye')

button.when_pressed = say_hello
button.when_released = say_goodbye
pause()"""

led = LED(18)
button.when_pressed = led.on
button.when_released = led.off
pause()
