import datetime

class Functions: 
    def __init__(self):
        now = datetime.datetime.now()
        self.STARTUP_STAMP = now.strftime("%Y-%m-%d_%H.%M.%S")
         
    def log(self, txt):
        f = open('log/Game_' + self.get_startup_stamp() + '.xml', 'a')
        f.write(txt + "\n")
        f.close()
    
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
        
