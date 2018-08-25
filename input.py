import pygame
# pylint: disable=no-member


class Input(object):

    EVENT_UP = "up"
    EVENT_DOWN = "down"
    EVENT_LEFT = "left"
    EVENT_RIGHT = "right"
    EVENT_NEXT = "enter"
    EVENT_BACK = "back"

    EVENT_2_KEYS = {
        EVENT_UP: [pygame.K_UP],
        EVENT_DOWN: [pygame.K_DOWN],
        EVENT_NEXT: [pygame.K_RETURN, pygame.K_SPACE],
        EVENT_BACK: [pygame.K_ESCAPE],
        EVENT_LEFT: [pygame.K_LEFT],
        EVENT_RIGHT: [pygame.K_RIGHT],
    }

    def __init__(self):

        self.keys = {
            Input.EVENT_UP: False,
            Input.EVENT_DOWN: False,
            Input.EVENT_LEFT: False,
            Input.EVENT_RIGHT: False,
            Input.EVENT_NEXT: False,
            Input.EVENT_BACK: False,
        }
        self.__envents = dict()

        pass

    def collectEvents(self, event):
        _ext_type = None

        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            for key in Input.EVENT_2_KEYS:
                if(event.key in Input.EVENT_2_KEYS[key]):

                    if(event.type == pygame.KEYDOWN):
                        _ext_type = key
                    self.keys[key] = event.type == pygame.KEYDOWN
                    break

        if(_ext_type == None):
            return

        # try:
        for _e in self.__envents[_ext_type]:
            _e()
        #    print(_e)
        # except:
        #    print("Error execute method")
        #    pass

    def addEvent(self, eventType, event):

        if(eventType in self.__envents):
            self.__envents[eventType].append(event)
        else:
            self.__envents[eventType] = [event]

    # end of addEvent

    def delEvent(self, eventType, event):

        if(eventType in self.__envents):
            try:
                self.__envents[eventType].remove(event)
                return True
            except:
                return False

    # end of delEvent
