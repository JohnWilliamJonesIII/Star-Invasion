# Beginning of Code
import os
import sys
import pygame
import random
from os import path
from pygame.locals import *
from pixel_planet import Pixel_Planet
from truecoderslogo import Truecoders_Logo
from hero import Hero
from fleet import Fleet
from enemy import Enemy
from ultra_bullet import Ultra_Bullet
from hero_shield import Hero_Shield
from pause_music import Pause_Music
from life_bar import Life_Bar
from life_bars import Life_Bars

pygame.init()
pygame.mixer.init()
# Media Files
## Game Object Images
truecoders_logo_image = pygame.image.load('media/truecoderslogo.gif')
pixel_planet_image = pygame.image.load('media/pixelplanet.jpeg')
player_image = pygame.image.load('media/si-player.gif')
bullet_image = pygame.image.load('media/si-bullet.gif')
ultra_bullet_image = pygame.image.load('media/si-ultrabullet.gif')
laser_image = pygame.image.load('media/smallmeteor.png')
hero_shield_image = pygame.image.load('media/si-heroshield.gif')
enemy_image = pygame.image.load('media/si-enemy.gif')
hero_first_life_image = pygame.image.load('media/si-life1.gif')
## Sound effects and Music
game_pause_sound = pygame.mixer.Sound('media/gamepause.wav')
game_level_win_sound = pygame.mixer.Sound('media/winlevel.wav')
game_lose_level_sound = pygame.mixer.Sound('media/losegame.wav')
enemy_death_sound = pygame.mixer.Sound('media/enemydead.wav')
hero_shield_sound = pygame.mixer.Sound('media/heroshield.wav')
hero_shield_dead_sound = pygame.mixer.Sound('media/heroshielddead.wav')
hero_damaged_sound = pygame.mixer.Sound('media/hero_damaged.wav')
laser_bullet_collision_sound = pygame.mixer.Sound('media/bulletlasercollision.wav')
bullet_sound = pygame.mixer.Sound('media/bullet.wav')
ultra_bullet_sound = pygame.mixer.Sound('media/ultrabullet.wav')
explosion_sound = pygame.mixer.Sound('media/explosion.wav')
background_music_tracks = ['media/rocketman.ogg', 'media/spaceoddity.ogg', 'media/stairwaytoheaven.ogg']
current_background_music_track = 0 
music_track_over = pygame.USEREVENT
pygame.mixer.music.set_endevent(music_track_over)
def play_music(path):
    songs = []
    for filename in os.listdir(path):
        if filename.endswith('.ogg'):
            songs.append(os.path.join(path, filename))
    return songs
pause_music = Pause_Music()

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

##Game Settings##
# Colours
BACKGROUND_COLOR = (0, 0, 0)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIME_GREEN = (0, 255, 0)
FOREST_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREY = (123, 123, 123)
RED = (255, 0, 0)
# Game Border/Margin Settings
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
GAME_SIZE = WINDOW_HEIGHT * WINDOW_WIDTH
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3
FLEET_COLUMN = 10
FLEET_ROW = 2
FLEET_SIZE = FLEET_COLUMN * FLEET_ROW
FLEET_SPEED = 1
LEVEL_SCORE = 1
GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH
GAME_FPS = 40
LIFE_BAR_COLUMN = 5
LIFE_BAR_ROW = 1
LIFE_BAR_SIZE = LIFE_BAR_COLUMN * LIFE_BAR_ROW
START_GAME = True
GAME_OVER = False
# Arrays for animated star background
star_field_slow = []
star_field_medium = []
star_field_fast = []
for slow_stars in range(50):
    star_x_coordinate = random.randrange(0, WINDOW_WIDTH)
    star_y_coordinate = random.randrange(0, WINDOW_HEIGHT)
    star_field_slow.append([star_x_coordinate, star_y_coordinate])
for medium_stars in range(35):
    star_x_coordinate = random.randrange(0, WINDOW_WIDTH)
    star_y_coordinate = random.randrange(0, WINDOW_HEIGHT)
    star_field_medium.append([star_x_coordinate, star_y_coordinate])
