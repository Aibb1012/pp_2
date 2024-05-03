# Racerrr
import pygame, sys
from pygame.locals import *
import random , time

# from pygame.sprite import _Group
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 1
coins = 0
background = pygame.image.load("road.png")
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
# total_coins = font_small.render("Coins" , True , BLACK)

class Moneyy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(30 , 250)
        self.image = pygame.image.load("coin.png")
        
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 

    def move(self):
        self.rect.move_ip(0 , 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            # self.image = pygame.transform.scale(self.image, (self.x,self.x))
    #special function for collide        
    def nextCoin(self , x):
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
        self.image = pygame.transform.scale(self.image, (x , x))
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
        
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
       
 
#class for playing movement
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
 
      
# Assign classes as variables
P1 = Player()
E1 = Enemy()
C1 = Moneyy()
# Creating Sprites Groups
moneys = pygame.sprite.Group()
moneys.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event for speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

#Game Loop
while True:     
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #       SPEED += 0.5              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Bliting texts
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score:"+ str(SCORE), True, GREEN)
    money = font_small.render("Coins:" + str(coins) , True , WHITE)
    DISPLAYSURF.blit(scores, (10,10))
    # DISPLAYSURF.blit(total_coins , (10 , 60))
    DISPLAYSURF.blit(money , (10 , 62))
    if SCORE%3 ==0:
        congrat = font_small.render("Congratulations" , True , RED)
        DISPLAYSURF.blit(congrat , (SCREEN_WIDTH-200 , 10))
        # time.sleep(0.2)
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        if pygame.sprite.spritecollideany(P1 ,moneys):
        # time.sleep(0.1)
            x = random.randint(50 , 150)
            C1.nextCoin(x)
            coins +=x//13
            if coins%5==0:
                SPEED+=0.5
            time.sleep(0.1)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        DISPLAYSURF.blit(scores , (60 , 320))
        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 

        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    
    pygame.display.update()
    FramePerSec.tick(FPS)
