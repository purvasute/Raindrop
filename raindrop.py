import pygame

from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        #Load the raindrop image

        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()

        #start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the raindrop's exact vertical position
        self.y = float(self.rect.y)


    def check_disappeared(self):
        """Check if drop has disappeared off the bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    