for fast_stars in range(15):
    star_x_coordinate = random.randrange(0, WINDOW_WIDTH)
    star_y_coordinate = random.randrange(0, WINDOW_HEIGHT)
    star_field_fast.append([star_x_coordinate, star_y_coordinate])

clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
level_font = pygame.font.SysFont('Comic Sans', 40, True)
level_equals_font = pygame.font.SysFont('Comic Sans', 20, True)
score_font = pygame.font.SysFont('Comic Sans', 20, True)
score_equals_font = pygame.font.SysFont('Comic Sans', 20, True)
hero_lives_font = pygame.font.SysFont('Comic Sans', 20, True)
title_font = pygame.font.SysFont('Comic Sans', 70, True)
title_press_start_font = pygame.font.SysFont('Comic Sans', 35, True)
title_copyright_font = pygame.font.SysFont('Comic Sans', 25, True)
pygame.display.set_caption(' STAR INVASION ')

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            START_GAME = False
        elif event.type == pygame.KEYDOWN:
            # Move Left
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            # Move Right
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            # Shoot Bullet
            elif event.key == pygame.K_UP:
                bullet_sound.play()
                hero.shoot(bullet_image)
            # Shoot UltraBullet
            elif event.key == pygame.K_DOWN:
                if hero.score > 5:
                    hero.score -= 5
                    ultra_bullet_sound.play()
                    hero.shoot_ultra_bullet(ultra_bullet_image)
            # Debug Enemy Projectile 
            elif event.key == pygame.K_u:
                bullet_sound.play()
                fleet.shoot(laser_image)
            # Place Down Shield
            elif event.key == pygame.K_SPACE:
                if hero.score > 5:
                    hero.score -= 5
                    hero_shield_sound.play()
                    hero.place_down_shield(hero_shield_image)
            # Pause Game
            elif event.key == pygame.K_p:
                game_pause_sound.play()
                pause_game() 
            # Pause Music
            elif event.key == pygame.K_q:
                pause_music.toggle()
            # Music Tracks
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                current_background_music_track = 0 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                current_background_music_track = 1 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                current_background_music_track = 2 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
        elif event.type == pygame.KEYUP:
            # Reset Hero Movement
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()
            # Cycling Music Tracks/ Not functional
        elif event.type == music_track_over:
                current_background_music_track = (current_background_music_track + 1) % len(songs)  # Go to the next song (or first if at last).
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()

# Defining Game Object classes
truecoders_logo = Truecoders_Logo(truecoders_logo_image, 230, 200)
pixel_planet = Pixel_Planet(pixel_planet_image, -30, 575)
hero = Hero(player_image, 225, GAME_BOTTOM_WALL - player_image.get_height())
fleet = Fleet(FLEET_ROW, FLEET_COLUMN, 1, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)
hero_shield = Hero_Shield(hero_shield_image, hero.xcor, 500)
ultra_bullet = Ultra_Bullet(ultra_bullet_image, hero.xcor, 535)
hero_life_bars = Life_Bars(LIFE_BAR_ROW, LIFE_BAR_COLUMN, hero_first_life_image, GAME_LEFT_WALL + 125, 1)

