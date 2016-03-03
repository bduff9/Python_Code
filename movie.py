
''' This file when complete, will contain all 
the code necessary to support the third programming 
project.  Your task is to complete it. On day 1
of the project (4/16 or 4/17), you should complete
all code indicated by "your code goes here." 
   Read through this file carefully.  It explains
some programming constructs you haven't seen
before, and it provides lots of given code so that
you have great examples to look at when you are
writing your new code.
   Part of the project will be to script a movie
of your own.  You should start thinking about a
cute little something now.                   '''

import Image, image_display, math, copy

#-------------------------------------------------
class movie:

   ''' The following function is called a class
   constructor.  Its purpose is to initialize
   any member variables that should be set when
   an instance of type movie is declared. It is
   very common for a class definition to include
   a constructor, and you will be writing the 
   constructors for some of the other classes
   we'll define.
      As we stated in the lesson, a movie is a
   collection of images.  In this case, the 
   collection is represented by a list.  In the
   constructor we set the imgList to be an 
   empty list.                             '''
   def __init__(self):
      # collection of images
      self.imgList = []
      return

   ''' addImage takes an image and simply 
   appends it to the list of images.       '''
   def addImage(self, newImage):
      # your code goes here
      #This code adds new images to the defined movie
      
      self.imgList.append(newImage)

   ''' play takes an display rate and shows 
   the movie by making a call to the display
   function we've used before              '''
   def play(self, rate):
      image_display.display_movie(self.imgList,rate)
      return

#-------------------------------------------------
class frame:

   ''' A frame is a collection of graphics objects
   which are represented by instances of the GO 
   class.
      Just as we did for the movie class, we 
   represent the collection by a list.  The 
   empty list, called GOList, should be defined
   in this constructor.                    '''
   def __init__(self):
      # collection of graphics objects
      # your code goes here
      #This code sets up the empty list of graphic objects
      
      self.GOList = []
      
   ''' addGO takes a GO instance and appends 
   it to the list of graphics objects.     '''
   def addGO(self, newGO):
      # your code goes here
      #This code adds a new graphic object to the given list
      
      self.GOList.append(newGO)

   ''' This function takes an image and
   returns a new image with all the GOs
   contained in the frame on it.
      It will make use of the GO member 
   function called render.                 '''
   def drawFrameBG(self,bg):
      # your code goes here
      #This code takes a background image and draws the given graphic objects onto it
      #by looping through every single graphic object within the list
      
      img = bg.copy()
      for x in range(len(self.GOList)):
         self.GOList[x].render(img)

      return img

   ''' This function takes a color and a size
   and returns a new image with all the GOs
   contained in the frame on it.
      It will make use of the GO member 
   function called render.                 '''
   def drawFrameColorSize(self,color,size):
      # your code goes here
      #This code creates a new image with the appropriate size and color to be
      #used as a background image.  Graphic objects are then drawn onto it by looping
      #through the given list

      img = Image.new('RGB', size, color)
      for x in range(len(self.GOList)):
         self.GOList[x].render(img)

      return img

