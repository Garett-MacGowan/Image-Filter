'''
Created on March 6, 2018
@author: Garett MacGowan
'''

from PIL import Image
from fractions import Fraction

def filterImage(percentEdgeTolerance, imageLocation):
    original = Image.open(imageLocation)
    #original.show()
    newImageSize = original.size #Getting size of image as a tuple
    xDexMin = 0
    yDexMin = 0
    xDexMax = newImageSize[0]-1
    yDexMax = newImageSize[1]-1
    imageArray = original.load() #Loading original image into a readable/writable array format.

    grayImage = Image.new('L', newImageSize,) #Creating new gray scale type image, with empty color parameter so that we may occupy the color ourselves.
    grayImageArray = grayImage.load() #Loading the empty gray scale image into a readable/writable array format.

    #Performing gray scale conversion operations.
    for x in range(0,xDexMax + 1):
        for y in range(0,yDexMax + 1): #Scanning down each y on the x axis
            grayImageArray[x,y] = int((imageArray[x,y][0])*0.21 + (imageArray[x,y][1])*0.72 + (imageArray[x,y][2])*0.07)

    finalImage = Image.new('RGB', newImageSize, "black") #Creating a new black image, will fill color.
    finalImageArray = finalImage.load() #Loading the black image into a readable/writable array format.

    edgeFindTolerance = (percentEdgeTolerance/100)*255

    #Populating finalImageArray with edges.
    for x in range(xDexMin,xDexMax + 1):
        for y in range(yDexMin,yDexMax + 1):
            currentLuminosity = grayImageArray[x,y]
            if (x == xDexMin):
                if (y == yDexMin):
                    if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    continue
                if (y == yDexMax):
                    if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                continue
            if (y == yDexMin):
                if (x == xDexMax):
                    if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                continue
            if (x == xDexMax):
                if (y == yDexMax):
                    if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = imageArray[x,y]
                        continue
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                continue
            if (y == yDexMax):
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = imageArray[x,y]
                    continue
                continue

            if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue
            if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                finalImageArray[x,y] = imageArray[x,y]
                continue

    return finalImage

def main(percentEdgeTolerance, imageLocation, saveLocation, saveBoolean):
    finalImage = filterImage(percentEdgeTolerance, imageLocation)
    if (saveBoolean == 1):
        finalImage.save(saveLocation)
    finalImage.show()

edgeFindTolerance = 1
imageLocation = "D:/My Documents/Queens1/GitSpace/Image-Filter/test.jpg"
saveLocation = "D:/My Documents/Queens1/GitSpace/Image-Filter/result.png"
saveBoolean = 1

main(edgeFindTolerance, imageLocation, saveLocation, saveBoolean)
