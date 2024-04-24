# Image_Processing
The goal is to show how we can use math and computer languages(python) to manipulate images through functions/algorithms to increase the amount of information that can be provided.

All libraries I am using can be found in the requirements.txt.

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
