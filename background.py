import pygame
import math
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self, game):
        Sprite.__init__(self)
        
        self.image = pygame.image.load(game.assets["BG_FULL"]).convert()
        
        _logo = pygame.image.load(game.assets["LOGO"]).convert_alpha()
        _logo_rect = _logo.get_rect()

        self.rect = pygame.rect.Rect(0,0, game.size[0], game.size[1])
        
        #если запихают другого размера
        self.image = pygame.transform.smoothscale(self.image, game.size)

        #logo, так как статичный рендер
        _logo_rect = _logo_rect.move(50,36)
        self.image.blit(_logo, _logo_rect)

        _line = pygame.Rect(45, 80, 630, 3)
        pygame.draw.rect(self.image,(255,255,255), _line)


    #end of init

    
    def draw(self, renderer):
        renderer.blit(self.image, self.rect)
    
    #end of draw

#end of Background