## Main Menu
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText
songs = play_music(path = '/Users/John/Source/Repos/SpaceInvadersMarkVIII/Media')
current_background_music_track = 1 # The current song to load
pygame.mixer.music.load(songs[current_background_music_track])
pygame.mixer.music.play()
current_background_music_track += 1
Show_Menu_Screen = True
Selected_Option = "PLAY"
while Show_Menu_Screen: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and Selected_Option == "QUIT":
                Selected_Option = "PLAY"
            elif event.key == pygame.K_UP and Selected_Option == "PLAY":
                Selected_Option = "QUIT"
            elif event.key == pygame.K_DOWN and Selected_Option == "PLAY":
                Selected_Option = "QUIT"
            elif event.key == pygame.K_DOWN and Selected_Option == "QUIT":
                Selected_Option = "PLAY"
            elif event.key == pygame.K_q:
                pause_music.toggle()
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                current_background_music_track = 0 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                current_background_music_track = 1 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                current_background_music_track = 2 # The current song to load
                pygame.mixer.music.load(songs[current_background_music_track])
                pygame.mixer.music.play()
            if event.key == pygame.K_RETURN:
                if Selected_Option == "PLAY":
                    Show_Menu_Screen = False
                    show_title_screen = True
                if Selected_Option == "QUIT":
                    pygame.quit()
                    quit()

    # Main Menu UI
    game_display.blit(game_display, (0, 0))
    game_display.fill(BACKGROUND_COLOR)
    # title = text_format("   | STAR INVASION |", 'Comic Sans', 70, WHITE)
    if Selected_Option == "PLAY":
        text_start = text_format("PLAY", 'Comic Sans', 40, WHITE)
    else:
        text_start = text_format("PLAY", 'Comic Sans', 40, GREY)
    if Selected_Option == "QUIT":
        text_quit = text_format("QUIT", 'Comic Sans', 40, WHITE)
    else:
        text_quit = text_format("QUIT", 'Comic Sans', 40, GREY)
    for star in star_field_slow:
        star[1] += 1
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, GREY, star, 3)
    for star in star_field_medium:
        star[1] += 4
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, GREY, star, 2)
    for star in star_field_fast:
        star[1] += 8
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, GREY, star, 1)
    
    start_rect = text_start.get_rect()
    quit_rect = text_quit.get_rect()
    game_display.blit(text_start, (WINDOW_WIDTH/2 - (start_rect[2]/2), 300))
    game_display.blit(text_quit, (WINDOW_WIDTH/2 - (quit_rect[2]/2), 360))
    title_text = title_font.render('| STAR INVASION |', False, CYAN)
    title_press_start_text = title_press_start_font.render('PRESS ENTER TO START', False, RED)
    title_copyright_text = title_copyright_font.render('©2019 JOHN WILLIAM JONES III | TRUECODERS', False, BLUE)
    pixel_planet.show(game_display)
    hero.show(game_display)
    truecoders_logo.show(game_display)
    fleet.show(game_display)
    fleet.move_over()
    fleet.title_screen_fleet_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    game_display.blit(title_text, (0, 150))
    game_display.blit(title_press_start_text, (85, 250))
    game_display.blit(title_copyright_text, (35, 500)) 
    pygame.display.flip()
    clock.tick(GAME_FPS)  

