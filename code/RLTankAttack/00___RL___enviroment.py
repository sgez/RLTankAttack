from pybrain.rl.environments.environment import Environment
from scipy import zeros
import numpy as np
from WaterLevel import WaterLevel
from Functions import Functions
import os

class RLTank(Environment):
    f = Functions()
    G_move = 0
    G_game = 0
    while os.path.exists("./games/"+str(G_game)):
        G_game+=1
    G_game -= 1
    p1 =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/p1",dtype=np.bool)
    p2 =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2",dtype=np.bool)
    wl =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/wl",dtype=np.bool)
    
    def __init__(self):
        self.f = Functions()
        self.G_move = 0
        self.G_game = 0
        while os.path.exists("./games/"+str(G_game)):
            self.G_game+=1
        self.G_game -= 1
        self.p1 =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/p1",dtype=np.bool)
        self.p2 =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2",dtype=np.bool)
        self.wl =  np.loadtxt("./games/"+str(G_game)+"/moves/"+str(G_move)+"/wl",dtype=np.bool)
    
    def get_p1p2wl_files(self, G_game, G_move):
        p1_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p1"
        p2_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2"
        wl_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/wl"
        return p1_file, p2_file, wl_file
    
    def arrays_load_from_txt_p1p2wl(self, G_game, G_move):
        p1_file, p2_file, wl_file = self.get_p1p2wl_files(G_game, G_move)
        p1 =  np.loadtxt(p1_file,dtype=np.bool)
        p2 =  np.loadtxt(p2_file,dtype=np.bool)
        wl =  np.loadtxt(wl_file,dtype=np.bool)
        return p1, p2, wl

    def arrays_save_to_text_p1p2wl(self, G_game, G_move, p1, p2, wl):
        p1_file, p2_file, wl_file = self.get_p1p2wl_files(G_game, G_move)
        np.savetxt(p1_file, p1, fmt='%d')
        np.savetxt(p2_file, p2, fmt='%d')
        np.savetxt(wl_file, wl, fmt='%d')
    
    def getSensors(self):
        self.G_game -= 1
        while os.path.exists("./games/"+str(self.G_game)+"/moves/"+str(self.G_move)):
            self.G_move+=1
        self.G_move -= 1
        self.p1, self.p2, self.wl = self.arrays_load_from_txt_p1p2wl(self.G_game, self.G_move)
        return self.p1, self.p2, self.wl
    
    def isLegal(self, p1, p2, wl):
        return True
    
    
    
    #TODO def perfomMove(self, move):