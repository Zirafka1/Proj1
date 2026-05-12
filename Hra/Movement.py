import pygame
import sys

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pohyb lodicky")

# Hodiny pro hlídání FPS
clock = pygame.time.Clock()

#BARVY
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 0, 0)

# --- OBJEKT HRÁČE (LODIČKA) ---
ship = pygame.Rect(225, 620, 50, 50)
ship_speed = 6

#STRELY
bullets = []
bullet_speed = 8

#HLAVNÍ HERNÍ SMYČKA

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship.centerx - 3, ship.y, 6, 15)
                bullets.append(bullet)
    #POHYB LODIČKY
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ship.x -= ship_speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ship.x += ship_speed


    if ship.x < 0:
        ship.x = 0

    if ship.x > WIDTH - ship.width:
        ship.x = WIDTH - ship.width


    for bullet in bullets[:]:
        bullet.y -= bullet_speed

        if bullet.y < 0:
            bullets.remove(bullet)

    # Vykreslení modrého těla lodě
    pygame.draw.rect(screen, BLUE, ship)
    
    # Vykreslení bílé plachty
    pygame.draw.polygon(
        screen,
        WHITE,
        [
            (ship.centerx, ship.y - 20),
            (ship.x, ship.bottom),
            (ship.right, ship.bottom)
        ]
    )

    # Vykreslení všech aktivních střel
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    pygame.display.flip()
    clock.tick(60)
