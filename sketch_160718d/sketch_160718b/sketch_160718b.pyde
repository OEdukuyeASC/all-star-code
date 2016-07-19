myFancyVariable = 0
myLowVariable = 0
def setup ():
    size ( 4000, 4000)
    background(0,160, 220)
def draw (): 
    global myFancyVariable
    global myLowVariable
    background(0,160, 220)
    stroke (0,255,0)
    fill ( 0,0,255)
    rect(myFancyVariable, 30, 20, 55, 55)
    myFancyVariable = myFancyVariable + 100
    triangle(myLowVariable, 75, 58, 20, 86, 75)
    myLowVariable = myLowVariable + 1
    