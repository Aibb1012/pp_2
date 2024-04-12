# paint22

import pygame , math
pygame.init()

fps = 5000
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_size = 0
active_color = 'white'
painting = []
current_tool = 'brush'  


#set a colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (34, 139, 34)
yellow = (255, 255, 0)
teal = (0,255,255)
purple = (123, 14, 196)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
right_gray = (80, 80, 80)
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Paint")


#Drawing menu logos
def draw_menu(color, size):
    pygame.draw.rect(screen, gray, [0, 0, WIDTH, 70])
    pygame.draw.rect(screen , right_gray , [WIDTH - 100, 0, 100, HEIGHT])
    xl_brush = pygame.draw.rect(screen, black, [10, 10, 50, 50])
    pygame.draw.circle(screen, white, (35,35), 20)
    l_brush = pygame.draw.rect(screen, black, [70, 10, 50, 50])
    pygame.draw.circle(screen, white, (95,35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, white, (155,35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, white, (215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
    pygame.draw.circle(screen, color, (400,35),30)

    bl = pygame.draw.rect(screen, (0,0,255), [WIDTH - 80, 80, 25, 25])
    rd = pygame.draw.rect(screen, (255,0,0), [WIDTH - 80, 105, 25, 25])
    gr = pygame.draw.rect(screen, (0,255,0), [WIDTH - 80, 130, 25, 25])
    ye = pygame.draw.rect(screen, (255,255,0), [WIDTH - 80, 155, 25, 25])
    tl = pygame.draw.rect(screen, (0,255,255), [WIDTH - 80, 180, 25, 25])
    prp = pygame.draw.rect(screen, (123, 14, 196), [WIDTH - 80, 205, 25, 25])
    wh = pygame.draw.rect(screen, (255,255,255), [WIDTH - 80, 230, 25, 25])  
    blc = pygame.draw.rect(screen, (0,0,0), [WIDTH - 80, 255, 25, 25])

    rhombus_button = pygame.draw.rect(screen , black ,[435 , 10 , 50 , 50])
    pygame.draw.polygon(screen , white ,((460 , 10) ,(435 , 35) ,(460 , 60) , (485 , 35)) , 3)

    rtriang_button = pygame.draw.rect(screen , black ,[487 , 10 , 50 , 50])
    pygame.draw.polygon(screen , white ,((490 , 10) ,(490 , 50) ,(520 , 50)) , 3)

    eqtrian_button = pygame.draw.rect(screen , black ,[541 , 10 , 50 , 50] )
    pygame.draw.polygon(screen , white ,((563 , 10) ,(543 , 50) ,( 583, 50)) , 3)

    circle_button = pygame.draw.rect(screen, black, [250, 10, 50, 50]) 
    pygame.draw.circle(screen, white, (275, 35), 20)
    
    rectangle_button = pygame.draw.rect(screen, black, [310, 10, 50, 50]) 
    pygame.draw.rect(screen, white, [315, 15, 40, 40])  

    color_rect = [bl, rd, gr, ye, tl, prp, wh, blc,eqtrian_button ,rtriang_button,rhombus_button,circle_button, rectangle_button]  
    rgb_list = [blue, red, green, yellow, teal, purple, white, black, None, None , None , None , None] 
    
    return brush_list, color_rect, rgb_list


#main logic to draw a different shape
def draw_painting(paints):
    #Drawing in Loop
    for i in range(len(paints)):
        if paints[i][0] == 'circle':  
            pygame.draw.circle(screen, paints[i][1], paints[i][2], paints[i][3])
        elif paints[i][0] == 'rectangle':  
            pygame.draw.rect(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'rhombus':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'rtriangle':
            pygame.draw.polygon(screen , paints[i][1], paints[i][2])
        elif paints[i][0]=='eqtrian':
            pygame.draw.polygon(screen , paints[i][1] , paints[i][2])
        else:
            pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

running = True
while running:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    #Settings of brush types
    if left_click and mouse[1] > 70:
        if current_tool == 'brush':  
            painting.append((active_color, mouse, active_size))
        elif current_tool == 'circle':  
            painting.append(('circle', active_color, mouse, active_size*3))
        elif current_tool == 'rectangle':  
            rect_width = 4 * active_size  
            rect_height = 4 * active_size 
            rect_x = mouse[0] - active_size  
            rect_y = mouse[1] - active_size  
            painting.append(('rectangle', active_color, pygame.Rect(rect_x, rect_y, rect_width, rect_height)))

        elif current_tool == 'rhombus':
            pos_top = (mouse[0] , mouse[1]-4*active_size)
            pos_right = (mouse[0]+4*active_size , mouse[1])
            pos_bott = (mouse[0], mouse[1]+4*active_size)
            pos_left = (mouse[0]-4*active_size , mouse[1])
            painting.append(('rhombus' , active_color ,(pos_top, pos_right, pos_bott, pos_left)))

        elif current_tool == 'rtriangle':
            top_ = (mouse[0] , mouse[1]-4*active_size)
            buttom_ = (mouse[0]-4*active_size , mouse[1])
            right_ = (mouse[0] , mouse[1])
            painting.append(('rtriangle' , active_color , (top_ , buttom_ , right_)))
            
        elif current_tool == 'eqtrian':
            height = 4*active_size * math.sqrt(3) / 2
            pos1 = (mouse[0] , mouse[1]-height)
            pos2 = (mouse[0] + 4*active_size/2 , mouse[1]+height/2)
            pos3 = (mouse[0] - 4*active_size/2 , mouse[1]+height/2)
            painting.append(('eqtrian' , active_color , (pos1 , pos2 , pos3)))


    draw_painting(painting)
    if mouse[1] > 70 and current_tool == 'brush':  
        pygame.draw.circle(screen, active_color, mouse, active_size)

    brushes, colors, rgbs = draw_menu(active_color, active_size)
         
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #drawing a circle
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            #pick a color and circle        
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    if rgbs[i] is not None:
                        active_color = rgbs[i]
                    else:
                        if i == len(colors) - 2:  
                            current_tool = 'circle' 
                        elif i == len(colors) - 1:  
                            current_tool = 'rectangle' 
                        elif i == len(colors)-3:
                            current_tool = 'rhombus' 
                        elif i == len(colors)-4:
                            current_tool = 'rtriangle'
                        elif i == len(colors)-5:
                            current_tool = 'eqtrian'
    pygame.display.flip()
    
pygame.quit()