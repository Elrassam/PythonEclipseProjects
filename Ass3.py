import cv2 as cv
import numpy as np
import math as math
class Ass3:
    
    def noise_reduction(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#        cv.imshow("1", gray)
        blur_img = cv.medianBlur(gray, 7)
#        cv.imshow("2", blur_img)
        return blur_img
    
    def canny_edge_detection(self, img):
        edges = cv.Canny(img, 250, 280)
#        cv.imshow("3", edges)
        return edges
    
    def CHT(self, img):
        hough = np.array([[0] * len(img)] * len(img[0]))
        radius = np.array([135, 120, 107])
        print len(hough), len(hough[0])
        for y in range(0, len(img)):
            for x in range(0, len(img[0])):
                if img[y, x] > 200:
                    for b in range(0, len(hough[0])):
                        for r in range(0, len(radius)):
                            rhs = math.pow(radius[r], 2) - math.pow((y - b), 2)
                            if rhs >= 0:
                                a = x - math.sqrt(rhs)
                                hough[a, b] += 1
        
#        cv.imshow("d", hough)
        print hough
                        
                
img = cv.imread("coins_3.jpg", True)
size = (300,300)
img = cv.resize(img, size)
ass = Ass3()

gray_blur = ass.noise_reduction(img)
edges = ass.canny_edge_detection(gray_blur) 
ass.CHT(edges)   
#cv.waitKey(0)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
#        img_smooth_gauss = cv.GaussianBlur(img, 3, 5)
#        filter_x, filter_y = cv.getDerivKernels(1, 1, 1, True)
#        filter_x = filter_x.t()
#        gradient_x = cv.filter2D(img_smooth_gauss, -1, filter_x, 0, cv.BORDER_REFLECT101);
#        gradient_y = cv.filter2D(img_smooth_gauss, -1, filter_y, 0, cv.BORDER_REFLECT101);        