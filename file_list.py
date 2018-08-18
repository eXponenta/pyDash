# pylint: disable=no-member
import pygame
import math
from sprite import Sprite
from text_sprite import TextSprite

class FileList(pygame.sprite.Group):
    def __init__(self, game, item_contructor):
        pygame.sprite.Group.__init__(self)
        
        self.game = game
        self.item_constructor = item_contructor
        self.items = []
        self.index = 0
        self.page = 1

        _bg = pygame.surface.Surface([450,420], pygame.SRCALPHA, 32).convert_alpha()
        _bg.fill([255,255,255,20])
        
        self.bg = Sprite(_bg)
        self.bg.pos = [240, 90]

        self.items_pool = []
        
        _offset = [250, 110]
        for i in range(10):
            _itm = TextSprite(str(i + 1) +":" , game.assets['LIST_FONT'], size=36)
            
            _itm.pos = [_offset[0], _offset[1] + i * (36 + 4)]
            self.items_pool.append(_itm)
        
        self.page_counter = TextSprite("СТРАНИЦА 1 ИЗ 1", game.assets['LIST_FONT'], size=18)
        
        self.add(self.bg)
        self.add(*self.items_pool)
        self.add(self.page_counter)

        self.update_items()
    #end of init

    def update_items(self):

        _all = self.item_constructor.all
        self.items =  _all [(self.page - 1) * 10: self.page *  10]

        self.update_counter( math.ceil(len(_all) / 10), self.page)
        
        for idx, itm in enumerate(self.items_pool):    
            txt = "-"
            if(idx < len(self.items)):
                txt = str(idx + (self.page - 1) * 10 + 1) +":"  + str(self.items[idx])[0:40]
            itm.set_text(txt)

    #end of update_items
    
    def update_counter(self, all_pages, current_page):
        
        self.page_counter.set_text('СТРАНИЦА {0} ИЗ {1}'.format(current_page, all_pages))
        self.page_counter.pos = [self.game.size[0] - 40 - self.page_counter.rect.w, 520]

    def draw(self, renderer):
        pygame.sprite.Group.draw(self, renderer)

#end of FileList