# Beginning of Code
import pygame

# Media Files
player_image = pygame.image.load('si-player.gif')

APPLE_COLOR = (255, 25, 55)
BACKGROUND_COLOR = (0, 0, 0)
YELLOW = (255, 255, 0)
LIME_GREEN = (0, 255, 0)
FOREST_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GAME_FPS = 40

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((400, 600))
score_font = pygame.font.SysFont('Comic Sans', 22, True)
title_font = pygame.font.SysFont('Comic Sans', 20, True)
title_press_start_font = pygame.font.SysFont('Comic Sans', 22, True)
title_copyright_font = pygame.font.SysFont('Comic Sans', 20, True)
pygame.display.set_caption(' STAR INVASION ')

x_coordinate = 200
y_coordinate = 575
should_move_right = False
should_move_left = False

def handle_events():
    global x_coordinate, y_coordinate, is_playing, should_move_left, should_move_right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                should_move_left = True
                should_move_right = False
            elif event.key == pygame.K_RIGHT:
                should_move_right = True
                should_move_left = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                should_move_left = False
            elif event.key == pygame.K_RIGHT:
                should_move_right = False


# Main Game Loop
is_playing = True
while is_playing:

    handle_events()
    if should_move_right:
        x_coordinate += 10
    elif should_move_left:
        x_coordinate -= 10

    game_display.blit(game_display, (0, 0))

    game_display.fill(BACKGROUND_COLOR)
    game_display.blit(player_image, (x_coordinate, y_coordinate))

    #score_text = score_font.render(str(snek.score), False, (255, 255, 255))

    #game_display.blit(score_text, (0, 0))

    #pygame.display.set_caption('STAR INVASION | Score = ' + str(snek.score) + ' | Press P to pause')

    pygame.display.update()

    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()