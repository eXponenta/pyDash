# pylint: disable=no-member
import pygame
import math
from sprite import Sprite
from text_sprite import TextSprite


class FileList(pygame.sprite.Group):

    ITEMS_PER_PAGE = 10
    ITEM_SELECTED_COLOR = (171, 249, 59)
    ITEM_DEF_COLOR = None  # (255,255,255)

    def __init__(self, game, item_contructor):
        pygame.sprite.Group.__init__(self)

        self.game = game
        self.__item_constructor = item_contructor
        self.items = []
        self.__selected = 0
        self.page = -1
        self.counters = False # show numbers near lines

        _bg = pygame.surface.Surface(
            [450, 420], pygame.SRCALPHA, 32).convert_alpha()
        _bg.fill([255, 255, 255, 20])

        self.bg = Sprite(_bg)
        self.bg.pos = [240, 90]

        self.items_pool = []

        _offset = [250, 110]
        self.text_clip_area = pygame.Rect(_offset[0], _offset[1], 450 - 20, 420 - 20)

        for i in range(10):
            _itm = TextSprite(str(i + 1) + ":",
                              game.assets['LIST_FONT'], size=36)

            _itm.pos = [_offset[0], _offset[1] + i * (36 + 4)]
            self.items_pool.append(_itm)

        self.page_counter = TextSprite(
            "СТРАНИЦА 1 ИЗ 1", game.assets['LIST_FONT'], size=18)

        self.add(self.bg)
        #self.add(*self.items_pool)
        self.add(self.page_counter)

        self.selected = 0
    # end of init

    def update_items(self):

        _all = []
        if(self.__item_constructor != None):
            _all = self.__item_constructor.all
            self.items = _all[(
                self.page - 1) * FileList.ITEMS_PER_PAGE: self.page * FileList.ITEMS_PER_PAGE]
        else:
            self.items = []

        _pages = max(math.ceil(len(_all) / FileList.ITEMS_PER_PAGE), 1)
        self.update_counter(_pages, self.page)

        for idx, itm in enumerate(self.items_pool):
            
            txt = None
            if(idx < len(self.items)):
                id = idx + (self.page - 1) * FileList.ITEMS_PER_PAGE + 1
                txt = str(self.items[idx])
                if(self.counters):
                    txt = str(id) +':' + txt
                
            itm.set_text(txt)

    # end of update_items

    def set_items(self, new, counters = False):
        self.__item_constructor = new
        self.counters = counters
        self.update_items()
        self.selected = 0

    # end of set_items

    def update_counter(self, all_pages, current_page):

        self.page_counter.set_text('СТРАНИЦА %d ИЗ %d' % (current_page, all_pages))
        self.page_counter.pos = [self.game.size[0] -
                                 40 - self.page_counter.rect.w, 520]

    # end of update_counter

    def deselect_all(self):
        self.items_pool[self.__selected % FileList.ITEMS_PER_PAGE].set_color(
            FileList.ITEM_DEF_COLOR)
    
    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, val):

        if(self.__item_constructor != None):
            _all = len(self.__item_constructor.all)
        else:
            _all = 0

        self.items_pool[self.__selected % FileList.ITEMS_PER_PAGE].set_color(
            FileList.ITEM_DEF_COLOR)

        self.__selected = val

        if(self.__selected < 0):
            self.__selected = _all - 1
        elif(self.__selected > _all - 1):
            self.__selected = 0

        _page = self.__selected // FileList.ITEMS_PER_PAGE + 1

        if(_page != self.page):
            self.page = _page
            self.update_items()

        self.items_pool[self.__selected % FileList.ITEMS_PER_PAGE].set_color(
            FileList.ITEM_SELECTED_COLOR)

    def draw(self, renderer):
        pygame.sprite.Group.draw(self, renderer)

        #render items with cliping rect
        
        for line in self.items_pool:
            line.draw(renderer, self.text_clip_area)
# end of FileList
