import cv2
import numpy as np
#from PIL import Image


class Image:
    def __init__(self, im, height, width):
        self.im = im
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


fg_image = cv2.resize(cv2.imread('/Users/mohammedfairoz/Downloads/falling_greenscreen.png'), (1080, 720))    #resize images to the same size
bg_image = cv2.resize(cv2.imread('/Users/mohammedfairoz/Downloads/city_background.png'), (1080, 720))

hsv = cv2.cvtColor(fg_image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,(36, 25, 25), (86, 255,255))
#print(hsv)
print(type(mask))
background = Image(fg_image, fg_image.shape[0], fg_image.shape[1])
foreground = Image(bg_image, bg_image.shape[0], bg_image.shape[1])

print(background.get_width()-1)

for x in range(background.get_height()):        # Iterate over each pixel in the x axis
    for y in range(background.get_width()):     # Iterate over each pixel in the y axis
        r,g,b = fg_image[x,y]
        #for array in mask:
        #print(r,g,b)
        if g > 220 and g <=255:
            fg_image[x,y] = bg_image[x,y]

        #print(r,g,b)

cv2.imshow('image', fg_image)
cv2.waitKey(0)
#cv2.imshow('image1', bg_image)
#cv2.waitKey(0)
print(type(fg_image))
