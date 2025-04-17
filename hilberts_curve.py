!pip3 install ColabTurtle
from ColabTurtle.Turtle import *

def hilbert(side, level, ang=90):
  if level==0:
    return
  left(ang)
  hilbert(side, level-1, -ang)
  forward(side)
  right(ang)
  hilbert(side, level-1, ang)
  forward(side)
  hilbert(side, level-1, ang)
  right(ang)
  forward(side)
  hilbert(side, level-1, -ang)
  left(ang)

def run_hilbert(level, s=13):
  initializeTurtle()
  hideturtle()
  speed(s)  
  penup()
  goto(250,400)
  pendown()   
  setheading(0)
  side = 300/2**level
  hilbert(side, level)

run_hilbert(4, 13)
