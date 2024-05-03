from dip import *

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        h,w = binary_image.shape
        #print(h,w)
        #array of h,w full 0 now convert
        x = zeros((h,w))
        counter = 0

        # There's some things i have that i never made nicer looking or less redundant
        # This makes a the values from 255 to 1... this isnt needed but ill change later
        for i in range(h):
            for j in range(w):
                if binary_image[i,j] == 255:
                    x[i,j] = 1

        #makes a string array of size h
        rle_array = [''] * h
        # 'first pixel value' + counter + counter + counter
        # converts pixels into counts per row
        # once it hits end of row, the loop resets and first element is the first pixel of the array
        for i in range(h):
            j = 0
            pixel = x[i,0]
            count = 0
            bin_string = ''
            bin_string = str(int(pixel))
            for j in range(w):
                if pixel != x[i,j]:
                    bin_string = bin_string + ' ' + str(int(count))
                    count = 1
                if pixel == x[i, j]:
                    count += 1

                if j == w-1:
                    bin_string = bin_string + ' ' + str(int(count))
                    rle_array[i] = bin_string
                else:
                    pixel = x[i, j]

        # converts the array into a single string
        rle_string = rle_array[0]
        for i in range(h-1):
            rle_string = rle_string + ' ' + rle_array[i+1]


        return rle_string

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        rle_code = rle_code.split(" ")
        holder = [''] * height
        decoded = zeros((height, width))
        # input is long as string
        # this breaks down string into individual parts
        # i could have all those go into function
        for i in range(height):
            count = 0
            index = 1
            while count < width:
                count = count + int(rle_code[index])
                index += 1

            deleted = rle_code[0:index]
            holder[i] = deleted
            rle_code = rle_code[index:]

        # converts the row arrays into binary string array
        for i in range(height):
            bin_string = ''
            total = 0
            pixel = True
            if holder[i][0] == '1':
                pixel = True
            elif holder[i][0] == '0':
                pixel = False
            for j in range(len(holder[i][1:])):
                counter = 0
                for x in range(int(holder[i][1 + j])):
                    if pixel == True:
                        bin_string = bin_string + str(int(pixel))
                    elif pixel == False:
                        bin_string = bin_string + str(int(pixel))

                if pixel == True:
                    pixel = False
                elif pixel == False:
                    pixel = True
            holder[i] = bin_string
            bin_string = ''

        # converts the binary string into a binary image
        for i in range(height):
            for j in range(width):
                if (int(holder[i][j]) == 1):
                    decoded[i][j] = 255

        return  decoded  # replace zeros with image reconstructed from rle_Code





        




