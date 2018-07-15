# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:18:07 2018

@author: aap48
"""

class MySettings():
    
    """ Create a settings class for game. """
    
    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 206, 203)
        
        # Character settings.
        self.character_speed = .25