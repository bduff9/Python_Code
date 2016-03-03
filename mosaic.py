from PIL import Image
import os

# the distance function takes 2 pixels as input
# and returns the squared distance between them.

def distance(pix1, pix2):
    dist = 0
    for i in range(3):
        dist = dist + (pix1[i] - pix2[i])*(pix1[i] - pix2[i])
    return dist

# place your code for the "scale" function here

def scale(img, wscale, hscale):

    width,height=img.size
    w=int(width*wscale)
    h=int(height*hscale)
    newimg = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pix=img.getpixel((x/wscale,y/hscale))
            newimg.putpixel((x,y), pix)
                            
    return newimg

# place your code for the "putBlock" function here

def putBlock(imgBlock, img, start):
    width,height=img.size
    w,h=imgBlock.size
    for x in range(start[0],start[0]+w):
        for y in range(start[1],start[1]+h):
            pix=imgBlock.getpixel((x-start[0],y-start[1]))
            img.putpixel((x,y), pix)
            
def average(img):

    w,h=img.size
    r,g,b=[],[],[]
    
    for x in range(w):
        for y in range(h):
            r2,g2,b2=img.getpixel((x,y))
            r.append(r2)
            g.append(g2)
            b.append(b2)

    red=0
    green=0
    blue=0
    pix=len(r)
    
    for z in range(pix):
        red=red+r[z]
        green=green+g[z]
        blue=blue+b[z]

    avgPix=(red/pix,green/pix,blue/pix)
    
    return avgPix

def buildTile(img, tileSize):
    
    w,h=img.size
    w2,h2=tileSize
    w2=float(w2)
    h2=float(h2)
    newImg=scale(img,w2/w,h2/h)
    tile=(newImg,average(newImg))
    return tile

def scaleTarget(img, res):

    w,h=img.size
    w2,h2=res
    w2=float(w2)
    h2=float(h2)
    newImg=scale(img,w2/w,h2/h)
    return newImg

def findBestThumb(pix, tileList):

    bestValue=0
    best=0
    
    for x in range(len(tileList)):
        test=distance(pix, tileList[x][1])
        if(test<bestValue or x==0):
            bestValue=test
            best=x
               
    bestTile=tileList[best][0]
    
    return bestTile

def makeTileList(imageFileList, tileSize):

    tileList=[]
    
    for x in range(len(imageFileList)):
        img=Image.open(imageFileList[x])
        tileList.append(buildTile(img, tileSize))
        
    return tileList

def stitchMosaic(img, tileList):

    w,h=img.size
    tileW,tileH=tileList[0][0].size
    print (w,tileW,h,tileH)
    mosaicImg=Image.new('RGB',(w*tileW,h*tileH))

    for x in range(w):
        for y in range(h):
            pix=findBestThumb(img.getpixel((x,y)),tileList)
            putBlock(pix,mosaicImg,(x*tileW,y*tileH))
    
    return mosaicImg

# the buildMosaic function orchestrates the creation of the mosaic.
# It requires a target image file, and directory of images to use
# as a tile library, a tile size, and a mosaic resolution, as input.
# Though it returns nothing, its effect is to save a photoMosaic in
# a .jpg file.

def buildMosaic(imageFile, imageDirectory, tileSize, res):

    # Task 1:  create a list of image file names from a directory
    
    imgFileList = os.listdir(imageDirectory)
    for i in range(len(imgFileList)):
        imgFileList[i]=imageDirectory + r"\\" + imgFileList[i]

    # Task 2:  create a list of tiles by calling makeTileList.

    tileList=makeTileList(imgFileList, tileSize)
    
    # Task 3:  scale target image by calling scaleTarget.

    img=scaleTarget(imageFile,res)
    
    # Task 4:  create the mosaic image by calling stitchMosaic.

    mosaicImg=stitchMosaic(img,tileList)
    
    # Task 5:  save the mosaic image to a file.

    mosaicImg.save("newmosaic.jpg")
