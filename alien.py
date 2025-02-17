import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    # Solo alien class
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
    # Alien image loading
        self.image = pygame.image.load('images/alien3.png',)
        self.rect = self.image.get_rect()
        # Every new alien will appear at the left top part of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    def blitme(self):
        # Shows current alien position
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        # Return True if alien is at the screen side
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x
