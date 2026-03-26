import pygame
pygame.init()

WIDTH = 1200
HEIGHT = 1000
#set dimensions of the screen
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shapes")
screen.fill("blue")
#main loop
while True:
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.draw.circle(screen,"pink",(250,250),50,30)
                
            if event.key == pygame.K_r:
                pygame.draw.rect(screen,"red",(450,450,200,100))
            if event.key == pygame.K_l:
                pygame.draw.line(screen,"red",(50,50),(100,100),100)
            if event.key == pygame.K_e:
                pygame.draw.ellipse(screen,"red",(600,300,100,65),15)
            if event.key == pygame.K_p:
                pygame.draw.polygon(screen,"green",[(200,180),(400,180),(300,100)])
            #update the display
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            pygame.draw.circle(screen,"yellow",mouse_pos,50,0)
    pygame.display.update()