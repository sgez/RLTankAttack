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
        try:
            retval = ("Still playing...",2)
            '''
            print "======================="
            print "======================="
            print water_level
            print "======================="
            print boats[0]
            print "======================="
            print boats[1]
            print "======================="
            print "======================="
            '''
            xy0 = self.get_coords(boats[0])
            xy1 = self.get_coords(boats[1])
            
            for i in range(0,2):
                if self.boat_over_water(water_level, boats[i])==False:
                    retval = ("No Water Underneath\nLoser Boat:"+str(i),i)
                    break
                else:
                    try:
                        Y,X = self.get_coords(boats[i])
                        Y=Y-1
                        if(Y>=0):
                            if water_level[Y][X]==True:
                                retval = ("Run into Water\nLoser Boat:"+str(i),i)
                                break
                    except (RuntimeError, TypeError, NameError):
                        print "Error!"
            return retval    
        except (IndexError, RuntimeError, TypeError, NameError):
            print "Invalid move"

    def getReward(self, wl, p1, p2):
        try:
            retval = ("Still playing...",2)
            '''
            print "======================="
            print "======================="
            print water_level
            print "======================="
            print boats[0]
            print "======================="
            print boats[1]
            print "======================="
            print "======================="
            '''
            xy0 = self.get_coords(p1)
            xy1 = self.get_coords(p2)
            
            if self.boat_over_water(wl, p1)==False:
                retval = 1
            if self.boat_over_water(wl, p2)==False:
                retval = -1
            else:
                retval=0
            return retval    
        except (IndexError, RuntimeError, TypeError, NameError):
            print "Invalid move"
        
    def get_coords(self,boat_array):
        retval=np.where(boat_array == True)
        return retval[0][0],retval[1][0]
    
    def boat_over_water(self, water_level, boat):
        try:
            and_arrays = water_level & boat
            num = len(np.where(and_arrays==True)[0])
            if(num>0):
                return True
            else:
                return False
        except Exception as e:
            print e