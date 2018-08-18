import os
import pygame
import math

from pygame.sprite import Group
from image_button import ImageButton
from sprite import Sprite

class MainMenuPlatformList(Group):
    
    def __init__(self, game):
        Group.__init__(self)

        self.__selected = 0
        self.game = game
        self.selector = Sprite( pygame.image.load(game.assets["SELECTOR"]).convert_alpha())
        
        self.add(self.selector)
        self.createButtons()

        self.selected = 0
    #end of init

    def update(self, dt):
        Group.update(self, dt)
    
    #end of update

    def draw(self, renderer):
    
        Group.draw(self, renderer)
    
    #end of draw
         
    def createButtons(self):
        _list = self.game.assets["ICONS"]
        self.buttons = list()

        OFFSET = [50, 90]
        SPASE = 8

        for idx, item, in enumerate(_list):
            _gen = [item['img'].format(_suff) for _suff in ['n','a','d'] if os.path.isfile(item['img'].format(_suff))]
            _imgs = [pygame.image.load(img) for img in _gen]
            
            _btn = ImageButton(_imgs)
            _btn.pos = [OFFSET[0], OFFSET[1] + (_btn.rect.height + SPASE) * idx]
            self.buttons.append(_btn)
        
        self.add(*self.buttons)
    
    #end of createButtons
    
    @property
    def selected(self):
        return self.__selected
   
    @selected.setter
    def selected(self, id):

        if(self.buttons[self.__selected].state != ImageButton.DISABLED):
            self.buttons[self.__selected].state = ImageButton.NORMAL
        
        self.__selected = id
        if(id > len(self.buttons) - 1):
            self.__selected = 0
        elif(id < 0):
            self.__selected = len(self.buttons) - 1
        
        if(self.buttons[self.__selected].state != ImageButton.DISABLED):
            self.buttons[self.__selected].state = ImageButton.SELECTED
        
        _p = self.buttons[self.__selected].pos
        self.selector.pos = [_p[0] - 5, _p[1] - 5]


#end of MainMenuList