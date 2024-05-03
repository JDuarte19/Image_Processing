from dip import *
class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""
        h,w = image.shape
        hist = [0] * 256

        for i in range(h):
            for j in range(w):
                hist[image[i][j]] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""
        threshold = min(hist)
        # summations
        p_count = sum(hist)
        final_value = max(hist)
        pvals = arange(256)

        for i in range(255):
            # total pixels in region (above/below threshold)
            p1 = sum(hist[:i])
            p2 = sum(hist[i:])
            if p1 == 0:
                p1 = 1
            if p2 == 0:
                p2 = 1
            # weights
            # total pixels in region / total pixels in the image
            w1 = p1 * (1 / p_count)
            w2 = p2 * (1 / p_count)
            # mean
            # weighted sum of intensities / total pixels in region
            # weighted sum of intensities = intensity value * its probabilitiy
            mu1 = sum(pvals[:i] * hist[:i]) / p1
            mu2 = sum(pvals[i:] * hist[i:]) / p2
            # intra-class variance = ((x-mu)^2) / total pixels in region
            var1 = sum(((pvals[:i] - mu1) ** 2) * hist[:i]) / p1
            var2 = sum(((pvals[i:] - mu2) ** 2) * hist[i:]) / p2

            # weighted sum of in class variance
            fn = (w1 * var1) + (w2 * var2)

            if fn <= final_value:
                threshold = i
                final_value = fn
            else:
                threshold = threshold

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        hist = BinaryImage.compute_histogram(self,image)
        threshold = BinaryImage.find_otsu_threshold(self,hist)
        h,w = image.shape
        bin_img = zeros((h,w))

        for i in range(h):
            for j in range(w):
                if(image[i,j] <= threshold):
                    bin_img[i,j] = 255
                else:
                    bin_img[i,j] = 0

                if bin_img[i,j] != 255.0 and bin_img[i,j] != 0.0:
                    print(i,j, bin_img[i,j])

        return bin_img


