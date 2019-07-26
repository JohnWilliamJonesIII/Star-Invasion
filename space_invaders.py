# Beginning of Code
import pygame
from hero import Hero
from fleet import Fleet

pygame.init()
# Media Files
player_image = pygame.image.load('media/si-player.gif')
bullet_image = pygame.image.load('media/si-bullet.gif')
enemy_image = pygame.image.load('media/si-enemy.gif')
bullet_sound = pygame.mixer.Sound('media/si-laser.wav')
explosion_sound = pygame.mixer.Sound('media/si-explode.wav')

##Game Settings##
# Colours
BACKGROUND_COLOR = (0, 0, 0)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIME_GREEN = (0, 255, 0)
FOREST_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
# Game Border/Margin Settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3

GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH
GAME_FPS = 40


clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Comic Sans', 22, True)
title_font = pygame.font.SysFont('Comic Sans', 20, True)
title_press_start_font = pygame.font.SysFont('Comic Sans', 22, True)
title_copyright_font = pygame.font.SysFont('Comic Sans', 20, True)
pygame.display.set_caption(' STAR INVASION ')

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                bullet_sound.play()
                hero.shoot(bullet_image)
            elif event.key == pygame.K_p:
                pause_game() 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()
            

def show_background():
    game_display.blit(game_display, (0, 0))
    game_display.fill(BACKGROUND_COLOR)
    pygame.draw.rect(game_display, (FOREST_GREEN), (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, (BACKGROUND_COLOR), (GAME_LEFT_WALL, GAME_TOP_WALL, WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH, WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

def pause_game():
    game_is_paused = True
    while game_is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_paused = False
                hero.is_alive = False
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_p:
                     game_is_paused = False
        clock.tick(GAME_FPS)
            

hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())

fleet = Fleet(5, 7, 2, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)

# Main Game Loop
while hero.is_alive:

    handle_events()

    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    hero.handle_bullet_wall_collision(GAME_TOP_WALL)

    for bullet in hero.bullets_fired:
        for ship in fleet.ships:
            if bullet.has_collided_with(ship):
                explosion_sound.play()
                bullet.is_alive = False
                ship.is_alive = False
                hero.score += 1
    
    fleet.remove_dead_ships()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    fleet.move_over()
    hero.move_all_bullets()

    show_background()
    hero.show(game_display)
    fleet.show(game_display)
    hero.show_all_bullets(game_display)
    

    #score_text = score_font.render(str(snek.score), False, (255, 255, 255))

    #game_display.blit(score_text, (0, 0))

    score_text = score_font.render(str(hero.score), False, (255, 255, 255))
    game_display.blit(score_text, (0, 0))
    pygame.display.set_caption('STAR INVASION | Score = ' + str(hero.score) + ' | Press P to pause')

    pygame.display.update()

    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()