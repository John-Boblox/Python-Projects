import turtle
t = turtle.Turtle()
t.speed(0)

#makes square
def square():
  for i in range(4):
    t.fd(100)
    t.lt(90)

#makes triangle
def triangle():
  for i in range(3):
    t.fd(100)
    t.lt(120)

#makes pentagon
def pentagon():
  for i in range(5):
    t.fd(100)
    t.lt(72)
    
#makes circle
def circle():
  for i in range(360):
    t.fd(2)
    t.lt(1)
    
#makes parallelogram
def parallelogram():
  for i in range(2):
    t.fd(200)
    t.lt(60)
    t.fd(100)
    t.lt(120)

#drawing shapes
square()
triangle()
pentagon()
circle()
parallelogram()
