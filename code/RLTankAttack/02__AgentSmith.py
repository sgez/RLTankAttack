#Agent IS 5416
#past move: ./games/[G]/moves/[N]/p1, p2 & wl
#move to be played by agent: ./games/[G]/moves/[N+1]/p1, p2 & wl
#
#load --> think -->save
#
#will read/load p1, p2 & wl arrays
#think, learn alogrithm Q-Learn or SARSA 
#but will only write either p2 or wl at a time
#at each turn, a player can only move his/her/its own
#boat or the water level but will save all three arrays
#leaving p2 intact into to [N+1] directory
import os
import time
import DEFINES as df
import numpy as np
from WaterLevel import WaterLevel
from Functions import Functions
 
 
def get_p1p2wl_files(G_game, G_move):
    p1_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p1"
    p2_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2"
    wl_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/wl"
    return p1_file, p2_file, wl_file

def load_p1p2wl_arrays_from_text(G_game, G_move):
    p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
    p1 =  np.loadtxt(p1_file,dtype=np.bool)
    p2 =  np.loadtxt(p2_file,dtype=np.bool)
    wl =  np.loadtxt(wl_file,dtype=np.bool)
    return p1, p2, wl

def save_p1p2wl_arrays_to_text(G_game, G_move, p1, p2, wl):
    p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
    np.savetxt(p1_file, p1, fmt='%d')
    np.savetxt(p2_file, p2, fmt='%d')
    np.savetxt(wl_file, wl, fmt='%d')

def make_move(G_game, G_move):    
    fnsh = open ("./games/"+str(G_game)+"/finished",'r')
    finished = int(fnsh.read())
    fnsh.close()
    trn = open ("./games/"+str(G_game)+"/boats_turn",'r')
    turn = int(trn.read())
    trn.close()
    if(turn==1 and finished==0):
        while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
            G_move+=1
        G_move -= 1
        print 'Mr Anderson, this is my move!'+"./games/"+str(G_game)+"/moves/"+str(G_move)
        
        p1, p2, wl = load_p1p2wl_arrays_from_text(G_game, G_move)
        
        ##############MOVES BASED ON THINKING - BEGIN #####################
        
        wl = f.pop_column(wl, 3)
        #p2 = f.move_left(p2)
        ##############MOVES BASED ON THINKING -  END ######################
        
        G_move += 1
        if(not os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move))):
            os.mkdir("./games/"+str(G_game)+"/moves/"+str(G_move))
            
        p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
        save_p1p2wl_arrays_to_text(G_game, G_move, p1, p2, wl)
        
        trn = open ("./games/"+str(G_game)+"/boats_turn",'w')
        trn.write(str(0))
        trn.close()
    else:
        while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
            G_move+=1
        G_move -= 1
        print 'It is not my turn............'+"./games/"+str(G_game)+"/moves/"+str(G_move)
    if finished==1:
        rwrd = open ("./games/"+str(G_game)+"/reward",'r')
        reward = int(rwrd.read())
        rwrd.close()
        print "Never send a human to do a machine's job..."
        print "Reward: ",reward
        exit()
G_move = 0
G_game = 0

f = Functions()

while os.path.exists("./games/"+str(G_game)):
    G_game+=1
G_game -= 1

while(True):
    make_move(G_game, G_move)
    time.sleep(1)


