import pygame
from sys import exit
from random import randint

# --- FUNCTIONS ---
# --- FUNCTIONS ---
def display_score(score):
    # Calculate score using milliseconds instead of seconds so it ticks up faster
    #score_value = (pygame.time.get_ticks() - start_time) // 100 
    
    score_surface = text_font.render(f'Score: {score}', False, (0, 0, 0))
    score_rect = score_surface.get_rect(midtop=(700, 90))
    screen.blit(score_surface, score_rect)

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy in enemy_list:
            enemy['rect'].x -= 7  # Slightly faster for challenge
            screen.blit(plane_surface, enemy['rect'])
        
        # Remove enemies that go off screen
        enemy_list = [enemy for enemy in enemy_list if enemy['rect'].x > -400]
        return enemy_list
    return []

def collisions(player_rect, player_mask, enemy_list):
    if enemy_list:
        for enemy in enemy_list:
            enemy_rect = enemy['rect']
            offset = (enemy_rect.x - player_rect.x, enemy_rect.y - player_rect.y)
            if player_mask.overlap(plane_mask, offset):
                #death_sound.play()
                return False
    return True

# --- INITIALIZATION ---
pygame.init()
screen = pygame.display.set_mode((1400, 770))
clock = pygame.time.Clock()
pygame.display.set_caption('Catching Rabbit')
text_font = pygame.font.Font('/Users/phamceline/Downloads/pixeltype/Pixeltype.ttf', 120)

# --- SOUNDS ---
# Replace these paths with your actual sound files (.wav or .mp3)
#
# bg_music = pygame.mixer.Sound('/Users/phamceline/Downloads/music.mp3')
# bg_music.play(loops = -1)

# --- SURFACES ---
sky_surface = pygame.image.load('/Users/phamceline/Downloads/sky.jpg').convert()
ground_surface = pygame.image.load('/Users/phamceline/Downloads/gr270.png').convert()

rabbit_surface = pygame.image.load('/Users/phamceline/Downloads/rabbit.png').convert_alpha()
plane_surface = pygame.image.load('/Users/phamceline/Downloads/wolf1.png').convert_alpha()

rabbit_die = pygame.image.load('/Users/phamceline/Downloads/rabbit_die.png').convert_alpha()
rabbit_die = pygame.transform.scale(rabbit_die,(1600,1600))
rabbit_die_rect = rabbit_die.get_rect(center=(280,400))

# --- SCALING ---
sky_surface = pygame.transform.scale(sky_surface, (1400, 500))
ground_surface = pygame.transform.scale(ground_surface, (1400, 270))
rabbit_surface = pygame.transform.scale(rabbit_surface, (650, 650))
plane_surface = pygame.transform.scale(plane_surface, (150,150))

# --- RECTS & MASKS ---
rabbit_rect = rabbit_surface.get_rect(midbottom=(300, 680))
rabbit_mask = pygame.mask.from_surface(rabbit_surface)
plane_mask = pygame.mask.from_surface(plane_surface)

# --- UI ELEMENTS ---
rabbit_start = pygame.transform.scale(rabbit_surface, (1600, 1600)) # Reusing scaled rabbit
rabbit_start_rect = rabbit_start.get_rect(center=(700, 100))

text_start1 = text_font.render('Hoody Bestie!!', False, (0, 0, 0))
text_start1_rect = text_start1.get_rect(midbottom=(700, 150))
text_start2 = text_font.render('Press Space to Start', False, (0, 0, 0))
text_start2_rect = text_start2.get_rect(center=(700, 600))
text_die1 = text_font.render('Game over !!', False,(0,0,0) )
text_die1_rect = text_die1.get_rect(midbottom=(700,150))
text_die2 = text_font.render('Press Space to Start', False, (0, 0, 0))
text_die2_rect = text_die2.get_rect(center=(700, 650))

# --- GAME VARIABLES ---
start_time = 0
score = 0
rabbit_gravity = 0
game_active = False
enemy_list = []
bg_scroll = 0

# --- TIMERS ---
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

# --- MAIN LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and rabbit_rect.bottom >= 680:
                    rabbit_gravity = -25
                   # jump_sound.play()
            
            if event.type == enemy_timer:
                enemy_rect = plane_surface.get_rect(midbottom=(randint(1400,1700),545))
                enemy_list.append({"rect": enemy_rect, "scored": False})        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_list.clear() # Clear old planes
                rabbit_rect.midbottom = (300, 680)
                rabbit_gravity = 0
                start_time = int(pygame.time.get_ticks() / 1000)
                score=0

    if game_active:
        # Scrolling Background logic
        bg_scroll -= 2
        if bg_scroll <= -1400: bg_scroll = 0
        
        screen.blit(sky_surface, (bg_scroll, 0))
        screen.blit(sky_surface, (bg_scroll + 1400, 0))
        screen.blit(ground_surface, (0, 500))

        # Score
        display_score(score)

        # Player Physics
        rabbit_gravity += 1
        rabbit_rect.y += rabbit_gravity
        if rabbit_rect.bottom >= 680: rabbit_rect.bottom = 680
        screen.blit(rabbit_surface, rabbit_rect)

        # Enemies
        old_enemy_count = len(enemy_list)
        enemy_list = enemy_movement(enemy_list)

        if len(enemy_list) < old_enemy_count:
            score+=1

        # Collision logic
        game_active = collisions(rabbit_rect, rabbit_mask, enemy_list)

    else:
        screen.fill((249, 224, 252))
        if score == 0:
            screen.blit(rabbit_start, rabbit_start_rect)
            screen.blit(text_start1, text_start1_rect)
            screen.blit(text_start2, text_start2_rect)
        else:
            # Game Over Screen
            score_msg = text_font.render(f'Final Score: {score}', False, (0, 0, 0))
            score_msg_rect = score_msg.get_rect(center=(700, 530))
            screen.blit(text_die1, text_die1_rect) # "Game Over" feel
            screen.blit(score_msg, score_msg_rect)
            screen.blit(text_die2, text_die2_rect)
            screen.blit(rabbit_die,rabbit_die_rect)

    pygame.display.update()
    clock.tick(60)