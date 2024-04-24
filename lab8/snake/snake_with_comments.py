import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 1000
dis_height = 600

# Инициализация окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

# Инициализация часов
clock = pygame.time.Clock()

# Размер блока змейки и начальная скорость
snake_block = 10
snake_speed = 10

# Создание шрифтов для отображения счёта
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    # Функция для отображения счёта
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    # Функция для отрисовки змейки на экране
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    # Функция для вывода сообщения на экран
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    # Инициализация переменных
    global snake_speed
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    # Определение уровней с соответствующими скоростями
    levels = [
        {"speed": 10},  # Уровень 1
        {"speed": 15},  # Уровень 2
        {"speed": 20},  # Уровень 3
        
    ]
    current_level = 1
    snake_speed = levels[current_level]["speed"]
    
    while not game_over:
        while game_close == True:
            # Обработка событий при завершении игры
            dis.fill(blue)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Обработка нажатий клавиш
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        # Обработка столкновений и границ экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        
        # Отрисовка элементов на экране
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        
        # Обработка события поедания еды и повышение уровня
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if Length_of_snake % 5 == 0:  # Повышение уровня каждые 5 очков
                current_level += 1
                snake_speed = levels[current_level]["speed"]
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()