import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
#set dimensions of the screen
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shapes")

#main loop
while True:
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("blue")
    pygame.draw.circle(screen,"pink",(250,250),50,30)
    pygame.draw.rect(screen,"red",(450,450,200,100))
    pygame.draw.line(screen,"red",(50,50),(100,100),100)
    pygame.draw.ellipse(screen,"red",(600,300,100,65),15)
    #update the display
    pygame.display.update()