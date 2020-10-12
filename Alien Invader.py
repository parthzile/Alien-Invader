import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #Provide required bg settings for Pygame to run
    pygame.init()

    #Settings and Screen object
    ai_settings = Settings()

    #Scree size setting
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #Title bar setting
    pygame.display.set_caption("Alien Invader")

    #Make the Play Button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance  to store game statistics and create a acoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship, a group of bullets, & a group of alliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #Create teh fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship,  aliens)

    #Bg color setting
    bg_color = ai_settings.bg_color

    #Make an alien
    alien = Alien(ai_settings, screen)


    while True:
        #If the game freeze look at the main while loop.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()