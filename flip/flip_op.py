#perform horizontal or vertical flipping of an image
from dependencies import *

class flip:
    def __init__(self):
        pass

    def flip(self, image, direction):
        output_image = ones((image.shape),uint8)
        h, w , c = image.shape

        if direction == "horizontal":
            for i in range(0, h):
                for j in range(0, w):
                    output_image[i, j] = image[h - 1 - i, j]
        elif direction == "vertical":
            for i in range(0, h):
                for j in range(0, w):
                    output_image[i, j] = image[i, w - 1 - j]
        else:
            print("Not Valid Directional Flip")

        return output_image