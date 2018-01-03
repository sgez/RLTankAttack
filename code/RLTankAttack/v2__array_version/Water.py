import pygame

class Water(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/water_40x10.jpg")
        image = image.convert()
        self.image, self.rect = image, image.get_rect()
        self.rect.topleft = initial_position
        
    def draw(self, window_surface):
        window_surface.blit(self.image, self.rect)	
