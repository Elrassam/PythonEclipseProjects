import numpy as np
from scipy import misc;
from scipy.sparse import csr_matrix, lil_matrix;
import os;
import glob;

class DataGenerator:

    def generateSwissRoll(self, n=100000, dim=3):
        phi = np.random.random_sample(n)
        t = (3 * np.pi / 2) * (1 + 2 * phi)
        height = 21 * np.random.random_sample(n)
        data = np.transpose(np.array([t * np.cos(t), height, t * np.sin(t)]))
        currentDim = len(data[0])
        if currentDim < dim:
            data = np.concatenate((data, np.zeros((n, dim - currentDim))), 1)
        return data
    
    def generateFacesPoints(self, path):
        i = 0
        numOfPoints = 400
        numOfDims = 92*112
        a=np.zeros((numOfPoints,numOfDims))
        for k in range(1,41):
            images=glob.iglob(path + str(k) + "\\*.pgm");
            for im in images:
                img=misc.imread(im);
                a[i]=img.reshape((92*112));
                i=i+1;
        a = a/255.0
        return a