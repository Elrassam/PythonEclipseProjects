import cv2 as cv

class Ass2:
    
    def noise_reduction(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur_img = cv.medianBlur(gray, 7)
        return blur_img
    
    def edge_detection(self, img):
        edges = img.copy()
        cv.Laplacian(img, -1, edges, 5)
        cv.imshow("2", edges)
        s, thre = cv.threshold(edges, 125, 255, cv.THRESH_BINARY_INV)
        return thre  
    
img = cv.imread("D:\\test.JPG")
ass = Ass2()
gray = ass.noise_reduction(img)
edge_thre = ass.edge_detection(gray)
cv.imshow("1", edge_thre)
cv.waitKey(0)