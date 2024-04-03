import pygame
from pygame.draw import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((1200, 900))

font = pygame.font.Font(None, 36)
score = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

schet = 0 #счетчик
shariki = [] #вся инфа про шарики сюда


def new_sharik():
    '''
    Создает новый шарик
    x, y - рандомные значения центра шара
    r - рандомный радиус
    color - выбирает рандомный цвет, заданные в начале списком COLORS
    shariki.append - добавляет корды центра и радиуса шарика в список всех шаров
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    shariki.append((x, y, r, color))



def risuem_sharik():
    '''
    Рисует шары на экране
    for ... in ... - берет шар из общего списка
    присвает x, y, z, color все сохраненные значения
    '''
    for ball in shariki:
        x, y, r, color = ball
        circle(screen, color, (x, y), r)

def risovat_text(screen, text, x, y):
    '''
    Функция для отображения счетчика на экране (при помощи интернета)
    ... font.render - функция в питоне, дающая рендерить какой-либо текст через библиотеку pygame с определенными параметрами

    '''
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))
def proverka(x_click, y_click):
    '''
    Проверяет, попал ли курсор в шарик и добавляет очко в общий счет в конце, если попал.
    Добавляет в счетчик на экране +1 для дальнейшего вывода на экран
    вызывает в функцию координаты курсора (x_click, y_click)
    for ... in ... - берет шарик из общего списка шариков
    if (...) - проверяет, попал ли курсор (его координаты) в шар
    shariki.remove(sharik) - удаление из списка всех шаров последнего шара, в который попал курсор
    global ... - обозначает глобальные переменные, не зависящие от того, где они находятся
    '''
    global schet, score
    for sharik in shariki:
        x, y, r, _ = sharik
        if (x_click - x)**2 + (y_click - y)**2 <= r**2:
            schet += 1
            score += 1
            shariki.remove(sharik)
            #print("Попадение:", schet)


def handle_click(event):
    '''
    if (...) - Если происходит нажатие маши, выполняется положительное условие
    x_click, y_click - присваивает кординаты нажатия курсора
    proverka(... ) - запускает функцию проверки клика на нахождение внутри радиуса шара
    '''
    if event.type == pygame.MOUSEBUTTONDOWN:
        x_click, y_click = event.pos
        proverka(x_click, y_click)


#игра
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #останавливает если лив
            finished = True
            running = False
        handle_click(event) #вызывает клик мыши на проверку

    if len(shariki) < 2:  #сколько максимум шариков на экране
        new_sharik()

    risuem_sharik()  #все шарики отобразит
    pygame.display.update()  #очистить экран
    screen.fill(BLACK)  #экран фул блек
    screen.fill((0, 0, 0))
    risovat_text(screen, f"{score}", 10, 10) #

#help()

print("Итоговый счет:", schet)
pygame.quit()

