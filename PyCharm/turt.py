# import turtle
# my_pen = turtle.Turtle()
# for i in range(100):
#    my_pen.forward(50)
#    my_pen.right(90)
# turtle.done()
import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.speed(1)
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)