#-------------------------------------------------
class GO:

   ''' A GO is a collection of graphics elements
   which are represented by instances of the GE 
   class.
      Just as we did for the movie and GO classes,
   we represent the collection by a list.  The 
   empty list, called GEList, should be defined
   in this constructor.                    '''
   def __init__(self):
      # collection of graphics elements: circle, line, triangle
      # your code goes here
      #This code sets up the empty graphic elements list

      self.GEList = []

   # scale a GO
   def scale(self, factor):
      # to be added later
      #This code sets up a matrix and then loops through every single point within the given objects
      #making the object bigger

      m = [[factor,0,0],[0,factor,0],[0,0,1]]
      for x in range(len(self.GEList)):
         for y in range(len(self.GEList[x].pointList)):
            if(len(self.GEList[x].pointList)==1):
               self.GEList[x].radius = self.GEList[x].radius*factor
		#I know this is not listed in the directions, however we
		#needed this line for our movie to be displayed properly
		self.GEList[x].thickness = self.GEList[x].thickness*factor
            self.GEList[x].pointList[y] = matrixPointMultiply(m,self.GEList[x].pointList[y])

   # slide a GO 
   def translate(self, overUp):
      # to be added later
      #This code makes the graphic object move a given amount of space by looping over every point in
      #every graphic object

      xFactor, yFactor = overUp
      m = [[1,0,xFactor],[0,1,yFactor],[0,0,1]]
      for x in range(len(self.GEList)):
         for y in range(len(self.GEList[x].pointList)):
            self.GEList[x].pointList[y] = matrixPointMultiply(m,self.GEList[x].pointList[y])

   # rotate a GO
   def rotate(self, angle, center):
      # to be added later
      #This code takes an angle and a center point and rotates the object by that angle around the
      #given center point by looping over every point within each graphic element

      i,j = center
      cosV = math.cos(math.radians(angle))
      sinV = math.sin(math.radians(angle))
      m = [[cosV,-sinV,0],[sinV,cosV,0],[0,0,1]]

      self.translate((-i,-j))
      for x in range(len(self.GEList)):
         for y in range(len(self.GEList[x].pointList)):
            self.GEList[x].pointList[y] = matrixPointMultiply(m,self.GEList[x].pointList[y])
      self.translate((i,j))

   ''' addGE takes a GE instance and appends 
   it to the list of graphics elements.     '''
   def addGE(self, newGE):
      # your code goes here
      #This code adds a new graphic object to the list of graphic elements

      self.GEList.append(newGE)

   ''' render takes an image and draws the
   GO on the image.  It does this by calling
   the draw function associated with each 
   GE in the GEList.                       '''
   def render(self, img):
      # your code goes here
      #This code takes a list of graphic elements and an image and draws each element onto the
      #given image

      for x in range(len(self.GEList)):
         self.GEList[x].draw(img)

#-------------------------------------------------
class GE:

   ''' helper fucntion to change input points 
   into 3d so we can translate.  This will be
   explained in more detail on monday.   '''
   def make3D(self,pt):
      pt3D = [pt[0],pt[1],1]
      return tuple(pt3D)


#-------------------------------------------------
''' The following 3 classes are classes derived 
from the GE class.  This means that, though they
have their own identity, they can be used as GEs
when it's convenient.  For example, our GO class
stores a collection of GEs, and we don't have to
specify exactly what KIND of GE each is.  
   It is customary to say that derived classes, 
like circle, line, and triangle, possess an "is-a"
relationship with the base class (GE). That is, we
can say a circle is a GE, a line is a GE, and a
triangle is a GE.                           '''
class circle(GE):  

   ''' Here is the circle constructor.  Look at 
   it carefully, because we're going to ask you
   to write the constructors for the other two
   GE classes.                              '''
   def __init__(self, center, radius,thickness,color):
      self.pointList = [self.make3D(center)]
      self.radius = radius
      self.thickness = thickness
      self.color = color
      return

   # helper function to test circle points
   ''' This code came almost directly from the
   lesson on ellipses.                     '''
   def ptOnCircle(self,pt):
      
      centerX = self.pointList[0][0]
      centerY = self.pointList[0][1]
      x,y = pt

      dist = (x - centerX)**2 + (y - centerY)**2

      return ((dist <= self.radius**2) and (dist > (self.radius - self.thickness)**2))
         

   # draw a circle!
   ''' This code came almost directly from the
   lesson on ellipses. Note that it makes a call
   to function ptInImage which we ask you to 
   define below.                        '''
   def draw(self, im):

      width, height = im.size
      
      centerX = self.pointList[0][0]
      centerY = self.pointList[0][1]

      for x in range(centerX - self.radius, centerX + self.radius + 1):
         for y in range(centerY - self.radius, centerY + self.radius + 1):
            if (ptInImage((x,y),(width,height)) and self.ptOnCircle((x,y))):
               im.putpixel((x,y), self.color)           
      return

