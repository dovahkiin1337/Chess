import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chess Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
beige = (255, 178, 102)
brown = (153, 76, 0)
grey = (162, 162, 162)

# Other variables
turn = 0
run = True
white_pawns = []
black_pawns = []
pawns = []

# Start for Images
black_pawn_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\Schacksvartbonde.png")
white_pawn_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\.png")

black_rook_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\Schacksvarttorn.png")
white_rook_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")

black_knight_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")
white_knight_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")

black_bishop_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")
white_bishop_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")

black_king_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")
white_king_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")

black_queen_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")
white_queen_image = pygame.image.load(r"C:\Users\Henrik\PycharmProjects\PYTHON\")
# End for Images





# Functions
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


# Pawn class start(Not done)
class pawn:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 700
            if is_even(turn):
                if self.y == 700:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y - 200 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 200
            if is_odd(turn):
                if self.y == 200:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y + 300 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))


# Pawn class end

# Rook class start(Not done)
class rook:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 800
            if is_even(turn):
                if self.y == 800:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y - 200 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 100
            if is_odd(turn):
                if self.y == 100:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y + 300 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))

# Rook class end


# Knight class start(Not done)
class knight:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 800
            if is_even(turn):
                if self.y == 800:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y - 200 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 100
            if is_odd(turn):
                if self.y == 200:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y + 300 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))
# Knight class end


# Bishop class start(Not done)
class bishop:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 800
            if is_even(turn):
                if self.y == 700:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y - 200 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 100
            if is_odd(turn):
                if self.y == 200:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y + 300 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))

# Bishop class end

# King class start(Not done)
class king:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 800
            if is_even(turn):
                if self.y == 700:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y - 200 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 100
            if is_odd(turn):
                if self.y == 200:
                    if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                            1, 0, 0):
                        self.move = True
                    if self.move and mouse_click == (1, 0, 0):
                        if self.y + 300 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                            self.x = round_down_to_hundred(mouse_x)
                            self.y = round_down_to_hundred(mouse_y)
                            turn += 1
                            self.move = False

                elif (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (
                        1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))
# King class end


# Queen class start(Not done)
class queen:
    def __init__(self, color, x):
        self.color = color
        self.x = x
        self.move = False
        self.y = 0
        self.alive = True

    def activate(self):
        global turn
        if self.color == white:
            if turn == 0:
                self.y = 800
            if is_even(turn):
                if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y - 100 < mouse_y < self.y and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False
            if self.alive:
                screen.blit(white_pawn_image, (self.x, self.y))

        elif self.color == black:
            if turn == 0:
                self.y = 100
            if is_odd(turn):
                if (self.x + 100) > mouse_x > self.x and (self.y + 100) > mouse_y > self.y and mouse_click == (1, 0, 0):
                    self.move = True
                if self.move and mouse_click == (1, 0, 0):
                    if self.y + 200 > mouse_y > self.y + 100 and self.x + 100 > mouse_x > self.x:
                        self.x = round_down_to_hundred(mouse_x)
                        self.y = round_down_to_hundred(mouse_y)
                        turn += 1
                        self.move = False

            if self.alive:
                screen.blit(black_pawn_image, (self.x, self.y))
# Queen class end


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
    turn_text_x = 300
    turn_text_y = 0
    turn_text_width = 400
    turn_text_height = 90

    # End for defining variables

    screen.fill(white)
    screen.blit(black_rook_image, (0, 0))
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
    # End for drawing board

    # Start for explaining whose turn it is

    if is_even(turn):
        pygame.draw.rect(screen, grey, (turn_text_x, turn_text_y, turn_text_width, turn_text_height), 0)
        font = pygame.font.SysFont(None, 70)
        text = font.render("White's Turn", True, white)
        screen.blit(text, (turn_text_x + (turn_text_width / 2 - text.get_width() / 2),
                           turn_text_y + (turn_text_height / 2 - text.get_height() / 2)))

    elif is_odd(turn):
        pygame.draw.rect(screen, grey, (turn_text_x, turn_text_y, turn_text_width, turn_text_height), 0)
        font = pygame.font.SysFont(None, 70)
        text = font.render("Black's Turn", True, black)
        screen.blit(text, (turn_text_x + (turn_text_width / 2 - text.get_width() / 2),
                           turn_text_y + (turn_text_height / 2 - text.get_height() / 2)))

    # End for explaining whose turn it is

    pawns = white_pawns + black_pawns
    for item in pawns:
        item.activate()

    pygame.display.update()
# End of main loop
