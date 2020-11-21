import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import game_functions as gf


def run_game():
    # Инициализация игры и создание экрана:
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    sb = ScoreBoard(ai_settings,screen,stats)
    pygame.display.set_caption(('Alien Invasion'))
    play_button = Button(ai_settings,screen,'Play')
    # Ship creation
    ship = Ship(ai_settings,screen)
    # Bullet group creation
    bullets = Group()
    # Aliens group creation
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # Alien Creation


    # Start the main loop for the game:
    while True:
        # Отслеживание событий на клаиватуре и мыши
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens, bullets)
        if stats.game_active:
            ship.update()
        gf.update_bullets(ai_settings,screen,stats,sb,ship, aliens, bullets)
        gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets,play_button)

run_game()


