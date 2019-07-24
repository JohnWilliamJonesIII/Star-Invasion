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


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snek.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snek.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                snek.set_direction_right()

# Main Game Loop
is_playing = True
while is_playing:
    game_display.blit(game_display, (0, 0))

    game_display.fill(BACKGROUND_COLOR)
    pygame.draw.rect(game_display, (LIME_GREEN), pygame.Rect(50, 50, 20, 20))

    #score_text = score_font.render(str(snek.score), False, (255, 255, 255))

    #game_display.blit(score_text, (0, 0))

    #pygame.display.set_caption('STAR INVASION | Score = ' + str(snek.score) + ' | Press P to pause')

    pygame.display.update()

    clock.tick(GAME_FPS)

pygame.display.quit() # For Mac
pygame.quit()