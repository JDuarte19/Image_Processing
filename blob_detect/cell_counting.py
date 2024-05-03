from dip import *

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes a input:
        image: binary image
        return: a list/dict of regions"""
        h,w = image.shape
        regions = dict()
        k = 1
        R = zeros((image.shape))

        # sets the k values or something
        # need to go in and count the regions
        '''
        This is where I could not finish. I was having trouble with my if logic
        The K values I assign to R image are not being assigned correctly
        I see happens to region 1, which gets assigned a k value of 4.
        '''

        # 10/23 desperation update
        # instead of top and left neightborhood
        # try to use 3x3 hood
        # it didnt work lol
        for i in range(h):
            for j in range(w):
                top = int(image[i-1,j])
                left = int(image[i,j-1])
                cur = int(image[i,j])

                if cur == 255 and top == 0 and left == 0:
                    R[i, j] = k
                    k = k + 1
                elif cur == 255 and top == 0 and left == 255:
                    R[i, j] = R[i, j - 1]
                elif cur == 255 and top == 255 and left == 0:
                    R[i, j] = R[i - 1, j]
                elif cur == 255 and top == 255 and left == 255:
                    if R[i-1,j] != R[i,j-1]:
                        #the k should be consistent so it should only get changed to the last lowest
                        #if left k is greater than top
                        if top < left:
                            R[i, j - 1] = R[i - 1, j]
                            R[i, j] = R[i - 1, j]
                            k = R[i , j - 1]
                        else:
                            R[i - 1, j] = R[i, j - 1]
                            R[i, j] = R[i, j - 1]
                            k = R[i , j]
                    elif R[i-1,j] == R[i,j-1]:
                        R[i,j] = R[i-1,j]


        total = 0
        for i in range(h):
            for j in range(w):
                key = R[i,j]
                if key != 0:
                    if key in regions:
                        add_array = ['i,j']
                        string = str(i) + ',' + str(j)
                        add_array[0] = string
                        regions[key] = regions[key] + add_array
                    else:
                        add_array = ['i,j']
                        string = str(i) + ',' + str(j)
                        add_array[0] = string
                        regions[key] = add_array

        return regions
        #return R

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list/dict of pixels in a region
        returns: region statistics"""
        '''
        My Blob coloring function doesnt function correctly, and I couldn't fix it before the deadline.
        I believe my other functions do work properly but I could not get accurate numbers due to the blob function.
        
        Have mercy my great and wonderful T.A.

        ASSUMING ALL THE PIXELS WITHIN THE DICT ARE ALL NEXT TO EACH OTHER AND ARE ASSIGNED CORRECT K VALUE
        
        Then this should work
        center = sum(x) // total_pixels, sum(y) //total_pixels
        area = total_pixels = len(coord_array in the region dict)
        '''
        # stats[key] = string(center), int(area)
        # list = coords, center, area
        stats = list()
        counter = 0
        for x in region:
            tester = region[x]
            count = len(tester)
            total_x = total_y = 0
            # removes any region 15 or less
            if count > 15:
                #print(counter, tester)
                for j in range(count):
                    #format should be y, x
                    coords = tester[j].split(",")
                    total_y = total_y + int(coords[0])
                    total_x = total_x + int(coords[1])

                mid_x = total_x // count
                mid_y = total_y // count
                center = (mid_x,mid_y)

                print_s = "Region: " + str(counter) + ", Area: " + str(count) + ", Centroid: " + str(center)
                print(print_s)
                new_holder = tester, center, count
                stats.append(new_holder)
                counter += 1

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text. 
        takes as input
        image: a list/dict of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        h,w = image.shape
        write_copy = zeros((h,w,3),uint8)
        #stats = coords, center, area
        for i in range(len(stats)):
            cord_list = stats[i][0]
            x, y = stats[i][1]
            area = stats[i][2]

            for j in range(area):
                #format should be y, x
                coords = cord_list[j].split(",")
                cy, cx = coords
                cy = int(cy)
                cx = int(cx)
                write_copy[cy,cx] = 255
                string = "* " + str(i) + " " + str(area)
                write_copy = putText(write_copy, string, (x,y), FONT_HERSHEY_SIMPLEX, .5, (0,0,255))

        return write_copy

