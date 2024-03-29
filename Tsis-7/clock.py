import pygame
import datetime

pygame.init()


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect


def calculate_angle_from_noon():
    now = datetime.datetime.now()

    minute = now.minute
    second = now.second

    # Calculate the position of the minute and second hand
    minute_position = (minute / 60) * 360 *(-1)
    second_position = (second / 60) * 360 *(-1)

    return minute_position, second_position
#Standard Settings
height , width = 600 , 600
screen = pygame.display.set_mode((height , width))
pygame.display.set_caption("Mickey Clock")

#загружаем изображения в переменные
mickey = pygame.image.load('clock_mouse\clock.png')
hand1 = pygame.image.load('clock_mouse\h1.png')
hand2 = pygame.image.load('clock_mouse\h2.png')

#Утверждаем размеры данных фото
mickey = pygame.transform.scale(mickey , (height , width))
h1 = pygame.transform.scale(hand1 , (height/2 , width/2))
h2 = pygame.transform.scale(hand2 , (height/2 , width/2))
# pos = (height/2 , width/2)
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    minangle , secangle = calculate_angle_from_noon() #Нахождение точного угла между 12 и стрелкой

    rot_hand, x = rot_center(h1, minangle, height / 2, width/ 2) #центрирование и поворот изображения
    rot_hand1, y = rot_center(h2, secangle, height / 2, width / 2)

    #Ставка изображений поверх экрана
    screen.blit(mickey, (0, 0))
    screen.blit(rot_hand, x)
    screen.blit(rot_hand1, y)

    pygame.display.flip()

pygame.quit()
