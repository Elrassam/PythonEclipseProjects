import cv2 as cv

class Ass2:
    
    def noise_reduction(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur_img = cv.medianBlur(gray, 7)
        return blur_img
    
    def edge_detection(self, img):
        edges = img.copy()
        cv.Laplacian(img, -1, edges, 5)
        s, thre = cv.threshold(edges, 125, 255, cv.THRESH_BINARY_INV)
        return thre  
    
    def paint(self, img, edges):
        fltr = cv.bilateralFilter(img, 9, 30, 700)
        color_edges = cv.cvtColor(edges, cv.COLOR_GRAY2RGB)
        cv.imshow("2", color_edges)
        return cv.bitwise_and(fltr, color_edges)
        
        
img = cv.imread("D:\\test.JPG")
ass = Ass2()
gray = ass.noise_reduction(img)
edge_thre = ass.edge_detection(gray)
fltr = ass.paint(img, edge_thre)
cv.imshow("1", fltr)
cv.waitKey(0)