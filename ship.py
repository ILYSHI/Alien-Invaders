import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        # Инициализирует корабль и задает его начальную позицию
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading ship image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship will appear at the bottom of the screen
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving float ship coordinate:
        self.center = float(self.rect.centerx)
        # Movement FLAG
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            # Updating center NOT rect.centerx!
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor
        # Updating rect.centerx
        self.rect.centerx = self.center
    def blitme(self):
        # Drawing the ship in the current position
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
