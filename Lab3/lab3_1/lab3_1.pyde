#3-1
class Car(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myCar1 = Car(color(225, 20, 147), 0, 100, 2)
myCar2 = Car(color(154, 50, 205), 0, 10, 1)
myCar2 = Car(color(random(255)), 0, 10, 1)
    
def setup():
    size(200,200)

# I HAD TO TAB ONCE TO MAKE THE CAR RUN. THERES A BLUE AND A RED CAR 
# Every time I run it a random color shows up (white, grey, darker grey)

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  
#3-2 
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
          self.xpos = 0
        if self .xpos <0;
            self.xpos = width
    
myCar1 = Car(color(225, 20, 147), 0, 100, 2)
myCar2 = Car(color(154, 50, 205), 0, 10, 1)

    
def setup():
    size(200,200)
    print("test")
    noStroke()
    
 ## I tried using this methos but it didnt actually worked if ((keyCode) and ((key == 'space key'))):
 ##myCar2 = Car(color(random(255)), 0, 10, 1) 
 ## but the function didnt actally worked.



#3-3
class Box(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myBox1 = Car(color(225, 20, 147),random(0,200),random(0,200), 2)
myBox2 = Car(color(154, 50, 205), random(0,200),random(0,200), 3)
myBox3 = Car(color(139, 71, 93), random(0,200),random(0,200), 2)
myBox4 = Car(color(255, 255, 0), random(0,200),random(0,200), 1)
myBox2 = Car(color(random(255)), random(0,200),random(0,200), 4)

def mousePressed():
    ellipse(mouseX, mouseY, 20, 20)

  
  # From the car function 3-1 I changed Car for Box and I made 2 more boxes going in differents speeds. 
  
  #3-4
  class Box(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
    def updatelocation(self,xpos, ypos):
        self.xpos=xpos
        self.ypos=ypos
        
    def display(self):
        stroke(0)
        fill(self.c)
        ellipse(CENTER)
        ellipse(self.xpos, self.ypos, 10, 10);
myDoor1 = Door(color(255, 255, 0), 0, 0, 1)

def mousePressed():
    myDoor1.updatelocation(mouseX, mouseY)
    
myCar1 = Car(color(225, 20, 147), 0, 100, 2)
myCar2 = Car(color(154, 50, 205), 0, 10, 1)
myCar3 = Car(color(255, 0, 0), 0, 450, 3)
    
myBox1 = Box(color(225, 20, 147), 0, 100, 2)
myBox2 = Box(color(154, 50, 205), 0, 10, 4)
myBox3 = Box(color(139, 71, 93), 0, 20, 3)
myBox4 = Box(color(255, 255, 0), 0, 40, 3)


  
##I tried this code but it didnt allow me to pick the position of the element using the mouse. 
#The only code that worked out was this one. https://processing.org/tutorials/interactivity/

#3-5
def setup():

    size(200,200)


def draw(): 

  background(255)

  mycar1.drive()
  mycar1.display()

  mycar2.drive()
  mycar2.display()
  
  mycar3.drive()
  mycar3.display()

  mycar4.drive()
  mycar4.display()
  
  mycar5.drive()
  mycar5.display()
  
  myBox1.drive()
  myBox1.display()
  
  myBox2.drive()
  myBox2.display()
  
  myBox3.drive()
  myBox3.display()
  
  myBox4.drive()
  myBox4.display()  
  
  mydoor1.display()
  
  
  if ((keyPressed) and (key == ' ')):
      mycar1.colorchange(color(random(255), random (255), random (255)))
      mycar3.colorchange(color(random(255), random (255), random (255)))
      mycar5.colorchange(color(random(255), random (255), random (255)))
      myBox2.colorchange(color(random(255), random (255), random (255)))
      myBox4.colorchange(color(random(255), random (255), random (255)))
  if ((keyPressed) and (key == 'a')):
      mycar2.colorchange(color(0, 0, 0))
      mycar4.colorchange(color(0, 0, 0))
      myBox1.colorchange(color(0, 0, 0))
      myBox3.colorchange(color(0, 0, 0))
      
  if ((keyPressed) and (key == 's')):
      mycar2.colorchange(color(random(255), random (255), random (255)))
      mycar4.colorchange(color(random(255), random (255), random (255)))
      myBox1.colorchange(color(random(255), random (255), random (255)))
      myBox3.colorchange(color(random(255), random (255), random (255)))

#I tried to run this code, creating Brush Strokes (https://www.uniquesoftwaredev.com/intro-to-processing-creating-colorful-brush-strokes/) 
#but it kept breaking and I wasnt sure if what I was doing was right. 
  
