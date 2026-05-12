

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


