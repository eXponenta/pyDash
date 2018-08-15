import pygame

from pygame.font import Font
from pygame.sprite import Sprite

print('def font' + pygame.font.get_default_font())


class TextSprite(Sprite):

    def __init__(self, text = "", fontname = None, size = 32):

        self.x = self.y = 0 
        self.centered = False

        self.font = Font(fontname or pygame.font.get_default_font(), size)
        self.set_text(text)

    #end of init

    def set_text(self, text, color = None):
       
        self.image = self.font.render(text, True, color or (255,255,255))
        self.rect = self.image.get_rect()

    #end of text
    
    def draw(self, renderer):
        
        _x = self.x
        _y = self.y

        if (self.centered) :
            _x -= self.rect.w / 2
            _y -= self.rect.h / 2
        
        renderer.blit(self.image, (_x, _y))
    #end of draw

#end of TextSprite