#-------------------------------------------------
class line(GE):

   ''' constructor for the line class.  It 
   should set member variables pointList
   and color.                             '''
   def __init__(self, pt1, pt2,color):
      # your code goes here
      #This code sets up the point list and color for the line

      self.pointList = [self.make3D(pt1),self.make3D(pt2)]
      self.color = color

   ''' draw a line on a given image.  this
   code comes directly from the drawing 
   lessons.                               '''
   def draw(self, im):

      width, height = im.size
      p1 = self.pointList[0]
      p2 = self.pointList[1]
   
      dx = p2[0] - p1[0]  # difference in x coord
      dy = p2[1] - p1[1]  # difference in y coord

      if dx == 0 and dy == 0:
         return

      # draw by x or by y depending on slope
      if abs(dy) > abs(dx):  # line has |m| > 1
         #draw by y calculate x
         for y in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
            x = int(((y - p2[1]) * dx / float(dy)) + p2[0])
            if ptInImage((x,y),(width,height)):
               im.putpixel((x,y), self.color)           
      else:
         #draw by x calculate y
         for x in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1):
            y = int(((x - p2[0]) * dy / float(dx)) + p2[1])
            if ptInImage((x,y),(width,height)):
               im.putpixel((x,y), self.color)           
      return

#-------------------------------------------------
class triangle(GE):

   ''' constructor for the triangle class.  It 
   should set member variables pointList, color
   and filled.                            '''
   def __init__(self, pt1, pt2, pt3, color, filled = False):
      # your code goes here
      #This code sets up the pointlist and color and whether or not it should be filled for a triangle
      #graphic element

      self.pointList = [self.make3D(pt1),self.make3D(pt2),self.make3D(pt3)]
      self.color = color
      self.filled = filled

   ''' Determine whether the triangle is filled
   and call the appropriate draw function.    '''
   def draw(self, im):
      # your code goes here
      #This code draws a triangle, with the given specifications

      if(self.filled):
         self.drawFilledTriangle(im)
      else:
         self.drawTriangle(im)

   # helper from drawing lessons
   def sort3Pts(self):
      p1 = self.pointList[0]
      p2 = self.pointList[1]
      p3 = self.pointList[2]

      pL = p1
   
      if p2[0] < pL[0]:
         pM = pL
         pL = p2
      else:
         pM = p2
      
      if p3[0] < pL[0]:
         pR = pM
         pM = pL
         pL = p3
      else:
         if p3[0] < pM[0]:
            pR = pM
            pM = p3
         else:
            pR = p3

      return (pL,pM,pR)

   # from drawing lesson
   def drawFilledTriangle(self, im):

      # first we have to order our pts by their x value
      pL,pM,pR = self.sort3Pts()

      # we need slopes of all our lines.
      if pL[0] != pM[0]:
         dLM = (pL[1] - pM[1])/float(pL[0]-pM[0])
      if pL[0] != pR[0]:
         dLR = (pL[1] - pR[1])/float(pL[0]-pR[0])
      if pR[0] != pM[0]:
         dRM = (pR[1] - pM[1])/float(pR[0]-pM[0])

      #grab the y coordinates of the leftmost point
      y1 = pL[1]
      y2 = pL[1]
      # now we step across, drawing vertical lines
      for x in range(int(pL[0]),int(pM[0])):
         if (y1 != y2):
            vLine = line((x,int(y1)),(x,int(y2)),self.color)
            vLine.draw(im)
   
         # new y values corresponding to a step in the x direction
         y1 = y1 + dLM
         y2 = y2 + dLR
   
      # reset y1 to the y value of the middle pt
      y1 = pM[1]
      for x in range(int(pM[0]),int(pR[0])):
         if (y1 != y2):  
            vLine = line((x,int(y1)),(x,int(y2)),self.color)
            vLine.draw(im)
         
         # new y values corresponding to a step in the x direction
         y1 = y1 + dRM
         y2 = y2 + dLR

      return

   # from drawing lesson
   def drawTriangle(self, im):
      l1 = line(self.pointList[0], self.pointList[1],self.color)
      l2 = line(self.pointList[0], self.pointList[2],self.color)
      l3 = line(self.pointList[1], self.pointList[2],self.color)
      l1.draw(im)
      l2.draw(im)
      l3.draw(im)
      return

#-------------------------------------------------
def matrixPointMultiply(matrix, point):
   newPoint = [0,0,0]
   for i in range(3):
      for j in range(3):
         newPoint[i] += matrix[i][j]*point[j]
   return tuple(newPoint)

