import networkx as nx
import os
import glob
from pprint import pprint
import numpy as np
import md5

'''
while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
    G_move+=1
G_move -= 1
'''
class RLGraph:
    DG=nx.DiGraph()
    def getGraph(self, draw=False):
        if(os.path.exists("DG.gpickle")):
            pprint("Loading pickled directed graph")
            self.DG=nx.read_gpickle("DG.gpickle")
            if(draw):
                nx.draw_circular(self.DG) 
                plt.show()
        
        rewardlist = sorted(glob.glob('.\games\*\reward'), key=os.path.getmtime)

        for i in range(0, len(rewardlist)):
            fl = open(rewardlist[i],'r')
            #print fl.read()
           
        nd = "START" 
        prevnd = "START"
        
        moveslist = sorted(glob.glob('.\games/*/*/*/'), key=os.path.getmtime)
        
        for i in range(0, len(moveslist)):
            npwl = np.loadtxt(moveslist[i]+"/wl",dtype=np.int)
            npp1 = np.loadtxt(moveslist[i]+"/p1",dtype=np.int)
            npp2 = np.loadtxt(moveslist[i]+"/p2",dtype=np.int)
            rf = open(moveslist[i]+"r",'r')
            r = rf.read()
            
            npnd = (npwl, npp1, npp2)
            nd =  md5.new(str(npnd)).hexdigest()
            
            #pprint(r)
            if(int(r)==-1):
                nd = "-1"
            elif(int(r)==1):
                nd = "1"
            
            if(len(prevnd)<3 and not prevnd=='0'):
                if(prevnd=="-1"):
                    prevnd = "START"
                if(prevnd=="1"):
                    prevnd = "START"
            try:    
                if(i%2==0):
                    af = open(moveslist[i]+"/a1",'r')
                else:
                    af = open(moveslist[i]+"/a2",'r')
                a = af.read()
            except Exception as e:
                #print 'Exception raised'
                a='0 0'
                
            self.DG.add_edge(prevnd, nd)
            self.DG[prevnd][nd]['a'] = a
            
            #pprint((nd,prevnd))
            #pprint(npnd)
            #print "================================================"
            #pprint(prevnd)
            prevnd = nd
        
        pprint("Nodes: "+str(len(self.DG.nodes())))
        pprint("Edges: "+str(len(self.DG.edges())))
        if(draw):
            nx.draw_circular(self.DG) 
            plt.show()
            
        nx.write_gpickle(self.DG,"DG.gpickle")
        
        pprint("Pickling directed graph")
        pprint("Nodes: "+str(len(self.DG.nodes())))
        pprint("Edges: "+str(len(self.DG.edges())))
        
        return self.DG
    
    def getPath(self, node1, node2):
        try:
            if(nx.has_path(self.DG,node1,node2)):
                print node1, node2
                print nx.shortest_path_length(self.DG,node1,node2)
                return(nx.shortest_path(self.DG,node1,node2))
            else:
                return('-1')
        except Exception as ex:
            print ex 
            return('-1')
            

#USAGE for functions
'''
import matplotlib.pyplot as plt
DGO = RLGraph()
G = DGO.getGraph(True)
'''

