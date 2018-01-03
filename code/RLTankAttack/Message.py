import pygame

class Message(pygame.sprite.Sprite):
    def __init__(self, initial_position, txt):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.Font(None, 30)
        text = font.render(txt, 1, (255, 255, 0))
        textpos = text.get_rect()
        self.image = text
        self.rect = text.get_rect()
        self.rect.bottomleft = initial_position
        
    def update(self):
       self.rect.center = self.pos

    def draw(self, window_surface):
        window_surface.blit(self.image,self.rect)	

    #TODO test setText() in ViewGame instead of creating a new object
    def setText(self,txt):
        self.mytxt = txt


    def set_center(self, initial_position):
        self.center = initial_position
