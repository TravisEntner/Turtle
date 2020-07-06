import turtle

s = turtle.getscreen()
t = turtle.Turtle() 
t.fillcolor("Blue")
for n in range(4):
  t.left(90)
  t.forward(90)
t.color("red")
t.goto(100,100)

for n in range(4):
  t.left(90)
  t.forward(90)
t.goto(0,0)
t.penup()
t.goto(10, 100)
t.pendown()
t.goto(-90,0)
t.penup()
t.goto(10,190)
t.pendown()
t.goto(-90,90)
t.penup()
t.goto(100, 190)
t.pendown()
t.goto(0,90)
t.penup()

t.goto(1000,1000)
