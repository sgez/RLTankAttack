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
import os, sys
import time
import random
import DEFINES as df
import numpy as np
from WaterLevel import WaterLevel
from Functions import Functions
from GameState import GameState
import Speak
from graphs.RLGraph import RLGraph
import md5


def LearnedFromGame(G_game):
    f = Functions()
    reward = getReward(G_game)
    Speak.say("finale")
    print "Agent Smith: Reward: ",reward
    G_move = 0
    while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
        G_move+=1
    G_move -= 1
    p1_n_1, p2_n_1, wl_n_1 = getState(G_game, G_move-1) # last move
    p1_n, p2_n, wl_n = getState(G_game, G_move) #game finishing move
    f.file_write("./games/"+str(G_game)+"/moves/"+str(G_move)+"/r",str(reward))
    RLG = RLGraph()
    RLDG = RLG.getGraph() 
    
def LearnAndAct(G_game):
    f = Functions()
    #RL DiGraph
    RLG = RLGraph()
    RLDG = RLG.getGraph() 
    G_move = 0
    while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
        G_move+=1
    G_move -= 1
    p1, p2, wl = getState(G_game, G_move)
    #print "even a1 - odd a2"
    #print "{a=0|1}&{col=[0,wl.columns]} POP PUSH col"
    #print  "{a=2|3}&{col=-1} LEFT RIGHT boat"
    npnd = (wl, p1, p2)
    nd =  md5.new(str(npnd)).hexdigest()
    path = RLG.getPath(nd,'1')
    print 'Node md5:',nd
    #print RLDG.nodes()
    print 'Path: ',path
    
    if(str(path)=='-1'):
        print 'RANDOM ACTION'
        f.file_append("./games/"+str(G_game)+"/rlactions",'random\n')
        return randAction()
    else:
        print 'SMART ACTION'
        f.file_append("./games/"+str(G_game)+"/rlactions",'smart\n')
        arr = RLDG[path[0]][path[1]]['a'].split(" ")
        rv = int(arr[0]),int(arr[1])
        return setAction(rv[0],rv[1])
    
    
def get_p1p2wl_files(G_game, G_move):
    '''GET p1, p2, wl 
    
    files ON current path
    
    '''
    p1_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p1"
    p2_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2"
    wl_file = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/wl"
    return p1_file, p2_file, wl_file

def arrays_load_from_txt_p1p2wl(G_game, G_move):
    '''NUMPY load p1, p2, wl from files 
    
    '''
    p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
    p1 =  np.loadtxt(p1_file,dtype=np.bool)
    p2 =  np.loadtxt(p2_file,dtype=np.bool)
    wl =  np.loadtxt(wl_file,dtype=np.bool)
    return p1, p2, wl

def arrays_load_from_txt_p1p2wl_int(G_game, G_move):
    '''NUMPY load p1, p2, wl from files int
    
    '''
    p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
    p1 =  np.loadtxt(p1_file,dtype=np.int)
    p2 =  np.loadtxt(p2_file,dtype=np.int)
    wl =  np.loadtxt(wl_file,dtype=np.int)
    return p1, p2, wl

def arrays_save_to_text_p1p2wl(G_game, G_move, p1, p2, wl):
    '''NUMPY save p1, p2, wl to files 
    
    '''
    p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
    np.savetxt(p1_file, p1, fmt='%d')
    np.savetxt(p2_file, p2, fmt='%d')
    np.savetxt(wl_file, wl, fmt='%d')

def getReward(G_game):
    '''GET REWARD 
    
    Get reward (-1, 0, 1) for current G_game  
    
    ''' 
    f = Functions()
    return f.file_read_int("./games/"+str(G_game)+"/reward")

def getState(G_game, G_move):
    '''GET STATE 
    p1, p2 & wl FOR move IN game
    
    '''
    return arrays_load_from_txt_p1p2wl_int(G_game, G_move)

