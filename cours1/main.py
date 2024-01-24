import pygame
import time

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 100
PIECE_RADIUS = SQUARE_SIZE//2 - 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

x = 0
y = 0

board = [[2,1,1,1,1,1,1,1],
        [0,0,0,0,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,0,0,0,0,1,1,1],
        [1,0,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,2]]


# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (16, 177, 226)
YELLOW = (255,255,0)

FPS = 30

pygame.init()
pygame.display.set_caption("Labyrinthe")


def haut():
    global y, WIN
    y -= 1
    next(WIN)

def bas():
    global y, WIN
    y += 1
    next(WIN)

def gauche():
    global x, WIN
    x -= 1
    next(WIN)

def droite():
    global x, WIN
    x += 1
    next(WIN)

def next(win):
    updateview(win)
    time.sleep(1)



def updateview(win):
    win.fill(BLACK)
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                pygame.draw.rect(win, BLACK, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 1: #and abs(col - x) <= 1 and abs(row - y) <= 1:
                pygame.draw.rect(win, WHITE, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE-1, SQUARE_SIZE-1))
            if board[row][col] == 2:
                pygame.draw.rect(win, YELLOW, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.circle(win, BLUE, (x * SQUARE_SIZE + SQUARE_SIZE/2, y * SQUARE_SIZE + SQUARE_SIZE/2), PIECE_RADIUS)
    pygame.display.flip()


    
def solution():
# Donne la solution du labyrinthe ici!    
    bas()
    droite()
    haut()
    gauche()



def solution2():
    bas()
    for i in range(4):
        droite()
    for i in range(2):
        bas()


def main():

    run = True
    victoire = False
    clock = pygame.time.Clock()
    updateview(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                quit()

            time.sleep(1)

            if run:
                solution()
                run = False
                quit()
        
    pygame.quit()
    
main()

