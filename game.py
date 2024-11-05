import pygame

pygame.init()
sw = 600
sh = 450
screen = pygame.display.set_mode((sw,sh))
player = pygame.Rect((300,225,12,12))
run = True
while run:
    pygame.draw.rect(screen,(10,0,199),player)
    key = pygame.key.get_pressed()

    screen.fill((0,0,0))
    if key[pygame.K_a]== True:
        player.move_ip(-1,0)
    elif key[pygame.K_d]== True:
        player.move_ip(1,0)
    elif key[pygame.K_w]== True:
        player.move_ip(0,-1)
    elif key[pygame.K_s]== True:
        player.move_ip(0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    pygame.display.update()
pygame.quit()