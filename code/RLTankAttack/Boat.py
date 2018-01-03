import pygame
import DEFINES as df 
import numpy as np

#TODO implement move_up, move_down, move_left, move_right 
#attribute for boat

class Boat(pygame.sprite.Sprite):
    def __init__(self, img, surface):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/"+img+".png")
        image = image.convert()
        self.image, self.rect = image, image.get_rect()
        self.surface = surface
        LOOKING_TO_THE_RIGHT = True
        if img == "boat_1":
			self.image = pygame.transform.flip(self.image, 1, 0)
			LOOKING_TO_THE_RIGHT = False
        if img == "boat_0":
            self.rect.center = (40,df.TOP)
        if img == "boat_1":
            self.rect.center = (160,df.TOP)

        if(LOOKING_TO_THE_RIGHT):
			self.id = 0
        else:
			self.id = 1
        
        self.draw()
        
    def update(self):
       self.rect.center = self.pos
       
    #draw boat on surface blit
    def draw(self):
        self.surface.blit(self.image, self.rect)	
       
    #returns true if boat is over pos position
    def over_point(self, pos):
		rv = False
		if self.rect.collidepoint(pos):
			rv = True
		return rv
	
    def get_boat_id(self):
		return self.id

    #move horizontally by STEP step
    def move_hor(self, STEP):
        retval = False    
        return retval
    
    #move vertically by STEP step
    def move_ver(self, STEP):
        retval = False    
        return retval
    
    #set boat coordinates based on NxM array (size of WATER_LEVEL array)
    def draw_boat(self):
        for i in range(0, df.NUMBER_OF_WATERS):
            k = df.HEIGHT_OF_WATER - 1
            for j in range (df.BOTTOM, df.TOP, -df.STEPy):
                if df.BOATS_ARRAY[self.get_boat_id()][k][i] == True:
                    self.rect.bottomleft = (df.LEFT + i * df.STEP + i * df.MARGIN, j-df.STEPy/4)
                    break
                k -= 1
        self.draw()
    
    def set_coords(self):
        self.boat_array = df.BOATS_ARRAY[self.get_boat_id()]
                
    def get_coords(self):
        ###return where boat is currently 
        retval=np.where(df.BOATS_ARRAY[self.get_boat_id()] == True)
        return retval[0][0],retval[1][0]
    
    def move_left(self):
        arr = df.BOATS_ARRAY[self.get_boat_id()]
        cur_y,cur_x = self.get_coords()
        lim_left = 0
        lim_right = df.NUMBER_OF_WATERS - 1
        if(cur_x>lim_left and cur_x<=lim_right):
            cur_x = cur_x-1
        df.BOATS_ARRAY[self.get_boat_id()][:,:][:,:] = 0
        df.BOATS_ARRAY[self.get_boat_id()][cur_y][cur_x] = 1
        
    def move_right(self):
        arr = df.BOATS_ARRAY[self.get_boat_id()]
        cur_y,cur_x = self.get_coords()
        lim_left = 0
        lim_right = df.NUMBER_OF_WATERS - 1
        if(cur_x>=lim_left and cur_x<lim_right):
            cur_x = cur_x+1
        df.BOATS_ARRAY[self.get_boat_id()][:,:][:,:] = 0
        df.BOATS_ARRAY[self.get_boat_id()][cur_y][cur_x] = 1
        
    def move_up(self):
        arr = df.BOATS_ARRAY[self.get_boat_id()]
        cur_y,cur_x = self.get_coords()
        lim_bottom = 0
        lim_top = df.HEIGHT_OF_WATER - 1
        if(cur_y>lim_bottom and cur_y<=lim_top):
            cur_y = cur_y-1
        df.BOATS_ARRAY[self.get_boat_id()][:,:][:,:] = 0
        df.BOATS_ARRAY[self.get_boat_id()][cur_y][cur_x] = 1
    
    def move_down(self):
        cur_y,cur_x = self.get_coords()
        lim_bottom = 0
        lim_top = df.HEIGHT_OF_WATER - 1
        if(cur_y>=lim_bottom and cur_y<lim_top):
            cur_y = cur_y+1
        df.BOATS_ARRAY[self.get_boat_id()][:,:][:,:] = 0
        df.BOATS_ARRAY[self.get_boat_id()][cur_y][cur_x] = 1
        