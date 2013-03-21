import cv2 as cv
import numpy as np

class Ass2:
    
    def noise_reduction(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("2", gray)
        blur_img = cv.medianBlur(gray, 7)
        cv.imshow("3", blur_img)
        return blur_img
    
    def edge_detection(self, img):
        edges = img.copy()
        cv.Laplacian(img, -1, edges, 5)
        cv.imshow("5", edges)
        s, thre = cv.threshold(edges, 125, 255, cv.THRESH_BINARY_INV)
        cv.imshow("4", thre)
        return thre  
    
    def paint(self, img, edges):
        i = 1;
        filters_array = np.array([img] * 8)
        filters_array[0] = img
        while(i <= 7):
            filters_array[i] = cv.bilateralFilter(filters_array[i - 1], 9, 9, 7)
            i += 1
        color_edges = cv.cvtColor(edges, cv.COLOR_GRAY2RGB)
        return cv.bitwise_and(filters_array[7], color_edges)
        
        
img = cv.imread("D:\\test.JPG")
ass = Ass2()
gray = ass.noise_reduction(img)
edge_thre = ass.edge_detection(gray)
fltr = ass.paint(img, edge_thre)
cv.imshow("1", fltr)
cv.waitKey(0)