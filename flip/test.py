import flip_op
from dependencies import *

def display_image(window_name, image):
    """A function to display image"""
    namedWindow(window_name)
    imshow(window_name, image)
    waitKey(0)


image = imread("compass_image.jpg")
direction = "vertical"

#display_image("test",image)

#set up enviroment to perform ops
outputDir = 'output/'
flip_operators = flip_op.flip()

flipped = flip_operators.flip(image,direction)

display_image("test",flipped)
