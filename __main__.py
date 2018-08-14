#! /usr/bin/python3
# pylint: disable=no-member

from game import Game

if __name__ == "__main__":
    app = Game()

    while 1:
        app.update()