import pygame
import math
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self, game):
        Sprite.__init__(self)
        
        _tile = pygame.image.load(game.assets["BG"])
        _grad = pygame.image.load(game.assets["GRAD_BG"]).convert_alpha()
        _grad = pygame.transform.smoothscale(_grad, game.size)
        
        self.image = pygame.surface.Surface(game.size).convert()
        self.rect = pygame.rect.Rect(0,0, game.size[0], game.size[1])

        _t_size = _tile.get_size()
        
        # blit one pass tiled background
        for coll in range(math.ceil(game.size[0] / _t_size[0])):
            for row in range(math.ceil(game.size[1] / _t_size[1])):
                self.image.blit(_tile,(coll * _t_size[0], row * _t_size[1]))
        
        self.image.blit(_grad, self.rect)

    #end of init

    
    def draw(self, renderer):
        renderer.blit(self.image, self.rect)
    
    #end of draw

#end of Background