def show_background():
    game_display.blit(game_display, (0, 0))
    game_display.fill(BACKGROUND_COLOR)
    pygame.draw.rect(game_display, (BLACK), (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, (BACKGROUND_COLOR), (GAME_LEFT_WALL, GAME_TOP_WALL, WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH, WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))
    for star in star_field_slow:
        star[1] += 1
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, GREY, star, 3)
    for star in star_field_medium:
        star[1] += 4
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, CYAN, star, 2)       
    for star in star_field_fast:
        star[1] += 8
        if star[1] > WINDOW_HEIGHT:
            star[0] = random.randrange(0, WINDOW_WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(game_display, YELLOW, star, 1)

def pause_game():
    game_is_paused = True
    while game_is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_paused = False
                START_GAME = False
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_p:
                     game_is_paused = False
        clock.tick(GAME_FPS)  

# Main Game Loop
while START_GAME:
    handle_events()
    ## | Collision |
    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    hero.handle_bullet_wall_collision(GAME_TOP_WALL)
    fleet.handle_laser_wall_collision(GAME_BOTTOM_WALL)
    ## Projectile Collision
    # Hero Projectiles
    for bullet in hero.bullets_fired:
        for ship in fleet.ships:
            if bullet.has_collided_with(ship):
                enemy_death_sound.play()
                bullet.is_alive = False
                ship.is_alive = False
                hero.score += 1    
    for ultra_bullet in hero.ultra_bullets_fired:
        for ship in fleet.ships:
            if ultra_bullet.has_collided_with(ship):
                enemy_death_sound.play()
                ultra_bullet.is_alive = False
                ship.is_alive = False
                hero.score += 1
    # Fleet Projectiles
    if random.randrange(25) == 0:
        fleet.shoot(laser_image)
    for laser in fleet.lasers_fired:
        if laser.has_collided_with(hero):
            if hero.first_life == True:
                laser.is_alive = False
                hero_damaged_sound.play()
                for bar in hero_life_bars.bars:
                    bar.is_alive = False
                hero.first_life = False
                hero.second_life = True
            elif hero.second_life == True: 
                pause_music.toggle()
                clock.tick(15)
                game_lose_level_sound.play()
                clock.tick(.7)
                laser.is_alive = False
                START_GAME = False
                if START_GAME == False:
                    run("Star-Invasion.py")
        elif laser.has_collided_with(ultra_bullet):
            laser_bullet_collision_sound.play()
            laser.is_alive = False
        for hero_shield in hero.shields_placed:
            if laser.has_collided_with(hero_shield):
                hero_shield.is_alive = False
                hero_shield_dead_sound.play()
                laser.is_alive = False
            elif ultra_bullet.has_collided_with(hero_shield):
                hero_shield.is_alive = False
                ultra_bullet.is_alive = False
                hero_shield_dead_sound.play()
        for bullet in hero.bullets_fired:
            if laser.has_collided_with(bullet):
                laser_bullet_collision_sound.play()
                hero.score += 1
                laser.is_alive = False
                bullet.is_alive = False
    ## Fleet Collision
    for ship in fleet.ships:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                fleet.shoot(laser_image)
        if ship.has_collided_with(hero):
            pause_music.toggle()
            clock.tick(.7)
            START_GAME = False
    ## | Levels |
    if len(fleet.ships) == 0:
        game_level_win_sound.play()
        clock.tick(.7)
        hero.remove_bullets_after_level_change()
        hero.remove_ultra_bullets_after_level_change()
        fleet.remove_lasers_after_level_change()
        FLEET_ROW = FLEET_ROW + 1
        FLEET_SPEED = FLEET_SPEED + .50
        fleet = Fleet(FLEET_ROW, FLEET_COLUMN, FLEET_SPEED, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)
        LEVEL_SCORE += 1
        if LEVEL_SCORE > 10:
            clock.tick(.7)
            fleet = Fleet(0, 0, FLEET_SPEED, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)
            START_GAME = False
            
    # Removing dead instances of classes
    fleet.remove_dead_ships()
    hero.remove_dead_shields()
    hero.remove_dead_ultra_bullets()
    hero.remove_dead_bullets()
    hero_life_bars.remove_dead_life_bars()
    # Calling Game Object Move methods
    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    fleet.move_over()
    hero.move_all_bullets()
    hero.move_all_ultra_bullets()
    fleet.move_all_lasers()
    # Display Background and Game Objects
    show_background()
    pixel_planet.show(game_display)
    hero.show(game_display)
    fleet.show(game_display)
    fleet.show_all_lasers(game_display)    
    hero.show_all_bullets(game_display)
    hero.show_all_ultra_bullets(game_display)
    hero.show_all_hero_shields(game_display)
    hero_life_bars.show(game_display)

    # Display score and UI
    score_text = score_font.render(str(hero.score), False, WHITE)
    game_display.blit(score_text, (60, 1))
    score_equals_text = score_equals_font.render('Score = ', False, WHITE)
    game_display.blit(score_equals_text, (0, 1))
    level_text = level_font.render(str(LEVEL_SCORE), False, WHITE)
    game_display.blit(level_text, (460, 1))
    level_equals_text = level_equals_font.render('Level: ', False, WHITE)
    game_display.blit(level_equals_text, (400, 8))
    hero_lives_text = hero_lives_font.render('Lives: ', False, WHITE)
    game_display.blit(hero_lives_text, (100, 1))
    pygame.display.set_caption('| STAR INVASION |Score = ' + str(hero.score) + ' | Press P to pause')
    pygame.display.update()
    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()
quit()