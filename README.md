# Image_Processing
The goal is to show how we can use math and computer languages(python) to manipulate images through functions/algorithms to increase the amount of information that can be provided.

These programs were for a course over digital image processing, and all the mathematical equations and ideas were gained from that course, but all written code and debugging were done by myself.

All libraries I am using can be found in the requirements.txt file.

# Flip
This program will simply flip an image either horizontally or vertically.
At the moment this must be done manually.
- Usage: `python test.py'

# Rotation
There are 3 parts of this program.
1. Forward Rotation: Simply rotate an image by radians
2. Inverse Rotation: Inverse an images current position by radians
3. Interpolation Rotation: Interpolate pixels to create a clearer image (not very effective)

- Usage: 'python dip_hw1_rotate.py -i image-name -t theta -m method'
- example: 'python dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m bilinear'

# Blob Detection - WIP
This program is harder to explain. I was asked to create a program to detect blobs or regions in an image, and then to encode the image into a string of values representing 0's and 1's values.

Region Analysis starts with finding an optimal threshold using Otsu's method on the image, with the threshold value found, a binary image is created by comparing each pixel to the threshold value(if less than = 0, if greater than = 1), then a blob colorng function is performed on the image to create a regions list for any blob found.

At the moment, the blob algorithim is not working and fails to keep all regions seperate.

Finally the binary image is compressed into a binary string or character string that can be decoded to reform the binary image.

- Usage: 'python region_analysis.py -i image-name
