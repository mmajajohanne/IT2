# coding=utf-8
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #(width, height)
pygame.display.set_caption("Runner") #kan også endre ikonet
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 50) 

sky_surf = pygame.image.load("./graphics/Sky.png").convert()
ground_surf = pygame.image.load("./graphics/ground.png").convert()

score_surf = test_font.render('My game',False,(64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (800,300))

player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

    screen.blit(sky_surf,(0,0)) 
    screen.blit(ground_surf,(0,300))

    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
            
    screen.blit(score_surf,score_rect)
            
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    #PLAYER
    player_gravity += 1
    player_rect.y += player_gravity 
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf,player_rect)

    # collision
    if snail_rect.colliderect(player_rect):
        game_active = False

    pygame.display.update()
    clock.tick(60) 


 
