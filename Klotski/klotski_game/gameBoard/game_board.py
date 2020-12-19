import pygame

x = pygame.init()
board = 2
plane = pygame.display.set_mode((600,600))

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

def board_function():
    return 3

pygame.quit()
quit()


