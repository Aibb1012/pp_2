# circle_movingred
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
colordefault = (255, 0, 0)
ballradius = 50

speed = 15

ballpos = [400 , 300]

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ballpos[1] = max(ballradius, ballpos[1] - speed)
    if keys[pygame.K_DOWN]:
        ballpos[1] = min(600 - ballradius, ballpos[1] + speed)
    if keys[pygame.K_LEFT]:
        ballpos[0] = max(ballradius, ballpos[0] - speed)
    if keys[pygame.K_RIGHT]:
        ballpos[0] = min(800 - ballradius, ballpos[0] + speed)

    pygame.draw.circle(screen, colordefault, ballpos, ballradius)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()