import pygame
import random

WIDTH, HEIGHT = 800, 800
PLAYER_RADIUS = 20
CHEESE_RADIUS = 10

# rgb
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
BLUE = (16, 177, 226)
YELLOW = (255,255,0)

FPS = 30

def checkCollision(x1, y1, x2, y2, r1, r2):
    if (x2 - x1)**2 + (y2 - y1)**2 <= (r1 + r2)**2:
        return True
    else:
        return False

def main():

    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('RATnCHEESE')
    font = pygame.font.Font(None, 36)

    x,y = 400,400
    cheeseX, cheeseY = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    score = 0

    run = True
    while run:
        clock.tick(FPS)

        window.fill(WHITE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                quit()

        
        pygame.display.update()
    pygame.quit()
    
main()

