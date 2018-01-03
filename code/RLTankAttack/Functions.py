import datetime, os
import numpy as np
import DEFINES as df

class Functions: 
    def __init__(self):
        now = datetime.datetime.now()
        self.STARTUP_STAMP = now.strftime("%Y-%m-%d_%H.%M.%S")
         
    def log(self, txt):
        f = open(self.log_file(), 'a')
        f.write(""+str(txt) + "\n")
        f.close()
    
    def log_file(self):
        return 'log/Game_' + self.get_startup_stamp() + '.html'
    def get_stamp(self):    
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def get_startup_stamp(self):    
        return self.STARTUP_STAMP
    
    def pop_water(self, arr, col):
        height = len(arr)
        for i in range(0, height):
            if(arr[i][col] == True):
                arr[i][col] = False
                break
        return arr

    def push_water(self, arr, col):
        height = len(arr)
        rng = range(0, height)
        rng.reverse()
        for i in rng:
            print i
            if(arr[i][col] == False):
                arr[i][col] = True
                break
        return arr
    
    def who_is_winner(self, water_level, boat_row):
        retval = -1
        '''
           ret vals: -1, 0, 1
                 -1: no winner i.e. still playing
                  0: player id 0
                  1: player id 1
        water_level: water level array
           boat_row: position for each boat on top array
        '''
        return retval   
    
    def file_write(self, filename, txt):
        try:
            rwrd = open (filename,'w')
            rwrd.write(txt)
            rwrd.close()
        except Exception as e:
            print "Minor: File write error"
    def file_append(self, filename, txt):
        try:
            rwrd = open (filename,'a')
            rwrd.write(txt)
            rwrd.close()
        except Exception as e:
            print "Minor: File write error"
            
    def file_read_int(self, filename):
        fl = open (filename,'r')
        retval = int(fl.read())
        fl.close()
        return retval
    
    def file_read_int_arr(self, filename):
        fl = open (filename,'r')
        str = fl.read()
        fl.close()
        arr = str.split(" ")
        retval = int(arr[0]),int(arr[1])
        return retval
    
    def logmove(self, G_game, G_move):
        G_Path = "./games/"+str(G_game)+"/moves/"+str(G_move)+"/"
        if(not os.path.exists(G_Path)):
           os.makedirs(G_Path)
        WL_Path = G_Path + "wl"
        P1_Path = G_Path + "p1"
        P2_Path = G_Path + "p2" 
        np.savetxt(WL_Path,df.WATER_LEVEL, fmt='%d')
        np.savetxt(P1_Path,df.BOATS_ARRAY[0], fmt='%d')
        if(not os.path.exists("./games/"+str(G_game)+"/moves/"+str(G_move)+"/p2")):
            np.savetxt(P2_Path,df.BOATS_ARRAY[1], fmt='%d')
        G_move+=1
        return G_move
    
    def pop_column(self, array, col):
        height = len(array) #y
        width = len(array[0]) #x
        for i in range(height):
            if(array[i][col]==True):
                array[i][col] = False
                break
        return array
    
    def push_column(self, array, col):
        height = len(array) #y
        width = len(array[0]) #x
        for i in range(height-1,-1,-1):
            if(array[i][col]==False):
                array[i][col] = True
                break
        return array

    def get_coords(self, boat):
        ###return where boat is currently 
        retval=np.where(boat == True)
        return retval[0][0],retval[1][0]
    
    def get_coords_x(self, boat):
        ###return where boat is currently 
        retval=np.where(boat == True)
        return retval[1][0]
    
    def move_left(self, boat):
        binit = boat
        try:
            lim_left = 0
            lim_right = len(boat[0]) - 1
            cur_y,cur_x = self.get_coords(boat)
            if(cur_x>lim_left and cur_x<=lim_right):
                cur_x = cur_x-1
            boat[:,:][:,:] = 0
            boat[cur_y][cur_x] = 1
            return boat
        except IndexError:
            print "Not valid"
            return binit
    
    def move_right(self, boat):
        binit = boat
        try:
            lim_left = 0
            lim_right = len(boat[0]) - 1
            cur_y,cur_x = self.get_coords(boat)
            if(cur_x>lim_left and cur_x<lim_right):
                cur_x = cur_x+1
            boat[:,:][:,:] = 0
            boat[cur_y][cur_x] = 1
            return boat
        except IndexError:
            print "Not valid"
            return binit  
        
    def move_pop_down(self, boat, col):
        print boat
        binit = boat
        try:
            lim_down = 0
            lim_up = len(boat) - 1 
            cur_y,cur_x = self.get_coords(boat)
            print lim_down, lim_up
            print cur_y,cur_x
            if(cur_y<=lim_up and cur_x==col):
                cur_y = cur_y-1
            print cur_y,cur_x
            boat[:,:][:,:] = 0
            boat[cur_y][cur_x] = 1
            print boat
            return boat
        except IndexError:
            print "Not valid"
            return binit
        
    def move_push_up(self, boat, col):
        print boat
        binit = boat
        try:
            lim_down = 0
            lim_up = len(boat) - 1
            cur_y,cur_x = self.get_coords(boat)
            print lim_down, lim_up
            print cur_y,cur_x
            if(cur_y<=lim_up and cur_x==col):
                cur_y = cur_y+1
            boat[:,:][:,:] = 0
            boat[cur_y][cur_x] = 1
            print boat
            return boat
        except IndexError:
            print "Not valid"
            return binit
        
