import os
import pygame
from boardGame.chineseChess import ChineseChess
def clickEvent():
    pass

if __name__ == '__main__':
    pygame.init()
    window_size = (800, 600)
    # Create the window
    screen = pygame.display.set_mode(window_size)
    game = ChineseChess()
    game.createBoard()
    button_size=(100,50)

    # left, top, width, height
    button=pygame.Rect((window_size[0]-button_size[0])//2,(window_size[1]-button_size[1])//2,button_size[0],button_size[1])
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit Pygame when the user closes the window
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                clickEvent()
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0, 0, 0), button)
    
        # Update the screen
        pygame.display.update()

