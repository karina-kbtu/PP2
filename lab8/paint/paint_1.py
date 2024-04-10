import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Программа Paint")

# Установка начальных значений для цвета, толщины кисти и выбранной фигуры
brush_color = (0, 0, 0)
brush_size = 5
current_shape = "circle"  # Начальная форма - круг

# Определение цветов для кнопок
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# Определение размеров для кнопок
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 10

# Определение позиций кнопок на дисплее
color_buttons = [
    pygame.Rect(SCREEN_WIDTH - (BUTTON_WIDTH + BUTTON_MARGIN) * i - BUTTON_WIDTH - BUTTON_MARGIN, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
    for i in range(5)
]

shape_buttons = [
    pygame.Rect(SCREEN_WIDTH - (BUTTON_WIDTH + BUTTON_MARGIN) * i - BUTTON_WIDTH - BUTTON_MARGIN, BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
    for i in range(2)
]

size_buttons = [
    pygame.Rect(SCREEN_WIDTH - (BUTTON_WIDTH + BUTTON_MARGIN) * i - BUTTON_WIDTH - BUTTON_MARGIN, 2 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT)
    for i in range(5)
]

# Подписи для кнопок
color_button_labels = ["Red", "Green", "Blue", "White", "Black"]
shape_button_labels = ["Circle", "Rectangle"]
size_button_labels = ["Small", "Medium", "Large", "Extra Large", "Jumbo"]

# Флаг, указывающий на то, что кнопка мыши нажата
drawing = False

# Функция рисования
def draw():
    screen.fill((255, 255, 255))  # Заполнение экрана белым цветом

    # Рисование кнопок и подписей
    for i, button in enumerate(color_buttons):
        pygame.draw.rect(screen, [COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_WHITE, COLOR_BLACK][i], button)
        font = pygame.font.SysFont(None, 24)
        text = font.render(color_button_labels[i], True, (0, 0, 0))
        screen.blit(text, (button.x + (BUTTON_WIDTH - text.get_width()) // 2, button.y + (BUTTON_HEIGHT - text.get_height()) // 2))

    for i, button in enumerate(shape_buttons):
        pygame.draw.rect(screen, [COLOR_RED, COLOR_GREEN][i], button)
        font = pygame.font.SysFont(None, 24)
        text = font.render(shape_button_labels[i], True, (0, 0, 0))
        screen.blit(text, (button.x + (BUTTON_WIDTH - text.get_width()) // 2, button.y + (BUTTON_HEIGHT - text.get_height()) // 2))

    for i, button in enumerate(size_buttons):
        pygame.draw.rect(screen, [COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_WHITE, COLOR_BLACK][i], button)
        font = pygame.font.SysFont(None, 24)
        text = font.render(size_button_labels[i], True, (0, 0, 0))
        screen.blit(text, (button.x + (BUTTON_WIDTH - text.get_width()) // 2, button.y + (BUTTON_HEIGHT - text.get_height()) // 2))

    # Рисование курсора
    if drawing and screen.get_rect().collidepoint(pygame.mouse.get_pos()):
        if current_shape == "circle":
            pygame.draw.circle(screen, brush_color, pygame.mouse.get_pos(), brush_size // 2)
        elif current_shape == "rectangle":
            pygame.draw.rect(screen, brush_color, (pygame.mouse.get_pos()[0] - brush_size // 2, pygame.mouse.get_pos()[1] - brush_size // 2, brush_size, brush_size))

    pygame.display.update()

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка событий мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Проверяем, на какую кнопку нажали
                for i, button in enumerate(color_buttons):
                    if button.collidepoint(event.pos):
                        brush_color = [COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_WHITE, COLOR_BLACK][i]
                for i, button in enumerate(shape_buttons):
                    if button.collidepoint(event.pos):
                        current_shape = ["circle", "rectangle"][i]
                for i, button in enumerate(size_buttons):
                    if button.collidepoint(event.pos):
                        brush_size = (i + 1) * 5
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    draw() 