import numpy as np
from operator import itemgetter
from scipy.sparse import lil_matrix;
import matplotlib.pyplot as plt
import networkx as nx
from DataGenerator import DataGenerator


class GraphConstruction:
    
    def __init__(self, numOfPoints):
        self.G = nx.DiGraph()
        for j in range(0,numOfPoints):
            self.G.add_node(j)
            
    def pre_construction(self, a, numOfPoints):
        SS=np.dot(a,a.T);
        diag=SS.diagonal()[np.newaxis];
        diag=diag.T;
        on=np.ones((numOfPoints,1));
        self.D=np.dot(diag,on.T)+np.dot(on,diag.T)-2*SS;
    
    def graph_k_neighbor(self, numOfPoints):
        A_K=lil_matrix((numOfPoints,numOfPoints), dtype='uint8');
        W_K=lil_matrix((numOfPoints,numOfPoints), dtype='float64');
        for i in range(0,3):
            for j in range(0,numOfPoints):
                minind=0;
                minv=np.amax(self.D[j]);
                for k in range(0,numOfPoints):
                    if(minv>self.D[j,k] and A_K[j,k]!=1 and k!=j):
                        minind=k;
                        minv=self.D[j,k];
                A_K[j,minind]=1;
                self.G.add_edge(j,minind)
                W_K[j,minind]=self.D[j,minind];
    
    def graph_epsilon_sphere(self, numOfPoints, Eps):
        A_Eps=lil_matrix((numOfPoints,numOfPoints), dtype='uint8');
        W_Eps=lil_matrix((numOfPoints,numOfPoints), dtype='float64');
        for j in range(0,numOfPoints):
            for k in range(0,numOfPoints):
                if(self.D[j,k]<=(Eps*Eps) and k!=j):
                    A_Eps[j,k]=1;
                    self.G.add_edge(j,k)
                    W_Eps[j,k]=self.D[j,k];
