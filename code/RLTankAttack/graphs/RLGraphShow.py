import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os, glob, md5, datetime
from pprint import pprint

class RLGraphShow:
    DG=nx.DiGraph()
    def show(self):
        path = os.getcwd()
        path = path[:path.rfind('graphs')]+"DG.gpickle"
        
        print path
        if(os.path.exists(path)):
            pprint("Loading pickled directed graph")
            self.DG=nx.read_gpickle(path)
            pprint("Nodes: "+str(len(self.DG.nodes())))
            pprint("Edges: "+str(len(self.DG.edges())))
            nx.draw_circular(self.DG) 
            dt = datetime.date.today()
            dt = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            pngfile = ".\images\RLGraph_"+dt+".png"
            plt.savefig(pngfile, dpi=200)
            pprint("PNG File name: "+os.getcwd()+"\\"+pngfile)
            plt.show()
        else:
            pprint("Pickle does not exist")


DGO = RLGraphShow() 
DGO.show()

