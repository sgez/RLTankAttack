#Earth.py
import pygame

class WhosTurn(pygame.sprite.Sprite):
    def __init__(self, initial_position,look_to_the_right):
        pygame.sprite.Sprite.__init__(self)
        self.LOOKING_TO_THE_RIGHT = look_to_the_right
        if look_to_the_right == True:
            image = pygame.image.load("images/0_TURN.png")
        else:
            image = pygame.image.load("images/1_TURN.png")
        self.image, self.rect = image, image.get_rect()
        self.rect.center = initial_position
		
    def lookingToTheRight(self):
		return self.LOOKING_TO_THE_RIGHT

    def draw(self, window_surface):
        window_surface.blit(self.image, self.rect)	
        
    def changeTurn(self, BOATS_TURN):
        if(BOATS_TURN == 0):
            return 1
        elif(BOATS_TURN == 1):
            return 0

