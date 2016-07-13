from Myro import *
init ("sim")
i = 0 # Start the counter
k = 0
speed = 1
seconds = 1
degrees = 90
penDown()
while i < 360:
    forward (1, .01)
    motors(-.1, .25, 0.4) 
    i = i + 1



 