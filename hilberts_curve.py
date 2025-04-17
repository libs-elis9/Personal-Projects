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

def run_hilbert(level: int, s: int=13):
  '''
  Draw's Hilberts Curve

  :param level: the level of curve (square within a square)
  :param s: speed at which the curve is drawn
  '''
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
