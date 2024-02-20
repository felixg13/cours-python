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
        pygame.draw.circle(window, GRAY, (x, y), PLAYER_RADIUS)
        pygame.draw.circle(window, YELLOW, (cheeseX, cheeseY), CHEESE_RADIUS)
        text = font.render("Score: " + str(score), True, BLACK)
        window.blit(text, (10, 10))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_DOWN:
                    move_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_DOWN:
                    move_down = False
        if move_left:
            x -= 5
        if move_right:
            x += 5
        if move_up:
            y -= 5
        if move_down:
            y += 5

        if checkCollision(x, y, cheeseX, cheeseY, PLAYER_RADIUS, CHEESE_RADIUS): 
            cheeseX, cheeseY = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            score += 1

        
        pygame.display.update()
    pygame.quit()
    
main()

