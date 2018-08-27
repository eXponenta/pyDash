import pygame
import os
import input

from background import Background
from text_sprite import TextSprite
from pygame.sprite import Group
from main_menu_platform_list import MainMenuPlatformList
from sprite import Sprite
from file_list import FileList
from item_constructor import BaseItemConstructor, DirlistItemConstructor, RomDataItemsConstructor
from executor import Executor, RomExecutor


class MainStage(Group):

    app = None
    SELECTRO_ICONS = "icons"
    SELECTOR_LIST = "list"

    def __init__(self, game):
        Group.__init__(self)

        self.game = game
        self.need_draw = True

        self.key_test_period = 0.25
        self.__tick = 0

        self.rom_executor = RomExecutor()
        self.game_list = RomDataItemsConstructor(
            game.app.config.get("PATHS", "gamelist"))

        self.sdcard_constructor = DirlistItemConstructor(
            game.app.config.get("PATHS", "sdcard"), Executor())

        self.all_constructors = [
            BaseItemConstructor(),  # for favorites
            self.game_list.getConsole("GEN"),  # for gen
            self.game_list.getConsole("SMS"),  # for sms
            self.game_list.getConsole("NES"),  # for nes
            self.game_list.getConsole("SNES"),  # for snes
            self.sdcard_constructor,
            None
        ]

        self.item_constructor = self.all_constructors[0]

        self.bg = Background(game)

        self.title_text = TextSprite("", game.assets["TITLE_FONT"])
        self.update_title_text(self.game.assets["ICONS"][0]['title'])

        self.title_text.centered = True

        self.platform = MainMenuPlatformList(game)
        self.file_list = FileList(game, self.item_constructor)
        self.file_list.deselect_all()

        self.selector_state = MainStage.SELECTRO_ICONS

        #self.add(*[self.bg, self.title_text, self.platform, self.file_list])

        game.app.input.addEvent(input.Input.EVENT_DOWN, self.nextItem)
        game.app.input.addEvent(input.Input.EVENT_UP, self.lastItem)
        game.app.input.addEvent(input.Input.EVENT_NEXT, self.select)
        game.app.input.addEvent(input.Input.EVENT_BACK, self.selectBack)

        game.app.input.addEvent(input.Input.EVENT_LEFT, self.last10Item_list)
        game.app.input.addEvent(input.Input.EVENT_RIGHT, self.next10Item_list)

        self.parts = [self.title_text, self.platform, self.file_list]

    # end of init

    def next10Item_list(self):
        if (self.selector_state != MainStage.SELECTOR_LIST):
            return
        self.file_list.selected = (1 + self.file_list.selected //
                                   self.file_list.ITEMS_PER_PAGE) * self.file_list.ITEMS_PER_PAGE

    def last10Item_list(self):
        if (self.selector_state != MainStage.SELECTOR_LIST):
            return
        self.file_list.selected = (-1 + self.file_list.selected //
                                   self.file_list.ITEMS_PER_PAGE) * self.file_list.ITEMS_PER_PAGE

    def nextItem(self):
        self.lastNextItem(1)
    # end of nextItem

    def lastItem(self):
        self.lastNextItem(-1)

    def lastNextItem(self, dir):
        self.__tick = 0
        if(self.selector_state == MainStage.SELECTRO_ICONS):
            self.platform.selected += dir
            _title = self.game.assets["ICONS"][self.platform.selected]['title']
            self.update_title_text(_title)

            self.item_constructor = self.all_constructors[self.platform.selected]
            self.file_list.set_items(self.item_constructor,
                                     not isinstance(self.item_constructor, DirlistItemConstructor))
            self.file_list.deselect_all()
        else:
            self.file_list.selected += dir

    # end of lastNextItem

    def select(self):
        if(self.selector_state == MainStage.SELECTRO_ICONS):
            self.selector_state = MainStage.SELECTOR_LIST
            self.file_list.selected = 0
            return

        if (self.selector_state == MainStage.SELECTOR_LIST):

            if(isinstance(self.item_constructor, DirlistItemConstructor)):
                if self.item_constructor.next(self.file_list.selected):
                    self.file_list.set_items(self.item_constructor)
            else:
                rom = self.item_constructor.all[self.file_list.selected]
                print(self.rom_executor.exec(rom))

    # end of select

    def selectBack(self):

        if (self.selector_state == MainStage.SELECTOR_LIST):
            self.selector_state = MainStage.SELECTRO_ICONS
            self.file_list.deselect_all()

    # end of select

    def update_title_text(self, text):

        self.title_text.set_text(text)
        self.title_text.pos = [
            455 - self.title_text.rect.w / 2, 70 - self.title_text.rect.h / 2]

    # end of update_title_text

    def update(self, dt):

        Group.update(self, dt)
        self.platform.update(dt)

        self.__tick += dt
        if(self.__tick >= self.key_test_period):
            self.__tick = 0
            if(self.game.app.input.keys[input.Input.EVENT_UP]):
                self.lastItem()
            if(self.game.app.input.keys[input.Input.EVENT_DOWN]):
                self.nextItem()

    # end of update

    def draw(self, renderer):
        #Group.draw(self, renderer)

        if(self.need_draw):
            self.bg.draw(renderer)
            self.need_draw = False

        _updated = False
        
        for p in self.parts:
            if(p.need_draw):

                rs = p.last_rect
                if(not isinstance(rs, list)):
                    rs = [rs]
                for r in rs:
                    renderer.blit(self.bg.image, r, r)

                p.draw(renderer)

                _updated = True
        
        return _updated

    # end of draw

# end of MainStage
