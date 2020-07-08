import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chess Game")
white = (255, 255, 255)
black = (0, 0, 0)
beige = (255, 178, 102)
brown = (153, 76, 0)
turn = 0

# pictures
svart_bonde_bild = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\Schacksvartbonde.png")
vit_bonde_bild = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\.png")


def is_even(number):
    if number / 2 == int(number / 2):
        return True
    else:
        return False


def is_odd(number):
    if number / 2 != int(number / 2):
        return True
    else:
        return False


class bonde:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        if color == white:
            if turn == 0:
                self.y = 700
            screen.blit(vit_bonde_bild, (self.x, self.y))
        elif color == black:
            if turn == 0:
                self.y = 200
            screen.blit(svart_bonde_bild, (self.x, self.y))




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(white)


    #start for drawing board
    for i in range(100, 1000, 100):
        pygame.draw.line(screen, black, (i, 100), (i, 900))
    for i in range(100, 1000, 100):
        pygame.draw.line(screen, black, (100, i), (900, i))

    for i in range(100, 900, 100):
        for e in range(100, 900, 100):
            if is_even(i / 100) and not is_even(e / 100):
                rect_color = brown
            elif is_odd(i / 100) and is_even(e / 100):
                rect_color = brown
            else:
                rect_color = beige

            pygame.draw.rect(screen, rect_color, (i, e, 100, 100))
    #end for drawing board

    bonde(white, 100)
    bonde(white, 200)
    bonde(white, 300)
    bonde(white, 400)
    bonde(white, 500)
    bonde(white, 600)
    bonde(white, 700)
    bonde(white, 800)
    bonde(black, 100)
    bonde(black, 200)
    bonde(black, 300)
    bonde(black, 400)
    bonde(black, 500)
    bonde(black, 600)
    bonde(black, 700)
    bonde(black, 800)

    pygame.display.update()
