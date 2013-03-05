import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as scm
from matplotlib.figure import Figure

class Methods:
    
    #3) a
    def plot_intensities(self, A):
        A = np.reshape(A, len(A) * len(A[0]))
        A.sort()
        A = A[-1::-1]
        plt.plot(A)
        plt.show()
    
    #3) b    
    def display_hist(self, A):
        A = np.reshape(A, len(A) * len(A[0]))
        plt.hist(A, 20, facecolor='g')
        Figure()
        plt.show()
    
    #3) c
    def change_255(self, x):
        return (x >= 100)*255;
    

    def change_color(self):
        A = scm.imread('C:/Users/Carnival/Desktop/g.png')
        A[:,:,0] = map(self.change_255, A[:,:,0]);
        A[:,:,1] = 0
        A[:,:,2] = 0
        plt.imshow(A)
        plt.show() 
    
    #3) d
    def bottom_left(self, A):
        w = len(A[0])
        h = len(A)
        B = A[h//2:h, 0:w//2];
        plt.imshow(B, 'gray')
        plt.show()
    
    #3) e
    def subtract_mean(self, A):
        B = np.array(A)
        B = B - np.mean(B)
        B = B.clip(0, 256)
        plt.imshow(B, 'gray')
        plt.show()
    
    #3) f
    def roll(self):
        a = np.ceil(np.random.rand(1) * 6);
        print(a);
    
    #3) g
    def get_max(self, A):
        index = np.argmax(A)
        r = index / len(A[0])
        c = index - (r * len(A[0]))
        x = A[r, c]
        print x, r, c
        
    #3) h
    def count_ones(self):
        print [1, 8, 8, 2, 1, 3, 9, 8].count(1)
    
    #2)
    def procedure(self, img):
        fig = plt.figure()
        fig1 = fig.add_subplot(2, 4, 6)
        plt.imshow(img, 'gray')
        plt.title("original")
        
        self.get_negative(img, fig, 1)
        self.get_mirror(img, fig, 2)
        self.swap_channels(fig, 3)
        self.get_avg_with_mirror(img, fig, 4)
        self.add_clip(fig, 5)
        plt.show()

    #2) 1
    def get_negative(self, img, fig, i):
        fig1 = fig.add_subplot(2, 4, i)
        plt.imshow(255 - img, 'gray')
        plt.title("negative")

    
    #2) 2
    def get_mirror(self, A, fig, i):
        fig1 = fig.add_subplot(2, 4, i)
        plt.imshow(np.fliplr(A), 'gray')
        plt.title("mirror")
    
    #2) 3
    def swap_channels(self, fig, i):
        img = scm.imread('D:\\color.jpg')
        fig1 = fig.add_subplot(2, 4, 7)
        plt.imshow(img)
        plt.title("original")
        r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        rgb = np.dstack((b,g,r))
        fig2 = fig.add_subplot(2, 4, i)
        plt.imshow(rgb)
        plt.title("swap")
    
    #2) 4
    def get_avg_with_mirror(self, A, fig, i):
        img = (A + np.fliplr(A)) / 2
        fig1 = fig.add_subplot(2, 4, i)
        plt.imshow(img, 'gray')
        plt.title("avg with mirror")
    
    #2) 5
    def add_clip(self, fig, i):
        A = scm.imread('C:/Users/Carnival/Desktop/g.png')
        n = np.random.randint(256)
        A = A + n
        A.clip(0, 255)
        fig1 = fig.add_subplot(2, 4, i)
        plt.imshow(A, 'gray')
        plt.title("clipping")
        
    
A = scm.imread('C:/Users/Carnival/Desktop/g.png', True)
A_colored =  scm.imread("D:\\color.jpg")
methods = Methods()
#methods.plot_intensities(A)
#methods.display_hist(A)
#methods.change_color()
methods.subtract_mean(A)
#methods.roll()
#methods.bottom_left(A)
#methods.count_ones()
#methods.procedure(A)




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