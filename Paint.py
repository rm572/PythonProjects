import pygame
import time


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
gray = (128, 128, 128)
teal = (0, 128, 128)
cyan = (0, 255, 255)
darkcyan = (0, 139, 139)

width = 750
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint with Keyboard')

font = pygame.font.SysFont("calibri", 35)
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def text(msg, color):
    message = font_style.render(msg, True, color)
    dis.blit(message, [width/6, height/2])

dx = 0
dy = 0
radius = 20

game_over = False

x = width//2

y = height//2

color = black

screen.fill(white)

while game_over == False:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = black

            if event.key == pygame.K_r:
                color = red

            if event.key == pygame.K_b:
                color = blue

            if event.key == pygame.K_g:
                color = green

            if event.key == pygame.K_w:
                color = white

            if event.key == pygame.K_p:
                color = purple

            if event.key == pygame.K_y:
                color = yellow

            if event.key == pygame.K_o:
                color = orange

            if event.key == pygame.K_a:
                color = gray

            if event.key == pygame.K_t:
                color = teal

            if event.key == pygame.K_c:
                color = cyan

            if event.key == pygame.K_d:
                color = darkcyan

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] == True:
        x += 5

    if keys[pygame.K_LEFT] == True:
        x -= 5

    if keys[pygame.K_DOWN] == True:
        y += 5

    if keys[pygame.K_UP] == True:
        y -= 5


    x = x % width
    y = y % height

    circ = pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.update()

    clock.tick(45)

pygame.quit()


