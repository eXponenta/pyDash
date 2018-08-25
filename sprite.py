import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.need_draw = True
        
        if(img == None):
            img = pygame.surface.Surface((0,0))
        
        self.image = img
        
        self.rect = pygame.Rect(0,0,0,0)
        self.last_rect = self.rect

        self.rect = img.get_rect()
        self.last_rect = self.rect
        
        self.__pos = [0,0]

    def draw(self, surface, clip = None):
        if(clip != None):
            clip = self.rect.clip(clip)
            clip.x =max(0, self.rect.x - clip.x)
            clip.y =max(0, self.rect.y - clip.y)
            
        surface.blit(self.image, self.pos, clip)
        self.need_draw = False
    
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        #self.last_rect = self.rect.copy()
        self.__pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.need_draw = True