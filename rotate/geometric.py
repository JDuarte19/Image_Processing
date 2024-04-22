from .interpolation import interpolation
from dip import *
import math
 
class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        # original height,width
        h, w = image.shape

        # constants
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        max_width = round(abs(w * cos_theta) + abs(h * sin_theta)) + 1
        max_height = round(abs(h * cos_theta) + abs(w * sin_theta)) + 1
        rotated = zeros((max_height, max_width))
        
        # find center with respect to original and new
        og_width = round(((w + 1) / 2) - 1)
        og_height = round(((h + 1) / 2) - 1)
        cx = round(((max_width + 1) / 2) - 1)
        cy = round(((max_height + 1) / 2) - 1)
        # nested for loop like a boss
        for i in range(h):
            for j in range(w):
                y = h - 1 - i - og_height
                x = w - 1 - j - og_width
                new_x = round(x * cos_theta + y * sin_theta)
                new_y = round(x * -sin_theta + y * cos_theta)
                new_x = cx - new_x
                new_y = cy - new_y

                if 0 <= new_x < max_width and 0 <= new_y < max_height and new_x >= 0 and new_y >= 0:
                    rotated[new_y, new_x] = image[i, j]

        return rotated

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by an angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""
        # constants
        h, w = rotated_image.shape
        og_h, og_w = original_shape
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        inversed = zeros((og_h,og_w))

        for i in range(h):
            for j in range(w):
                x = w - j - (w//2)
                y = h - i - (h//2)
                new_x = round(x * cos_theta + y * -sin_theta)
                new_y = round(x * sin_theta + y * cos_theta)
                new_x = (og_w//2) - new_x - 1
                new_y = (og_h//2) - new_y - 1
                if new_x >= 0 and new_y>= 0 and new_x < og_w and new_y < og_h:
                    inversed[round(new_y),round(new_x)] = rotated_image[i,j]
        # return image
        return inversed

    def rotate(self, image, theta, interpolation_type):
        # original height,width
        h, w = image.shape
        # constants
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        org_x, org_y = (w // 2, h // 2)
        # new h,w and new mid points
        new_height = round(abs(h * math.cos(theta)) + abs(w * math.sin(theta))) + 1
        new_width = round(abs(w * math.cos(theta)) + abs(h * math.sin(theta))) + 1
        new_x, new_y = (new_width // 2, new_height // 2)
        # new image shape
        rotated_img = zeros((new_height, new_width))
        for i in range(new_height):
            for j in range(new_width):
                if interpolation_type == "nearest_neighbor":
                    x = (i - new_x) * cos_theta + (j - new_y) * sin_theta
                    y = -(i - new_x) * sin_theta + (j - new_y) * cos_theta
                    x = math.floor(x + org_x)
                    y = math.floor(y + org_y)
                    if (x >= 0 and y >= 0 and x < h and y < w):
                        rotated_img[i, j] = image[x, y]
                if interpolation_type == "bilinear":
                    y = (i - new_x) * cos_theta + (j - new_y) * sin_theta
                    x = -(i - new_x) * sin_theta + (j - new_y) * cos_theta
                    #get point in new graph?
                    x = x + org_x
                    y = y + org_y
                    x2 = math.floor(x + .5)
                    y2 = math.floor(y + .5)
                    y1 = math.floor(y)
                    x1 = math.floor(x)
                    god = interpolation()
                    p1 = self.find_pixel(image, (y1, x1))
                    p2 = self.find_pixel(image, (y1, x2))
                    p3 = self.find_pixel(image, (y2, x1))
                    p4 = self.find_pixel(image, (y2, x2))
                    new_i = god.bilinear_interpolation(x2, y2, p1, p2, p3, p4, i, j)
                    if (x >= 0 and y >= 0 and x < h and y < w):
                        rotated_img[i, j] = new_i

        #return image
        return rotated_img

        #return image
        return rotated_img

    def find_pixel(self, image, coord):
        y,x = coord
        h,w = image.shape
        # hard coding power
        # was having issues with accessing pixels outside of actual image size
        # this helps but for some reason edges aren't returned correctly
        # first if gets everything not an edge
        # second if should be entered when x is max length or greater
        # nested if will catch bottom right corner?
        # third if gets called when x is less than 0
        # wtf is wrong
        if 0 <= x <= w-1 and 0 <= y <= h-1:
            pixel = image[y,x]
            return pixel
        if x > w -1:
            if y > h-1:
                return image[h-1,w-1]
            else:
                return image[y,w-1]
        if x < 0:
            if y > h-1:
                return image[h-1, 0]
            else:
                return image[y, 0]
        if y > h-1 and x < w-1:
            return image[h-1,x]
        else:
            #edges of original dont get counted???
            return 40

