# Beginning of Code
import pygame

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

x_coordinate = 50
y_coordinate = 100

def handle_events():
    global x_coordinate, y_coordinate, is_playing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_coordinate -= 10
            elif event.key == pygame.K_RIGHT:
                x_coordinate += 10


# Main Game Loop
is_playing = True
while is_playing:

    handle_events()

    game_display.blit(game_display, (0, 0))

    game_display.fill(BACKGROUND_COLOR)
    pygame.draw.rect(game_display, (LIME_GREEN), pygame.Rect(x_coordinate, y_coordinate, 20, 20))

    #score_text = score_font.render(str(snek.score), False, (255, 255, 255))

    #game_display.blit(score_text, (0, 0))

    #pygame.display.set_caption('STAR INVASION | Score = ' + str(snek.score) + ' | Press P to pause')

    pygame.display.update()

    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()