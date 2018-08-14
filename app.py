#! /usr/bin/python3
# pylint: disable=no-member

import sys
import configparser

'''
Base App class
'''

class App(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        try:
            self.config.readfp(open('config.cfg'))
        except:
            self.config['DISPLAY'] = {'width':'704', 'height':'576', 'fullscreen':'false'}
            self.config.write(open('config.cfg', 'w'))