#from numpy import *;

#initialize array from 1 to 100 inclusive and then randomize the sequence order in place 
#k = range(1,101);
#random.shuffle(k);
#print k

#access the row with index 1 and take the all elements in it
#a = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
#b = a[1, :];
#print b;

#allocate 1 dimension array 5 with random numbers, and then check if the 
#numbers are greater than 0 or not
#f = random.rand(5,1);
#g = f > 0.5;
#print g, f

#initialize array with length 10 to zero, then sum 0.5 to each element
#initialize array with length equal to x to be ones, then multiply 0.5 to each element
#sum x and y
#x = zeros((1,10))+0.5;
#y = 0.5*ones((1,x.size));
#z = x + y;
#print z

#initialize array with values from 1 to 100 inclusive, then reverse it.
#a = arange(1,101);
#b = a[::-1];
#print b;


###########################################################################################
import numpy as np
import matplotlib.pyplot as plt
#from scipy.misc import *
import scipy.misc as scm


#A = np.random.randint(256,size=(5,5))
#A = np.reshape(A, 25, 'C')
#A.sort()
#A = A[-1::-1]
#pl.plot(A)
#pl.show()

#A = scm.imread("D:\\im.jpg", True)
#A = np.reshape(A, len(A) * len(A[0]), 'C')
#plt.hist(A, 20, facecolor='g')
#plt.show()

#A = np.random.randint(256,size=(5,5))
#R = np.array([255] * 25)
#R = np.reshape(R, (5,5))
#print R

#A = np.random.randint(256,size=(8,8))
#w, h = len(A[0]), len(A)
#bw, bh = len(A[0])//2, len(A)//2 
#sz = A.itemsize
#shape = (h-bh+1, w-bw+1, bh, bw)
#strides = (w*sz, sz, w*sz, sz) # information about how to map indices to image data
#blocks = np.lib.stride_tricks.as_strided(A, shape=shape, strides=strides)
#print blocks[bw][bh]

#A = np.random.randint(256,size=(5,5))
#A = A - np.mean(A)
#print A


#A = np.array([[111,9,3],[5,8,7],[5,8,17]])
#x = np.argmax(A)
#row = x / len(A[0])
#col = x - (row * len(A[0]))
#print x
#print row
#print col
#print A[row, col]

#print [1, 8, 8, 2, 1, 3, 9, 8].count(1)


#img = scm.imread("D:\\im.JPG")
#img = 255 - img
#r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
#lum_img = img[:,0]

#plt.imshow(img)
#plt.show() 

#rgb = np.dstack((b,g,r))
#plt.imshow(rgb)
#plt.show()
#img = np.fliplr(img)
#scm.imsave("D:\\ssss.jpg", img)



















