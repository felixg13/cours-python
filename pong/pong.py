import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

joueur1 = pygame.Rect( 30 , 250 , PADDLE_HEIGHT , PADDLE_WIDTH )
joueur2 = pygame.Rect( 750 , 250 , PADDLE_HEIGHT , PADDLE_WIDTH )

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
