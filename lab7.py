import pygame
pygame.init()

screen=pygame.display.set_mode((640,480))
background=pygame.Surface(screen.get_size())
background.fill((255,255,255))

# ballsurface = pygame.Surface((50, 50))
# pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25) # blue colored cirlce RGB -> (0, 0, 255)

pygame.draw.circle(background,(228,35,127),(320,240),150) # "giant" pink circle, radius=150

pygame.draw.polygon(background,(0,255,0),((40,0),(30,30),(50,30)))
pygame.draw.polygon(background,(0,255,0),((0,30),(30,30),(24,48)))
pygame.draw.polygon(background,(0,255,0),((50,30),(80,30),(56,48))) # polygons
pygame.draw.polygon(background,(0,255,0),((24,48),(10,90),(40,60)))
pygame.draw.polygon(background,(0,255,0),((40,60),(56,48),(70,90)))

pygame.draw.arc(background,(0,0,0),(0,0,1280,960),0,3.14) # arc

for point in range(0,641,64): # range(start, stop, step)
   pygame.draw.line(background, ( (255-(point%256))%256 ,(255-(228+point))%256 ,point%256), (0,0), (480, point), 1)
   pygame.draw.line(background, ( (255-(point%256))%256 , point%256 , (255+(point%256))%256), (640,0), (160, point), 1)             # lines
   pygame.draw.line(background, ( (255+(point%256))%256 ,point%256 , (100*point//64)%256 ), (640,480), (160, point), 1)             # lines
   pygame.draw.line(background, ( (100*point//64)%256 , (228+point)%256 , (255*(point%256))%256 ) , (0,480), (480, point), 1)

background=background.convert()
screen.blit(background, (0, 0))

# ballsurface = ballsurface.convert()
# screen.blit(background, (0, 0))
# screen.blit(ballsurface, (50, 50))

running = True
FPS = 65
clock = pygame.time.Clock()

while running:
    milliseconds=clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        elif(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_ESCAPE):
                running=False
    pygame.display.flip()

pygame.quit()