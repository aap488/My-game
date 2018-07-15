# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:02:40 2018

@author: aap48
"""

import sys
import pygame
from game_settings import MySettings
from my_character import Character
import my_functions as mf

# Initialize pygame functions.
pygame.init()

# Initialize instance of MySettings.
settings = MySettings()

# Create main surface and set dimensions.
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
# Label main window with caption.
pygame.display.set_caption('My game')

# Initialize instance of Character.
character = Character(screen, settings)

while True:
    
    # Check for keyevents and react.
    mf.check_events(character)
    
    # Set background color using RGB.
    screen.fill(settings.bg_color)
    
    # Update characters position.
    character.update_pos()
    
    # Render character.
    character.blit_char()
    
    # Render most recent screen.
    pygame.display.flip()