def setAction(a, col=-1):
    '''SET ACTION based on 
      a: action identifier
    col: integer
    a=0 or 1 and col is number N of column to pop(0,N) or push(1,N) water
    {a=0|1}&{col=[0,wl.columns]}
    a=2 or 3 and col is -1 to move boat left(2) or right(3)
    {a=2|3}&{col=-1}
    '''
    G_game = 0
    G_move = 0
    f = Functions()
    while os.path.exists("./games/"+str(G_game)):
        G_game+=1
    G_game -= 1
    while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
        G_move+=1
    G_move -= 1
    #action = str(a)+" "+str(col)
    #f.file_write("./games/"+str(G_game)+"/moves/"+str(G_move)+"/a2",action)
    if(col>=0 and col<get_columns_number()):
        if(a==0):
            return move_str_pop_column(str(col)),a,col
        if(a==1):
            return move_str_push_column(str(col)),a,col
    else:
        if(a==2):
            return move_str_boat_left(),a,col
        if(a==3):
            return move_str_boat_right(),a,col

def randAction():
    '''Random action generator player
    
    '''
    a = random.randint(0, 3)
    if(a==0 or a==1):
        c = random.randint(0, get_columns_number()-1)
    else:
        c=-1
    #print a, c, setAction(a,c)
    return setAction(a,c)

def move_str_pop_column(col):
    ''' ACTION 
    
    POP COLUMN
    
    '''
    print 'POPING'
    return 'wl = f.pop_column(wl,'+col+')'

def move_str_push_column(col):
    ''' ACTION 
    
    PUSH COLUMN
    
    '''
    ############todo############### move down boats
    return 'wl = f.push_column(wl,'+col+')'


def move_str_boat_left():
    ''' ACTION 
    
    MOVE BOAT LEFT
    
    '''
    return 'p2 = f.move_left(p2)'

def move_str_boat_right():
    ''' ACTION 
    
    MOVE BOAT RIGHT
    
    '''
    return 'p2 = f.move_right(p2)'
 

def get_columns_number():
    '''GET COLUMN NUMBER SIZE integer
    
    Get number of columns for water level array
    
    '''
    return df.NUMBER_OF_WATERS

def make_move(G_game, G_move):    
    gs = GameState()
    
    f = Functions()
    finished = f.file_read_int("./games/"+str(G_game)+"/finished")
    turn = f.file_read_int("./games/"+str(G_game)+"/turn")
    if(turn==1 and finished==0):
        while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
            G_move+=1
        G_move -= 1
        print 'Agent Smith: Mr Anderson, this is my move!'+"./games/"+str(G_game)+"/moves/"+str(G_move)
        p1, p2, wl = getState(G_game, G_move)
        
        exec_move = LearnAndAct(G_game)
        
        exec(exec_move[0])
        
        G_move += 1
        if(not os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move))):
            os.mkdir("./games/"+str(G_game)+"/moves/"+str(G_move))
        p1_file, p2_file, wl_file = get_p1p2wl_files(G_game, G_move)
        arrays_save_to_text_p1p2wl(G_game, G_move, p1, p2, wl)
        action = str(exec_move[1])+" "+str(exec_move[2])
        print exec_move
        f.file_write("./games/"+str(G_game)+"/moves/"+str(G_move)+"/a2",action)
        f.file_write("./games/"+str(G_game)+"/turn","0")
        reward = getReward(G_game)
        f.file_write("./games/"+str(G_game)+"/moves/"+str(G_move)+"/r",str(reward))
        return 1
    elif(turn==0 and finished==0):
        while os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)):
            G_move+=1
        G_move -= 1
        #print 'It is not my turn............'+"./games/"+str(G_game)+"/moves/"+str(G_move)
        return 0
    elif(finished==1):
        reward = getReward(G_game)
        Speak.say("finale")
        print "Agent Smith: My Reward: ",reward
        f.file_write("./games/"+str(G_game)+"/moves/"+str(G_move)+"/r",str(reward))
        if(reward==1):
            Speak.say("winner")
        exit()
    
def main():
    try:
        Speak.say("intro")
        G_move = 0
        G_game = 0
        
        while os.path.exists("./games/"+str(G_game)):
            G_game+=1
        G_game -= 1
        i=0
        f = Functions()
        
        while(True):
            time.sleep(.5)
            turn = f.file_read_int("./games/"+str(G_game)+"/turn")
            finished = f.file_read_int("./games/"+str(G_game)+"/finished")
            if(turn==1 and finished==0):
                i+=make_move(G_game, G_move)
                time.sleep(.1)
            if(finished==1):
                LearnedFromGame(G_game)
                exit()
    except RuntimeError as e:
        print e
        exit()
if __name__ == '__main__':
    main()
