import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        if(img != None): self.rect = img.get_rect()
        self.__pos = [0,0]
    
    def draw(self, surface, clip = None):
        
        if(clip != None):
            clip = self.rect.clip(clip)
            clip.x =max(0, self.rect.x - clip.x)
            clip.y =max(0, self.rect.y - clip.y)
            
        surface.blit(self.image, self.pos, clip)
    
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    