''' This function returns true if the given
point location exists in the given image '''
def ptInImage(pt,imDim):
   # your code goes here
   #This code simply checks to see if a given point is a valid point within the given image

   w,h = imDim
   x,y = pt
   inImage = False

   if(x>0 and x<w and y>0 and y<h):
      inImage = True

   return inImage

''' here is our movie code about a soccer player '''

#This sets the background and soccer ball up
bg = Image.open("soccerfield.jpg")
sBall = circle((50,280), 10, 10, (255,255,255))
ball = GO()
ball.addGE(sBall)

#This sets the rotating box up
box1 = line((170,140),(170,230),(0,0,0))
box2 = line((170,230),(200,230),(0,0,0))
box3 = line((170,140),(200,140),(0,0,0))
box4 = line((200,140),(200,230),(0,0,0))
boxlist = []
for y in range(140,231):
   boxlist.append(line((170,y),(200,y),(0,0,0)))
upBox = GO()
for x in range(len(boxlist)):
   upBox.addGE(boxlist[x])
upBox.addGE(box1)
upBox.addGE(box2)
upBox.addGE(box3)
upBox.addGE(box4)

#this sets the hurdle up
h = triangle((400,230),(400,285),(440,285), (0,0,0),True)
hurdle = GO()
hurdle.addGE(h)

#This code sets up the soccer player, done by individual body parts
rLeg1 = line((565,285),(555,258),(0,0,0))
rLeg2 = line((573,230),(555,258),(0,0,0))
lLeg1 = line((573,230),(581,258),(0,0,0))
lLeg2 = line((581,258),(599,250),(0,0,0))
torso = line((573,230),(573,195),(0,0,0))
head = circle((573,185),10,10,(0,0,0))
rArm1 = line((573,203),(560,203),(0,0,0))
rArm2 = line((560,203),(555,190),(0,0,0))
lArm1 = line((573,203),(586,203),(0,0,0))
lArm2 = line((586,203),(591,216),(0,0,0))
man = GO()
man.addGE(rLeg1)
man.addGE(rLeg2)
man.addGE(lLeg1)
man.addGE(lLeg2)
man.addGE(torso)
man.addGE(head)
man.addGE(rArm1)
man.addGE(rArm2)
man.addGE(lArm1)
man.addGE(lArm2)

#this is the first frame with everything in its first position
f = frame()
f.addGO(ball)
f.addGO(upBox)
f.addGO(hurdle)
f.addGO(man)

m = movie()
m.addImage(f.drawFrameBG(bg))

#Second frame
f2 = frame()
upBox.rotate(90,(185,185))
man.translate((-6,0))
f2.addGO(ball)
f2.addGO(upBox)
f2.addGO(hurdle)
f2.addGO(man)

m.addImage(f2.drawFrameBG(bg))

#Third frame
f3 = frame()
upBox.rotate(90,(185,185))
man.translate((-6,0))
f3.addGO(ball)
f3.addGO(upBox)
f3.addGO(hurdle)
f3.addGO(man)

m.addImage(f3.drawFrameBG(bg))

#This is a loop to add the majority of the movie
frames = []
adj = 1
for i in range(95):
   frames.append(frame())
   upBox.rotate(90,(185,185))
   if(i>=16 and i<=23):
      man.translate((-6,-7))
   elif(i>=27 and i<=34):
      man.translate((-6,7))
   elif(i>=50 and i<=53):
      man.translate((-15,0))
      man.rotate(22,((573-(i*6+adj*9)),285))
      adj = adj+1
   elif(i>=83):
      man.translate((-6,0))
      ball.scale(2)
   else:
      man.translate((-6,0))
   frames[i].addGO(ball)
   frames[i].addGO(upBox)
   frames[i].addGO(hurdle)
   frames[i].addGO(man)

   m.addImage(frames[i].drawFrameBG(bg))

#These last two frames are the end, where the viewer gets hit with the
#kicked soccer ball and sees red then black
f4 = frame()
m.addImage(f4.drawFrameColorSize((255,0,0), (600,400))

f5 = frame()
m.addImage(f5.drawFrameColorSize((0,0,0), (600,400))

#This finally displays the complete movie at a rate of 5 fps
m.play(5)