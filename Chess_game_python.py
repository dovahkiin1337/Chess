import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chess Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
beige = (255, 178, 102)
brown = (153, 76, 0)

# Other variables
turn = 0
run = True
white_pawns = []
black_pawns = []
pawns = []
moving = False

# Images
black_pawn_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\Schacksvartbonde.png")
white_pawn_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\.png")


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

def round_down_to_hundred(number):
    number = number / 100
    number = int(number)
    return number * 100

class pawn:
    def __init__(self, color, x):
        self.color = color
        self.x = x

    def activate(self):
        global moving
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 700
            screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 200
            screen.blit(black_pawn_image, (self.x, self.y))

        if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (1, 0, 0):
            moving = True
        if moving and mouse_click == (1, 0, 0) and mouse_y < self.y:
            self.x = round_down_to_hundred(mouse_x)
            self.y = round_down_to_hundred(mouse_y)
            turn += 1






for i in range(100, 900, 100):
    white_pawns.append(pawn(white, i))
for i in range(100, 900, 100):
    black_pawns.append(pawn(black, i))

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Start for defining variables
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    mouse_click = pygame.mouse.get_pressed()

# End for defining variables
    screen.fill(white)

    # Start for drawing board
    for i in range(100, 900, 100):
        for e in range(100, 900, 100):
            if is_even(i / 100) and not is_even(e / 100):
                rect_color = brown
            elif is_odd(i / 100) and is_even(e / 100):
                rect_color = brown
            else:
                rect_color = beige

            pygame.draw.rect(screen, rect_color, (i, e, 100, 100))
    # end for drawing board

    pawns = white_pawns + black_pawns
    for item in pawns:
        item.activate()

    pygame.display.update()
# End of main loop
