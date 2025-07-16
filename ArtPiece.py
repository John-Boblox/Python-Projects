import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.penup()
t.goto(0,-200)
t.pendown()
t.circle(200)
for i in range(40):
  t.goto(0,0)
  for i in range(10):
    t.fd(100)
    t.rt(170)
    t.fd(50)
    t.goto(0,0)
  t.fd(200)
  t.rt(170)
  t.circle(10)
  t.fd(50)
