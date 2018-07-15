# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 03:01:14 2018

@author: aap48
"""

import sys
import pygame

def check_keydown(event, character):
    """ Check for keypresses. """
    if event.key == pygame.K_LEFT:
        character.moving_left = True
    
    elif event.key == pygame.K_RIGHT:
        character.moving_right = True

def check_keyup(event, character):
    " Check for key releases. """
    if event.key == pygame.K_LEFT:
        character.moving_left = False
        
    elif event.key == pygame.K_RIGHT:
        character.moving_right = False

def check_events(character):
    """ Check for keypresses or mouse inputs. """
    for event in pygame.event.get():
        
        # Respond to closing game screen.
        if event.type == pygame.QUIT:
            sys.exit()
                    
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, character)
            
        elif event.type == pygame.KEYUP:
            check_keyup(event, character)