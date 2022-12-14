import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,400)) #(width, height)
pygame.display.set_caption("Runner") #kan også endre ikonet
clock = pygame.time.Clock() 

sky_surface = pygame.image.load("pygameIT2/graphics/Sky.png")
ground_surface = pygame.image.load("pygameIT2/graphics/ground.png") 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface,(0,0)) #(surface,position) one surface on another surface
    screen.blit(ground_surface,(0,300))
    
    pygame.display.update()
    clock.tick(60) #sier at while-løkken bare skal kjøre max 60 ganger per sekund

