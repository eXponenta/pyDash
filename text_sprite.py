import pygame

from pygame.font import Font
from sprite import Sprite

print('def font' + pygame.font.get_default_font())


class TextSprite(Sprite):

    def __init__(self, text = "", fontname = None, size = 32):
        self.font = Font(fontname or pygame.font.get_default_font(), size)
        
        Sprite.__init__(self, None)
        self.text = text
        self.set_text(text)
        
    #end of init

    def set_text(self, text, color = None):
        self.text = text
        if(self.text != None):
            self.image = self.font.render(text, True, color or (255,255,255))
        else:
            self.image.fill((255,255,255,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
    
    def set_color(self, color):
        self.set_text(self.text, color)
    #end of text

#end of TextSprite