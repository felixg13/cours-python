#Créateur: Felix Gagnon
#Niveau: Intermédaire
#Objectif: Créer un jeu rapide de cookie clicker, c'est une bonne introduction à pygame pour découvrir le event loop
#amélioration possible: 
#1)remplace le cercle par un coookie pixel art réaliser sur https://www.pixilart.com/draw
#2)limiter l'esace de cliquage à l'air du cercle (géométrie avancée + pythagore)
import pygame

WIDTH, HEIGHT = 800, 800
PIECE_RADIUS = 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (16, 177, 226)
YELLOW = (255,255,0)

FPS = 30

pygame.init()
pygame.display.set_caption("Cookie Clicker")


def main():
    font = pygame.font.Font(None, 36)
    score = 0
    run = True
    clock = pygame.time.Clock()

    
    while run:

        WIN.fill(BLACK)
        pygame.draw.rect(WIN, BLUE)
        text = font.render("Score: " + str(score), True, YELLOW)
        WIN.blit(text, (20, 20))
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse Clicked")
                score += 1
    pygame.quit()
    return;
    
main()
