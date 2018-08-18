import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        if(img != None): self.rect = img.get_rect()
        self.__pos = [0,0]
    
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        