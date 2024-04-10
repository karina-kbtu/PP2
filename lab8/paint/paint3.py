import pygame
import random

pygame.init()

win_x = 500
win_y = 500

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint')


class Drawing(object):

    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6
        self.tick = 0
        self.time = 0
        self.play = False
        self.draw_rect = False
        self.draw_circle = False

    def draw(self, win, pos):
        if self.draw_rect:
            pygame.draw.rect(win, self.color, (pos[0]-self.rad, pos[1]-self.rad, self.rad*2, self.rad*2))
        elif self.draw_circle:
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        else:
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        if self.color == (255, 255, 255):
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), 20)

    def click(self, win, list, list2):
        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 400:
            if pos[1] > 25:
                self.draw(win, pos)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            for button in list:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        self.color = button.color2
                        self.draw_rect = False
                        self.draw_circle = False
            for button in list2:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        if self.tick == 0:
                            if button.action == 1:
                                win.fill((255, 255, 255))
                                self.tick += 1
                            if button.action == 2 and self.rad > 4:
                                self.rad -= 1
                                self.tick += 1
                                pygame.draw.rect(
                                    win, (255, 255, 255), (410, 308, 80, 35))

                            if button.action == 3 and self.rad < 20:
                                self.rad += 1
                                self.tick += 1
                                pygame.draw.rect(
                                    win, (255, 255, 255), (410, 308, 80, 35))

                            if button.action == 5 and self.play == False:
                                self.play = True
                                game()
                                self.time += 1
                            if button.action == 6:
                                self.play = False
                                self.time = 0
                            if button.action == 8:
                                self.draw_rect = True
                                self.draw_circle = False
                            if button.action == 9:
                                self.draw_circle = True
                                self.draw_rect = False

        for button in list2:
            if button.action == 4:
                button.text = str(self.rad)

            if button.action == 7 and self.play == True:
                button.text = str(40 - (player1.time // 100))
            if button.action == 7 and self.play == False:
                button.text = 'Time'


class Button(object):

    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color2)
        pygame.draw.rect(win, (255, 255, 255), (410, 446, 80, 35))
        pygame.draw.rect(win, (255, 255, 255), (410, 308, 80, 35))
        win.blit(text, (int(self.x+self.width/2-text.get_width()/2),
                        int(self.y+self.height/2-text.get_height()/2)))


def draw_header(win):
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 25))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 25), 2)

    font = pygame.font.SysFont('comicsans', 30)

    canvas_text = font.render('Field for drawing', 1, (0, 0, 0))
    win.blit(canvas_text, (int(200 - canvas_text.get_width() / 2),
                          int(26 / 2 - canvas_text.get_height() / 2) + 2))

    tools_text = font.render('Tools', 1, (0, 0, 0))
    win.blit(tools_text, (int(450 - tools_text.get_width() / 2),
                         int(26 / 2 - tools_text.get_height() / 2 + 2)))


def draw(win):
    player1.click(win, Buttons_color, Buttons_other)

    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500),
                     2)
    pygame.draw.rect(win, (255, 255, 255), (400, 0, 100, 500),)
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500),
                     2)
    draw_header(win)

    for button in Buttons_color:
        button.draw(win)

    for button in Buttons_other:
        button.draw(win)

    pygame.display.update()


def main_loop():
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False

        draw(win)

        if 0 < player1.tick < 40:
            player1.tick += 1
        else:
            player1.tick = 0

        if 0 < player1.time < 4001:
            player1.time += 1
        elif 4000 < player1.time < 4004:
            game_over()
            player1.time = 4009
        else:
            player1.time = 0
            player1.play = False

    pygame.quit()


player1 = Drawing()
win.fill((255, 255, 255))
pos = (0, 0)

red_button = Button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0))
blue_button = Button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255))
green_button = Button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0))
orange_button = Button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0))
yellow_button = Button(407, 122, 40, 40, (255, 255, 0), (255, 255, 0))
purple_button = Button(453, 122, 40, 40, (112, 48, 160), (112, 48, 160))
black_button = Button(407, 168, 40, 40, (0, 0, 0), (0, 0, 0))
white_button = Button(453, 168, 40, 40, (0, 0, 0), (255, 255, 255), 1)

clear_button = Button(407, 214, 86, 40, (201, 201, 201), (0, 0, 0), 0, 1, 'Clear')

smaller_button = Button(407, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 2, '-')
bigger_button = Button(453, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 3, '+')
size_display = Button(407, 306, 86, 40, (0, 0, 0), (0, 0, 0), 1, 4, 'Size')

rectangle_button = Button(420, 370, 60, 40, (201, 201, 201), (0, 0, 0), 0, 8, 'Rectangle')
circle_button = Button(420, 320, 60, 40, (201, 201, 201), (0, 0, 0), 0, 9, 'Circle')

Buttons_color = [blue_button, red_button, green_button, orange_button,
                 yellow_button, purple_button, black_button, white_button]
Buttons_other = [clear_button, smaller_button, bigger_button,
                 size_display, rectangle_button, circle_button]

main_loop()