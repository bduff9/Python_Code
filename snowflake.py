from PIL import Image
from movieSolution import *
import math

class snowflake(GO):

   def __init__(n, color, rotate, point, length):

      if(n==0):
         return

      return fractal



# running this will test if everything is working or not
snowflakeMovie = movie()
f = frame()
for i in range(1, 5):
   # create a fractal of order i
   t = snowflake(i,(0,0,255), false, (450,250), 125)

   # add the fractal to the movie as a new frame
   f.addGO(t)
   snowflakeMovie.addImage(f.drawFrameColorSize((255,255,255), (900,500)))
im = f.drawFrameColorSize((255,255,255), (900, 500))
snowflakeMovie.addImage(im)
snowflakeMovie.addImage(im)
snowflakeMovie.addImage(im)
snowflakeMovie.play(10)
