# Beginning of Code
import pygame
from hero import Hero
from enemy import Enemy


# Media Files
player_image = pygame.image.load('media/si-player.gif')
bullet_image = pygame.image.load('media/si-bullet.gif')
enemy_image = pygame.image.load('media/si-enemy.gif')

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


pygame.init()
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
                hero.shoot(bullet_image)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()

hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())
enemies = []
enemies.append(Enemy(enemy_image, 30, 30))
enemies.append(Enemy(enemy_image, 60, 30))
enemies.append(Enemy(enemy_image, 90, 30))
enemies.append(Enemy(enemy_image, 120, 30))
enemies.append(Enemy(enemy_image, 150, 30))
enemies.append(Enemy(enemy_image, 30, 60))
enemies.append(Enemy(enemy_image, 60, 60))
enemies.append(Enemy(enemy_image, 90, 60))
enemies.append(Enemy(enemy_image, 120, 60))
enemies.append(Enemy(enemy_image, 150, 60))


# Main Game Loop
while hero.is_alive:

    handle_events()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)

    # Move each enemy down and change its direction if it has hit a wall.
    for enemy in enemies:
        if enemy.collided_with_left_wall(GAME_LEFT_WALL):
            # Move all enemies down and change all their directions
            for e in enemies:
                e.ycor += 10
                e.direction = 1
            break      
        if enemy.collided_with_right_wall(GAME_RIGHT_WALL):
            for e in enemies:
                e.ycor += 10
                e.direction = -1
            break


    # Move each enemy over based on its direction
    for enemy in enemies:
        enemy.xcor += 4 * enemy.direction
    ##for i in range (0, len(enemies))  ^--------------| Does the exact same thing as the for loop above 
        ##enemies[i].xcor += 10 * enemies[i].direction


    game_display.blit(game_display, (0, 0))

    game_display.fill(BACKGROUND_COLOR)

    #Borders
    pygame.draw.rect(game_display, (FOREST_GREEN), (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, (BACKGROUND_COLOR), (GAME_LEFT_WALL, GAME_TOP_WALL, WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH, WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

    hero.show(game_display)
    for enemy in enemies:
        enemy.show(game_display)

    for bullet in hero.bullets_fired:
        if bullet.collided_with_top_wall(GAME_TOP_WALL):
            bullet.is_alive = False

    hero.remove_dead_bullets()

    for bullet in hero.bullets_fired:
        bullet.move()
        bullet.show(game_display)

    #score_text = score_font.render(str(snek.score), False, (255, 255, 255))

    #game_display.blit(score_text, (0, 0))

    #pygame.display.set_caption('STAR INVASION | Score = ' + str(snek.score) + ' | Press P to pause')

    pygame.display.update()

    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()