import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tutorial game')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
FPS = 60 
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BULLET_VEL = 7
MAX_BULLETS = 100

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90 )

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", 'space.png')), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
     WIN.blit(SPACE, (0, 0))
     pygame.draw.rect(WIN, BLACK, BORDER)
     red_health_text = HEALTH_FONT.render('Health: ' + str(red_health), 1, WHITE)
     yellow_health_text = HEALTH_FONT.render('Health: ' + str(yellow_health), 1, WHITE)
     WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10 ))
     WIN.blit(yellow_health_text, (10, 10))
     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) 
     WIN.blit(RED_SPACESHIP, (red.x, red.y))

     for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    
     for bullet in yellow_bullets:
        pygame.draw.rect(WIN, PURPLE, bullet) 

     pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
            yellow.x -=  VEL
    if keys_pressed[pygame.K_d]and yellow.x + VEL + yellow.width < BORDER.x :
            yellow.x += VEL
    if keys_pressed[pygame.K_w]and yellow.y - VEL > 0:
            yellow.y -= VEL
    if keys_pressed[pygame.K_s]and yellow.y + VEL + yellow.height < HEIGHT - 10 :
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]and red.x - VEL > BORDER.x + BORDER.width:
            red.x -=  VEL
    if keys_pressed[pygame.K_RIGHT]and red.x + VEL + red.width < WIDTH :
            red.x += VEL
    if keys_pressed[pygame.K_UP]and red.y - VEL > 0:
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN]and red.y + VEL + red.height < HEIGHT - 10 :
            red.y += VEL


def  handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)



def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10


    clock = pygame.time.Clock()
    #this code handles being able to exit the game window without using a force quit
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)   
       
       
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)



        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()


if __name__ == '__main__':
    main()

                