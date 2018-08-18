import pygame
import os
import input

from background import Background
from text_sprite import TextSprite
from pygame.sprite import Group
from main_menu_platform_list import MainMenuPlatformList
from sprite import Sprite
from file_list import FileList

class BaseItemConstructor(object):
    def __init__(self):
        self.level = ""
        self.all = [self.level + str(idx) for idx in range(124)]

    def next(self, id):
        self.level += str(id) + ":"
        self.all = [self.level + str(idx) for idx in range(124)]
    

class FileItemConstructor(BaseItemConstructor):
    
    def __init__(self, startPath):
        BaseItemConstructor.__init__(self)
       
        self.set_path(startPath)
    #enf of init

    def collect(self):

        self.all = ["../"]
        
        try:
            _path_and_dir = list(os.listdir(self.currentPath))
            self.all += list(filter(lambda x: os.path.isdir(self.currentPath +'/' + x), _path_and_dir))
            self.all += list(filter(lambda x: os.path.isfile(self.currentPath + '/' + x), _path_and_dir))
        
        except Exception as e:
            print(e)
        
    def set_path(self, path):
        self.currentPath = path
        self.collect()

    def next(self,id):
        self.set_path(self.currentPath + "/" + self.all[id])    

class MainStage(Group):

    app = None
    SELECTRO_ICONS = "icons"
    SELECTOR_LIST = "list"

    def __init__(self, game):
        Group.__init__(self)

        self.game = game

        self.all_constructors = [
            BaseItemConstructor(), # for favorites
            BaseItemConstructor(), # for gen
            BaseItemConstructor(), # for sms
            BaseItemConstructor(), # for nes
            BaseItemConstructor(), # for snes
            FileItemConstructor("C:/"),
            None
        ]

        self.item_constructor = self.all_constructors[0]

        self.bg = Background(game)
        
        self.title_text = TextSprite("", game.assets["TITLE_FONT"])
        self.update_title_text(self.game.assets["ICONS"][0]['title'])

        self.title_text.centered = True

        self.platform = MainMenuPlatformList(game)
        self.file_list = FileList(game, self.item_constructor)

        self.selector_state = MainStage.SELECTRO_ICONS

        self.add(*[self.bg, self.title_text, self.platform, self.file_list])

        
        game.app.input.addEvent(input.Input.EVENT_DOWN, self.nextItem)
        game.app.input.addEvent(input.Input.EVENT_UP, self.lastItem)
        game.app.input.addEvent(input.Input.EVENT_NEXT, self.select)
        game.app.input.addEvent(input.Input.EVENT_BACK, self.selectBack)
        
    #end of init

    def nextItem(self):
        self.lastNextItem(1)
    #end of nextItem
    
    def lastItem(self):        
        self.lastNextItem(-1)
    
    def lastNextItem(self, dir):
        if(self.selector_state == MainStage.SELECTRO_ICONS):
            self.platform.selected += dir
            _title = self.game.assets["ICONS"][self.platform.selected]['title']
            self.update_title_text(_title)
            
            self.item_constructor = self.all_constructors[self.platform.selected]
            self.file_list.set_items(self.item_constructor)

        else:
            self.file_list.selected +=dir
    
    #end of lastNextItem

    def select(self):
        if(self.selector_state == MainStage.SELECTRO_ICONS):
            self.selector_state = MainStage.SELECTOR_LIST
            return

        if (self.selector_state == MainStage.SELECTOR_LIST):
            self.item_constructor.next(self.file_list.selected)
            self.file_list.set_items(self.item_constructor)
    
    #end of select

    def selectBack(self):

        if (self.selector_state == MainStage.SELECTOR_LIST):
            self.selector_state = MainStage.SELECTRO_ICONS
    
    #end of select

    def update_title_text(self, text):
        
        self.title_text.set_text(text)
        self.title_text.pos = [455 - self.title_text.rect.w / 2,70 - self.title_text.rect.h / 2]

    #end of update_title_text

    def update(self, dt):

        Group.update(self, dt)

    #end of update

    def draw(self, renderer):
        
        Group.draw(self, renderer)

    #end of draw

#end of MainStage