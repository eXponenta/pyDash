import pygame

import input

from background import Background
from text_sprite import TextSprite
from pygame.sprite import Group
from main_menu_platform_list import MainMenuPlatformList
from sprite import Sprite
from file_list import FileList

class BaseItemConstructor(object):
    def __init__(self):
        self.all = ['1', '2', '3', '4']
    

class MainStage(Group):

    app = None

    def __init__(self, game):
        Group.__init__(self)

        self.game = game
        self.item_constructor = BaseItemConstructor()

        self.bg = Background(game)
        
        
        self.title_text = TextSprite("", game.assets["TITLE_FONT"])
        self.update_title_text(self.game.assets["ICONS"][0]['title'])

        self.title_text.centered = True

        self.platform = MainMenuPlatformList(game)
        self.file_list = FileList(game, self.item_constructor)

        self.add(*[self.bg, self.title_text, self.platform, self.file_list])

        game.app.input.addEvent(input.Input.EVENT_DOWN, self.nextItem)
        game.app.input.addEvent(input.Input.EVENT_UP, self.lastItem)
        

    #end of init

    def nextItem(self):
        self.platform.nextItem()
        _title = self.game.assets["ICONS"][self.platform.selected]['title']
        self.update_title_text(_title)
    
    #end of nextItem
    
    def lastItem(self):
        self.platform.lastItem()
        _title = self.game.assets["ICONS"][self.platform.selected]['title']
        self.update_title_text(_title)

    #end of lastItem

    def update_title_text(self, text):
        
        self.title_text.set_text(text)
        self.title_text.pos = [455 - self.title_text.rect.w / 2,70 - self.title_text.rect.h / 2]

    #end of update_title_text

    def update(self, dt):
        Group.update(self, dt)

        pass

    #end of update

    def draw(self, renderer):
        Group.draw(self, renderer)

        #self.title_text.draw(renderer)
        #self.platform.draw(renderer)
        #self.file_list.draw(renderer)
    #end of draw

#end of MainStage