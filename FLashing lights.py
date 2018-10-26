from gpiozero import LED
red = LED (17)
yellow = LED(27)
green = LED (22)

red.blink = (1,1)
yellow.blink = (1,1)
green.blink =(3,3)
