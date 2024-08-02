import pygame # type: ignore
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

width = 1250
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint with Mouse')

font = pygame.font.SysFont("calibri", 35)
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

font_style = pygame.font.SysFont(None, 50)

def text(msg, color):
    message = font_style.render(msg, True, color)
dx = 0
dy = 0

small_radius = 15
radius = 25
big_radius = 40
r = 20

rect = 40

game_over = False

x = width//2

y = height//2

color = black

color_list = [blue, red, green, yellow, purple, black, cyan, white, orange, teal, gray]
screen.fill(white)

while game_over == False:

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
##    print(mouse_pos)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                if 0 <= mouse_x <= rect and 0 <= mouse_y <= rect:
                    color = blue

                if rect < mouse_x <= 2 * rect and 0 < mouse_y <= rect:
                    color = red

                if 2 * rect < mouse_x <= 3 * rect and 0 < mouse_y <= rect:
                    color = green

                if 3 * rect < mouse_x <= 4 * rect and 0 < mouse_y <= rect:
                    color = yellow

                if 4 * rect < mouse_x <= 5 * rect and 0 < mouse_y <= rect:
                    color = purple

                if 5 * rect <= mouse_x <= 6 * rect and 0 <= mouse_y <= rect:
                    color = black

                if 6 * rect < mouse_x <= 7 * rect and 0 < mouse_y <= rect:
                    color = cyan

                if 7 * rect < mouse_x <= 8 * rect and 0 < mouse_y <= rect:
                    color = white

                if 8 * rect < mouse_x <= 9 * rect and 0 < mouse_y <= rect:
                    color = orange

                if 9 * rect < mouse_x <= 10 * rect and 0 < mouse_y <= rect:
                    color = teal

                if 10 * rect < mouse_x <= 11 * rect and 0 < mouse_y <= rect:
                    color = gray

                if 13 * rect - radius < mouse_x <= 13 * rect + radius and 0 < mouse_y <= 2 * radius:
                    r = small_radius

                if 15 * rect - radius < mouse_x <= 15 * rect + radius and 0 < mouse_y <= 2 * radius:
                    r = radius

                if 17 * rect - big_radius < mouse_x <= 17 * rect + big_radius and 0 < mouse_y <= 2 * big_radius:
                    r = big_radius

                if 10 <= mouse_x <= 40 and height-20-rect <= mouse_y <= height-20:
                    screen.fill(color)

                    if color == black:
                        color = white
##                        print("white")
                    else:
                        color = black
##                        print("black")

                    pygame.draw.rect(screen, color, (10, height-20-rect, rect, rect))




                # for i in range(len(color_list)):
                #     if i * rect <= mouse <= (i + 1) * rect and 0 <= mouse_y <= rect:

                #         color = color_list[i]


##Set mouse to change on the drawing screen, add in the rest of the colors,
##make an array that contains the colors and then make a for loop to draw all the
##rectangles and to click

    for i in range(len(color_list)):
        pygame.draw.rect(screen, color_list[i], (i * rect, 0, rect, rect))

    pygame.draw.circle(screen, color, (17 * rect, big_radius), big_radius)
    pygame.draw.circle(screen, color, (15 * rect, big_radius), radius)
    pygame.draw.circle(screen, color, (13 * rect, big_radius), small_radius)


    # pygame.draw.rect(screen, red, (rect, 0, rect, rect))
    # pygame.draw.rect(screen, green, (2 * rect, 0, rect, rect))
    # pygame.draw.rect(screen, yellow, (3 * rect, 0, rect, rect))
    # pygame.draw.rect(screen, purple, (4 * rect, 0, rect, rect))

##    if mouse_y >= rect + 50:
##        if pygame.mouse.get_pressed()[0] == 1:
##            if mouse_y > 580 and mouse_y < 550 and mouse_x < 10 and mouse_x > 40:
##
##                pygame.draw.circle(screen, color, (mouse_x, mouse_y), r)
##                pygame.display.update()


    if mouse_y >= rect + 50:

##        if mouse_y > 580 and mouse_y < 550 and mouse_x < 10 and mouse_x > 40:
        if pygame.mouse.get_pressed()[0] == 1 and not (10 <= mouse_x <= 40 and height-rect-20 <= mouse_y <= height-20):
            pygame.draw.circle(screen, color, (mouse_x, mouse_y), r)
            pygame.display.update()


    pygame.draw.rect(screen, color, (10, height-20-rect, rect, rect))
##    print(pygame.mouse.get_pressed())

    x = x % width
    y = y % height

##    circ = pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.update()

    clock.tick(20000)

pygame.quit()


