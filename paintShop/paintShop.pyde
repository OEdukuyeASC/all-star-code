currentColor = ""

def setup ():
    size(400, 400)
    background(255)
    # BLACK BOX
    fill(0,0,0)
    rect(0, 0, 50, 50)
    #WHITE
    fill(255)
    rect(50, 0, 50, 50)
    #RED
    fill(255,0,0)
    rect(100, 0, 50, 50)
    #GREEN
    fill(0,255,0)
    rect( 150, 0, 50, 50)
    #BLUE
    fill(0, 0, 255)
    rect( 200, 0, 50,50)
     #GOLD
    fill(255, 212,0 )
    rect( 250, 0, 50,50)
    #TEAL
    fill(0, 255, 255)
    rect( 300, 0, 50,50)
    #PURPLE
    fill(160, 0, 255)
    rect( 350, 0, 50,50)

def draw():
    global currentColor
    radius = 20
    noStroke()
    if  mousePressed:
       # print ("X-coordinate", mouseX)
       # print ("Y-coordinate", mouseY)
        if mouseY < 50:
            if mouseX < 50:
                currentColor = "black"
            elif mouseX < 100:
                currentColor = "white"
            elif mouseX < 150:
                  currentColor = "red"
            elif mouseX < 200:
                  currentColor = "green"
            elif mouseX < 250:
                  currentColor = "blue"
            elif mouseX < 300:
                  currentColor = "gold"
            elif mouseX < 350:
                  currentColor = "teal"
            else:
                currentColor = "purple"
        else:
            if currentColor == "black":
                fill (0)
                
            elif currentColor == "white":
                fill (255)
          
            elif currentColor == "red":
                fill (255,0, 0)
                
            elif currentColor == "green":
                fill (0, 255, 0)
                
            elif currentColor == "blue":
                fill (0, 0, 255)
                
             
            elif currentColor == "gold":
                fill (255, 212, 0)
                
          
            elif currentColor == "teal":
                fill (255,255, 0)
            else:
                fill (160,0,255)
            print " Yo b"
            ellipse( mouseX, mouseY, radius, radius)
                    
            
            