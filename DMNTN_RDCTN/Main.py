import matplotlib.pyplot as plt
import networkx as nx
from DataGenerator import DataGenerator
from Graph_Construction import GraphConstruction
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
    
def take_integer_from_user(message):
    inp = raw_input(message)
    while True:
        try: 
            int(inp)
            break
        except ValueError: 
            inp = raw_input('You must specify a number: ')
    return int(inp)

fig_swiss = plt.figure()
dg = DataGenerator()
inp = take_integer_from_user('Press 1 for photos, 2 for Swiss Roll: ')
if inp == 1 :
    a = dg.generateFacesPoints("C:\\Users\\Elrassam\\Desktop\\Faces\\")
    numOfPoints = 400
elif inp == 2:   
    numOfPoints = take_integer_from_user('Enter the number of points: ')
    a = dg.generateSwissRoll(numOfPoints, 3)
    ax = fig_swiss.add_subplot(111, projection='3d')
    xs = a[:,0]
    ys = a[:,1]
    zs = a[:,2]
    ax.scatter(xs, ys, zs)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')


graph_con = GraphConstruction(numOfPoints)
graph_con.pre_construction(a, numOfPoints)
inp = take_integer_from_user('Press 1 for K neighbor, 2 for epsilon: ')
if inp == 1 :
    graph_con.graph_k_neighbor(numOfPoints)
elif inp == 2: 
    inp = take_integer_from_user('Epsilon value? ')
    graph_con.graph_epsilon_sphere(numOfPoints, inp)

G = graph_con.G
plt.figure()
nx.draw(G)
plt.show()

plt.figure()
while True:
    largest_hub = take_integer_from_user('Enter the node number to show its neighbors, or -1 for exit: ')
    if largest_hub == -1:
        break
    else:
        node_and_degree=G.degree()
        hub_ego=nx.ego_graph(G,largest_hub)
        pos=nx.spring_layout(hub_ego)
        nx.draw(hub_ego,pos,node_color='b',node_size=2000)
        nx.draw_networkx_nodes(hub_ego,pos,nodelist=[largest_hub],node_size=2000,node_color='r')
        plt.show()


        