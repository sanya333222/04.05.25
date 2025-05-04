img=0
irr=0
def setup():
    global img
    global irr
    size(800,600)
    img=loadImage("1.png")
    irr=loadImage("2.png")
def draw():
    global img
    global irr
    rect(100,100,100,100)
    image(img,100,150,50,50) 
    image(irr,150,150,50,50)
    
    
   
    
