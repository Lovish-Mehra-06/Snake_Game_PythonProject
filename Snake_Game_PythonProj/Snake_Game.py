import pygame
from pygame.locals import *
import random

pygame.init()

# RGB Values
white_c = 255, 255, 255
black_c = 0, 0, 0
red_c = 255, 0, 0
lightgreen_c = 14, 173, 14

# Creating window
screen_w = 900
screen_h = 600
gamescreen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Snake_Game_With Lovish")
Icon = pygame.image.load("snakeicon_Snake_Game.png")
pygame.display.set_icon(Icon)
font = pygame.font.SysFont(None, 55)


def score_on_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gamescreen.blit(screen_text, [x, y])


def plot_snk(gamescreen, black_c, snk_list, snakesize):
    for x, y in snk_list:
        pygame.draw.rect(gamescreen, black_c, [x, y, snakesize, snakesize])


# Game Loop
def game_loop():
    # Game specific variable
    exitgame = False
    gameover = False
    snake_x = 45
    snake_y = 45
    snake_velocity_x = 0
    snake_velocity_y = 0
    snakesize = 20
    fps = 30
    apple_x = random.randint(20, int(screen_w / 2))
    apple_y = random.randint(20, int(screen_h / 2))
    score = 0

    with open("highscore_file_Snake_Game.txt", "r")as f:
        highscorvar = f.read()

    clock = pygame.time.Clock()

    snk_list = []
    snk_length = 1

    while not exitgame:

        if gameover:
            with open("highscore_file_Snake_Game.txt", "w")as f:
                f.write(str(highscorvar))

            gamescreen.fill((22, 6, 59))
            score_on_screen("Game Over !   Press Spacebar to continue", white_c, 100, 100)

            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        exitgame = True

                    if event.key == K_SPACE:
                        game_loop()


                if event.type == pygame.QUIT:
                    exitgame = True

        else:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT or event.key == K_d:
                        snake_velocity_x = 10
                        snake_velocity_y = 0

                    if event.key == K_LEFT or event.key == K_a:
                        snake_velocity_x = -10
                        snake_velocity_y = 0

                    if event.key == K_UP or event.key == K_w:
                        snake_velocity_x = 0
                        snake_velocity_y = -10

                    if event.key == K_DOWN or event.key == K_s:
                        snake_velocity_x = 0
                        snake_velocity_y = 10

                    if event.key == K_ESCAPE:
                        exitgame = True

                    if event.key == K_z:
                        score += 1
                if event.type == pygame.QUIT:
                    exitgame = True

            snake_x = snake_x + snake_velocity_x
            snake_y = snake_y + snake_velocity_y

            if abs(snake_x - apple_x) < 12 and abs(snake_y - apple_y) < 12:
                score += 1
                apple_x = random.randint(20, screen_w)
                apple_y = random.randint(20, screen_h)
                snk_length += 5
                if score > int(highscorvar):
                    highscorvar = score

            gamescreen.fill(lightgreen_c)
            score_on_screen("Score : " + str(score) + "  HighScore : " + str(highscorvar), white_c, 5, 5)
            pygame.draw.rect(gamescreen, red_c, [apple_x, apple_y, snakesize, snakesize])

            head_snk = [snake_x, snake_y]
            snk_list.append(head_snk)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x < 0 or snake_x > screen_w or snake_y < 0 or snake_y > screen_h:
                gameover = True

            if head_snk in snk_list[:-1]:
                gameover = True

            plot_snk(gamescreen, black_c, snk_list, snakesize)

        pygame.display.update()  # imp-->Update the screen
        clock.tick(fps)

    pygame.quit()
    quit()


game_loop()
