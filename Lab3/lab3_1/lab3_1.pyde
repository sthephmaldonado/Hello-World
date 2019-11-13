#3-1
# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
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
    
myCar1 = Car(color(225, 20, 147), 0, 100, 2)
myCar2 = Car(color(154, 50, 205), 0, 10, 1)
if ((keyCode) and ((key == 'space key'))):
    myCar2 = Car(color(random(255)), 0, 10, 1)
else: 
    myCar2 = Car(color(154, 50, 205), 0, 10, 1)
    
#
    
def setup():
    size(200,200)
    
def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()


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
    
myBox1 = Car(color(225, 20, 147), 0, 100, 2)
myBox2 = Car(color(154, 50, 205), 0, 10, 4)
myBox3 = Car(color(139, 71, 93), 0, 20, 3)
myBox4 = Car(color(255, 255, 0), 0, 40, 3)
myBox2 = Car(color(random(255)), 0, 50, 1)

def setup():
    size(200,200)
         
def draw():
  background(255)
  myBox1.drive()
  myBox1.display()
  myBox2.drive()
  myBox2.display()
  myBox3.drive()
  myBox3.display()
  myBox4.drive()
  myBox4.display()

  
  # From the car function 3-1 I changed Car for Box and I made 2 more boxes going in differents speeds. 
  
  #3-4
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
    
myBox1 = Car(color(225, 20, 147), 0, 100, 2)
myBox2 = Car(color(154, 50, 205), 0, 10, 4)
myBox3 = Car(color(139, 71, 93), 0, 20, 3)
myBox4 = Car(color(255, 255, 0), 0, 40, 3)
myBox2 = Car(color(random(255)), 0, 50, 1)

def setup():
    size(200,200)
         
def draw():
  background(187,255,255)
  myBox1.drive()
  myBox1.display()
  myBox2.drive()
  myBox2.display()
  myBox3.drive()
  myBox3.display()
  myBox4.drive()
  myBox4.display()
  

def draw():
  line(mouseX, mouseY, pmouseX, pmouseY) 
  
##I tried this code but it didnt allow me to pick the position of the element using the mouse. 
#The only code that worked out was this one. https://processing.org/tutorials/interactivity/

#3-5
def setup():
    size(200, 200)
    background(187,255,255)

def draw():
    fill(255, 0, 0)
    ellipse(50, 50, 50, 50)



def setup():
    size(200, 200)
    background(187,255,255)

def draw ():
      if (mousePressed) 
      fill(255, 0, 0)
      ellipse(mouseX, mouseY, circleSize, circleSize)
circleSize++
    else 
circleSize = 0

#I tried to run this code, creating Brush Strokes (https://www.uniquesoftwaredev.com/intro-to-processing-creating-colorful-brush-strokes/) 
#but it kept breaking and I wasnt sure if what I was doing was right. 
  
