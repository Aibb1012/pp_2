import pygame
import time
import random
 
pygame.init()
#Screen settings
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake_block = 25
snake_speed = 10
food_block = 25
level = 0
#Font settings
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("comicsansms", 25)




#Blit Score counter on the top left
def Your_score_level(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    
    dis.blit(value, [0, 0])

#Drawing the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, pygame.Rect(x[0], x[1], snake_block, snake_block))

#bliting an message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])



#Game Loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    level = 0
    #initial position of an apple
    foodx = random.randint(0, dis_width - snake_block) // snake_block * snake_block 
    foody = random.randint(0, dis_height - snake_block) // snake_block * snake_block

    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 20)
    # seconds = 0


    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            # Your_score_level(Length_of_snake - 1 , Length_of_snake-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block  #присваиваем значение переменных ИЗМЕНЕНИЯ координат змеи при нажатии стрелок
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0



        #Закрытие игры при попадании головы змеи на границы экрана игры
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        #присваевам те значения после нажатии кнопок к первоначальным координатам головы змеи
        x1 += x1_change 
        y1 += y1_change

        global food_block #делаем значения переменных характеристик еды и змеи
        global snake_speed 
        
        dis.fill(blue)

        pygame.draw.rect(dis, green, pygame.Rect(foodx, foody, food_block, food_block))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head) #храним размеры змеи

        #Logic to remove after move(constant moving)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #Случай если столкнулась сама с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        
        our_snake(snake_block, snake_List)
        Your_score_level(Length_of_snake - 1)
        value2 = score_font.render("Level: "+ str(level) , True , green)
        dis.blit(value2 , [0 , 40])


        

        
        pygame.display.update() 
        for event in pygame.event.get(): #таймер исчезновения еды
            if event.type == timer:
                foodx = random.randint(0, dis_width - snake_block) // snake_block * snake_block
                foody = random.randint(0, dis_height - snake_block) // snake_block * snake_block
                time.sleep(0.1)
    

        #eating food and random distribution
        if x1 == foodx and y1 == foody:
            foodx = random.randint(0, dis_width - snake_block) // snake_block * snake_block
            foody = random.randint(0, dis_height - snake_block) // snake_block * snake_block
            food_block = random.randint(10 ,35)
            
            Length_of_snake += 1 #score

            if Length_of_snake == 5:
                level +=1       #меняем скорость и уровень змеи, аннулируем score
                snake_speed +=2
                Length_of_snake = 1


        
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()