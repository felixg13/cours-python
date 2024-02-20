import pygame
import time
WRONG_NUMBER = 3
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = 75
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
GRAY = (128, 128, 128)

pygame.init()
pygame.display.set_caption("Labyrinthe")


def up():
    global y, WIN
    y -= 1
    next(WIN)

def down():
    global y, WIN
    y += 1
    next(WIN)

def left():
    global x, WIN
    x -= 1
    next(WIN)

def right():
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
            if abs(col - x) <= 1 and abs(row - y) <= 1:
                if board[row][col] == 0:
                    pygame.draw.rect(win, GRAY, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if board[row][col] == 1:
                    pygame.draw.rect(win, WHITE, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE-1, SQUARE_SIZE-1))
                if board[row][col] == 2:
                    pygame.draw.rect(win, YELLOW, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.circle(win, BLUE, (x * SQUARE_SIZE + SQUARE_SIZE/2, y * SQUARE_SIZE + SQUARE_SIZE/2), PIECE_RADIUS)
    pygame.display.flip()


#TODO SOLVE THE MAZE HERE USING: up(), down(), left(), right()    
def solution1():
    down()   
    right()

#Congrats on completing Solution 1
#Lets use loops to solve the problem more efficiently
#TODO Replace WRONG_NUMBER with the right one to solve the maze
#HINT: Look how many times you used the directions in Solution1
#TODO You have to Write the last For statement yourself
def solution2():
    down()
    for i in range(WRONG_NUMBER):
        right()
    for i in range(WRONG_NUMBER):
        down()
    for i in range(WRONG_NUMBER):
        left()
    for i in range(WRONG_NUMBER):
        down()
    #Write the last FOR statement Manually


    
    

def main():

    run = True
    victoire = False
    clock = pygame.time.Clock()
    updateview(WIN)

    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                quit()

            time.sleep(1)

            if run:
                solution2()
                run = False
                quit()
        
    pygame.quit()
    
main()

