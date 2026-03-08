import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = text_font.render(f'Score: {current_time}',False,(0,0,0))
    score_rect = score_surface.get_rect (midtop = (700, 90))
    screen.blit(score_surface, score_rect)
    return current_time

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            screen.blit(plane_surface,enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]
        return enemy_list
    else:
        return []

pygame.init()  # khai bao
screen = pygame.display.set_mode((1400,770))
clock= pygame.time.Clock()
pygame.display.set_caption('catching')
text_font = pygame.font.Font('/Users/phamceline/Downloads/pixeltype/Pixeltype.ttf', 120)

start_time = 0
score = 0

sky_surface = pygame.image.load('/Users/phamceline/Downloads/sky.jpg').convert()
ground_surface = pygame.image.load('/Users/phamceline/Downloads/gr270.png').convert()
# text_surface = text_font.render('My game', False, (0,0,0))

rabbit_surface = pygame.image.load('/Users/phamceline/Downloads/rabbit.png').convert_alpha()

plane_surface = pygame.image.load('/Users/phamceline/Downloads/wolf1.png').convert_alpha()  #enemy

# scale background 
sky_surface = pygame.transform.scale(sky_surface,(1400,500))
ground_surface = pygame.transform.scale(ground_surface,(1400,270))
rabbit_surface = pygame.transform.scale(rabbit_surface,(650,650))
plane_surface = pygame.transform.scale(plane_surface, (140,140))
rabbit_rect = rabbit_surface.get_rect(midbottom=(300,680))  #player


plane_rect = plane_surface.get_rect(midbottom = (1000,100)) # enemy

enemy_list = []

rabbit_gravity = 0
game_active = False

rabbit_mask = pygame.mask.from_surface(rabbit_surface)
plane_mask = pygame.mask.from_surface(plane_surface)

rabbit_start = pygame.image.load('/Users/phamceline/Downloads/rabbit.png').convert_alpha()
rabbit_start = pygame.transform.scale(rabbit_start,(1500,1500))
rabbit_start_rect = rabbit_start.get_rect(center=(700,100))

rabbit_die = pygame.image.load('/Users/phamceline/Downloads/rabbit_die.png').convert_alpha()
rabbit_die = pygame.transform.scale(rabbit_die,(1500,1500))
rabbit_die_rect = rabbit_die.get_rect(center=(280,400))

rocket_surf = pygame.image.load('/Users/phamceline/Downloads/rocket.png').convert_alpha()
rocket = pygame.transform.scale(rocket_surf,(1000,1000))
rocket_rect = rocket.get_rect(center=(500,400))

text_start1 = text_font.render('Hoody  bestie !!', False,(0,0,0))
text_start1_rect = text_start1.get_rect(midbottom = (700,150))
text_start2 = text_font.render('Press  Space  to  start.', False,(0,0,0))
text_start2_rect = text_start2.get_rect( center = (700,600))
text_die1= text_font.render('Game  over.', False,(0,0,0))
text_die1_rect = text_die1.get_rect(midbottom = (700,150))
text_die2 = text_font.render(f'Your  score   is: {score}', False,(0,0,0))
text_die2_rect = text_die2.get_rect( center = (700,600))

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,2000)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and rabbit_rect.bottom == 680:
                  rabbit_gravity = -30

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rabbit_rect.collidepoint(event.pos) and rabbit_rect.bottom == 680:
                    rabbit_gravity = -30
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                plane_rect.left = 1400
                start_time= int(pygame.time.get_ticks() / 1000)
        
        if event.type == enemy_timer and game_active: 
            enemy_list.append(  plane_surface.get_rect(midbottom = (randint(1300,1700),535)))
    
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,500))
        # pygame.draw.rect(screen,'Pink',text_font,10,20)

        # screen.blit(text_surface, text_rect)
        score = display_score()
        rabbit_gravity +=1
        rabbit_rect.y += rabbit_gravity 
        if rabbit_rect.bottom > 680 :
            rabbit_rect.bottom = 680
            rabbit_gravity = 0

        screen.blit(rabbit_surface, rabbit_rect)
        screen.blit(rocket_surf, rocket_rect)


        enemy_rect_list = enemy_movement(enemy_list)

        # screen.blit(plane_surface,plane_rect)
        # plane_rect.x -= 5
        # if plane_rect.right <=0 : plane_rect.left = 1400
        for enemy_rect in enemy_list:
            offset = (enemy_rect.x - rabbit_rect.x, enemy_rect.y - rabbit_rect.y)
            if rabbit_mask.overlap(plane_mask, offset): 
              game_active = False

        # enemy_movement(enemy_rect)
    else:
        game_active
        if score == 0:
            screen.fill ((249,224,252))
            
            screen.blit (rabbit_start,rabbit_start_rect)
            screen.blit(text_start1,text_start1_rect)
            screen.blit(text_start2,text_start2_rect)
        else:
            screen.fill ((249,224,252))
            screen.blit (rabbit_die,rabbit_die_rect)
            screen.blit(text_die1,text_die1_rect)
            text_die2 = text_font.render(f'Your  score is: {score}', False,(0,0,0))
            screen.blit(text_die2,text_die2_rect)

    

    pygame.display.update()
    clock.tick(60) 