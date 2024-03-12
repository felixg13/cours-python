import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up the clock
clock = pygame.time.Clock()

# Define the game objects
paddle_width, paddle_height = 20, 100
paddle_speed = 5
ball_size = 20
ball_speedX = 2 * random.choice([-1, 1])
ball_speedY = 2 * random.choice([-1, 1])

player1_paddle = pygame.Rect(30, 250, paddle_width, paddle_height)
player2_paddle = pygame.Rect(750, 250, paddle_width, paddle_height)
ball = pygame.Rect(400, 400, ball_size, ball_size)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += paddle_speed

    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += paddle_speed

    # Ball movement
    ball.x += ball_speedX
    ball.y += ball_speedY

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speedX *= -1

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speedY *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - ball_size // 2
        ball.y = HEIGHT // 2 - ball_size // 2
        ball_speedX = 2 * random.choice([-1,1])
        ball_speedY = 2 * random.choice([-1,1])
    

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
