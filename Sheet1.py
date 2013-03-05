import numpy as np
import scipy.misc as scm
import matplotlib.pyplot as plt

class Sheet1:
    
    img = None
    cdf = None
    max = None
    
    def __init__(self, img_in, max):
        self.img = img_in
        self.max = max
    
    def calc_hist(self):
        img = self.img
        hist = [0] * self.max
        for i in range(len(img)):
            for j in range(len(img[0])):
                hist[int(img[i][j])] += 1
        return hist
    
    
    def cumulative_distribution_function(self):
        img = self.img
        rows = len(img)
        cols = len(img[0])
        hist = self.calc_hist()
#        print hist
        weight = 1.0 / (rows * cols)
        cdf = [0] * self.max
        j = 0
        while j < self.max:
            cdf[j] = sum(hist[0:(j+1)]) * weight
            j += 1
        return cdf
    
    
    def call(self,x):
        return int((self.cdf[int(x)]) * (self.max - 1))

    def histogram_equalization(self):
        img = self.img
        rows = len(img)
        cols = len(img[0])
        new_img = [[0] * cols] * rows
        self.cdf = self.cumulative_distribution_function()
#        print self.cdf
        for i in range(rows):
            new_img[i] = map(self.call, img[i])
        return new_img        
        
        
    def display_hist(self, img, i, fig):
        fig.add_subplot(2, 2, i)
        plt.hist(img, self.max, facecolor='g')
        
        

img = scm.imread("D:\\b.jpg", True)
#np.resize(img, (300,300))
#img = np.array([[52, 55, 61, 66,  70,  61,  64, 73],
#[63, 59, 55, 90,  109, 85,  69, 72],
#[62, 59, 68, 113, 144, 104, 66, 73],
#[63, 58, 71, 122, 154, 106, 70, 69],
#[67, 61, 68, 104, 126, 88,  68, 70],
#[79, 65, 60, 70,  77,  68,  58, 75],
#[85, 71, 64, 59,  55,  61,  65, 83],
#[87, 79, 69, 68,  65,  76,  78, 94]])
#img = np.array([[1,3,1,2], [2,6,1,3], [1,2,3,2], [3,1,4,1]])
sh = Sheet1(img, 256)
new_image = sh.histogram_equalization()
#sh2 = Sheet1(new_image, 8)
#hist = sh2.calc_hist()
#print hist
#fig = plt.figure()

#fig.add_subplot(2, 2, 1)
#plt.imshow(img, "gray")
#plt.title("Before")
#fig.add_subplot(2, 2, 2)

plt.imshow(new_image, "gray")
#plt.title("After")
#sh.display_hist(img, 3, fig)
#sh.display_hist(new_image, 4, fig)
plt.show()
        
        