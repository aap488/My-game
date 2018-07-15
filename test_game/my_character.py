# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:40:16 2018

@author: aap48
"""

import pygame


class Character():
    
    """ Class for game character. """
    
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        
        # Load character image.
        self.image = pygame.image.load('images/character.png').convert_alpha()
        
        # Get the rectangle position of image.
        self.rect = self.image.get_rect()
        # Get the rectangle position of the screen.
        self.screen_rect = self.screen.get_rect()
        
        # Set character starting position using the screen position.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store the center of character to use to move character.
        self.center = float(self.rect.centerx)
        
        # Character moving flags.
        self.moving_left = False
        self.moving_right = False
        
        
    def update_pos(self):
        """ Updates character position. """
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.settings.character_speed
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.center -= self.settings.character_speed
        
        # Give the new position to the center value.
        self.rect.centerx = self.center
    
    def blit_char(self):
        """ Draws character to main surface. """
        self.screen.blit(self.image, self.rect)