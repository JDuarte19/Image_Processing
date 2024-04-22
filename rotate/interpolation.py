from dip import *

class interpolation:

    #linear so only x values
    def linear_interpolation(self, x1, x2, i1, i2, x):
        numerator = (i1*(x2 - x1) + i2*(x-x1))
        divisor = (x2 - x1)
        #why is divsor 0?
        #x2-x1 = 0 means the lengths are the same
        #what to do if divisor is 0
        if(divisor == 0):
            divisor = 2
        calc_i = numerator/divisor
        if calc_i == 0:
            return i2
        return calc_i

    # [0,0][...,0][x,0][...,0][w-1,0]
    # []
    # [0,...,y2,...,w-1]
    # [...] [h-1]

    def bilinear_interpolation(self, x2, y2, i1, i2, i3, i4, y, x):
        bottom_i = self.linear_interpolation(x, x2, i1, i2, x)
        top_i = self.linear_interpolation(x, x2, i3, i4, x)
        # not sure how the y interpolation works, since
        y_i = self.linear_interpolation(y, y2, bottom_i, top_i, y)
        return y_i