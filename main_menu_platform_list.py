import os
import pygame
import math

from pygame.sprite import Group
from image_button import ImageButton
from sprite import Sprite


class MainMenuPlatformList(Group):

    def __init__(self, game):
        Group.__init__(self)

        self.need_draw = True
        self.__selected = 0
        self.game = game
        self.slide_time = 0.1
        self.target_selector_pos = [0, 0]

        self.selector = Sprite(pygame.image.load(
            game.assets["SELECTOR"]).convert_alpha())

        self.createButtons()
        self.add(self.selector)
        self.add(*self.buttons)

        self.last_rect = pygame.Rect(0,0,0,0)

        self.selected = 0
    # end of init

    def update(self, dt):
        Group.update(self, dt)

        delta = dt / self.slide_time

        fp = self.selector.pos

        if(abs(fp[1] - self.target_selector_pos[1]) > 1):
            fp[1] = fp[1] * (1 - delta) + self.target_selector_pos[1] * delta
            self.selector.pos = fp

            self.need_draw = True
        else:
            self.selector.pos = self.target_selector_pos

    # end of update

    def draw(self, renderer):
        Group.draw(self, renderer)

        rects = list(self.spritedict.values())
        self.last_rect =  rects[0].unionall(rects)
        
        self.need_draw = False

    # end of draw

    def createButtons(self):
        _list = self.game.assets["ICONS"]
        self.buttons = list()

        OFFSET = [50, 90]
        SPASE = 8

        for idx, item, in enumerate(_list):
            _gen = [item['img'].format(_suff) for _suff in [
                'n', 'a', 'd'] if os.path.isfile(item['img'].format(_suff))]
            _imgs = [pygame.image.load(img) for img in _gen]

            _btn = ImageButton(_imgs)
            _btn.pos = [OFFSET[0], OFFSET[1] +
                        (_btn.rect.height + SPASE) * idx]
            self.buttons.append(_btn)

        self.target_selector_pos = self.selector.pos = [
            self.buttons[0].pos[0] - 5, self.buttons[0].pos[1] - 5]

        # self.add(*self.buttons)

    # end of createButtons

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, id):

        if(id == self.selected):
            return

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
        self.target_selector_pos = [_p[0] - 5, _p[1] - 5]

        self.need_draw = True

# end of MainMenuList
