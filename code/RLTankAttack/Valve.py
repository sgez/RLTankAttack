#http://code.google.com/p/rltankattack/wiki/ThoughtsOnValveClicking
import pygame

class Valve(pygame.sprite.Sprite):
    def __init__(self, initial_position, UP, column):
        pygame.sprite.Sprite.__init__(self)
        self.LOOKING_UP = UP
        imgpath = "images/valve_downx10.png"
        if(UP):
          imgpath = "images/valve_upx10.png"
        image = pygame.image.load(imgpath)
        #image = image.convert()
        self.image, self.rect = image, image.get_rect()
        self.rect.topleft = initial_position
        self.column_of_water = column
		
    def update(self):
       self.rect.center = self.pos
       
    def lookingUp(self):
		return self.LOOKING_UP

    def animateRedRect(self):
		print "TODO Anim"
		lineRect = LineRectangle(self.rect.center)
		return lineRect
		
    def draw(self, window_surface):
        window_surface.blit(self.image, self.rect)	
        
    def get_column_of_water(self):
		return self.column_of_water	    
       
    def set_column_of_water(self, col):
		self.column_of_water = col
		
    def over(self, pos):
		rv = False
		if self.rect.collidepoint(pos):
			rv = True
		return rv
