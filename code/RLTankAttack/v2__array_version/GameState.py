import numpy as np

class GameState():
    def __init__(self):
        self.TIE = -1
        self.STILL_PLAYING = 2
        self.BOAT_0_ID = 0
        self.BOAT_1_ID = 1
        #print "GameState class loaded"
    
    #return array with message
    #id of state: 
    #0 or 1 for boat 0 or 1
    #2 if still playing
    #-1 if game is tie
    def state(self, water_level, boats):
        retval = ("Still playing...",2)
        print "======================="
        print "======================="
        print water_level
        print "======================="
        print boats[0]
        print "======================="
        print boats[1]
        xy0 = self.get_coords(boats[0])
        xy1 = self.get_coords(boats[1])
        print "======================="
        print "======================="
        for i in range(0,2):
            xy = self.get_coords(boats[i])
            if(water_level[xy[0]][xy[1]]==False):
                retval = ("LOSER BOAT:"+str(i),i)
                break
        return retval    
        
    def get_coords(self,boat_array):
        retval=np.where(boat_array == True)
        return retval[0][0],retval[1][0]