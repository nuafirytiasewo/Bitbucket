# импорт модулей
import pygame
import random

# инициализация игры
pygame.init()

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# размеры экрана
display_width = 800
display_height = 600

# создание экрана
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Змейка')

# флаг для выхода из игры
gameExit = False

# координаты головы змейки
lead_x = display_width / 2
lead_y = display_height / 2

# изменение координат головы змейки
lead_x_change = 0
lead_y_change = 0

# размеры змейки
block_size = 10

# скорость змейки
clock = pygame.time.Clock()
snake_speed = 15

# переменная для хранения яблока
apple_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
apple_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

# переменная для хранения длины змейки
snakeLength = 1
snakeList = []

# функция для отрисовки змейки
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

# функция для отрисовки яблока
def apple(apple_x, apple_y):
    pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, block_size, block_size])

# начало игры
while not gameExit:
    # обработка событий
    for event in pygame.event.get():
        # если нажата кнопка "Выход"
        if event.type == pygame.QUIT:
            gameExit = True
        # если нажата кнопка клавиатуры
        if event.type == pygame.KEYDOWN:
            # движение змейки вверх
            if event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            # движение змейки вниз
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
            # движение змейки влево
            elif event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            # движение змейки вправо
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0

    # изменение координат головы змейки
    lead_x += lead_x_change
    lead_y += lead_y_change

    # отрисовка фона
    gameDisplay.fill(white)

    # добавление нового блока в начало списка змейки
    snakeHead = []
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snakeList.append(snakeHead)

    # удаление последнего блока змейки, если ее длина больше, чем snakeLength
    if len(snakeList) > snakeLength:
        del snakeList[0]

    # отрисовка змейки
    snake(block_size, snakeList)

    # отрисовка яблока
    apple(apple_x, apple_y)

    # проверка на съедение яблока
    if lead_x == apple_x and lead_y == apple_y:
        # увеличение длины змейки
        snakeLength += 1
        # генерация новых координат для яблока
        apple_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
        apple_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    # обновление экрана
    pygame.display.update()

    # установка частоты обновления экрана
    clock.tick(snake_speed)

# выход из игры
pygame.quit()
quit()