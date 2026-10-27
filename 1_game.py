import pygame 
import sys
import random 

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("BALl DODGE")

#colour (red,green,blue)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)

# player setup
player_x=370
player_y=550
player_width=90 
player_height=30
player_speed=7

# Ball setup 
ball_radius_1=15
ball_x_1=random.randint(0,800-ball_radius_1)
ball_y_1=0
ball_speed_1=5

ball_radius_2=15
ball_x_2=random.randint(0,800-ball_radius_2)
ball_y_2=0
ball_speed_2=6

ball_radius_3=15
ball_x_3=random.randint(0,800-ball_radius_3)
ball_y_3=0
ball_speed_3=8


clock=pygame.time.Clock()
font=pygame.font.SysFont(None,60)

game_over=False

# game loop 
while True :
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
    if(not game_over):
        # to move player 
        key=pygame.key.get_pressed()
        if(key[pygame.K_LEFT]):
            player_x-=player_speed
        elif(key[pygame.K_RIGHT]):
            player_x+=player_speed
        # to keep player inside screen 
        if(player_x>800-player_width):
            player_x=800-player_width
        if(player_x<0):
            player_x=0

        # ball moving 
        ball_y_1+=ball_speed_1
        ball_y_2+=ball_speed_2
        ball_y_3+=ball_speed_3

        # to get ball restart 
        if(ball_y_1>600):
            ball_y_1=0
            ball_x_1=random.randint(0,800-ball_radius_1)
        if(ball_y_2>600):
            ball_y_2=0
            ball_x_2=random.randint(0,800-ball_radius_2)
        if(ball_y_3>600):
            ball_y_3=0
            ball_x_3=random.randint(0,800-ball_radius_3)

        # if they crash with each other 
        if (ball_y_1 + ball_radius_1 >= player_y and ball_x_1 + ball_radius_1 >= player_x and ball_x_1 - ball_radius_1 <= player_x + player_width):
            game_over = True
        if (ball_y_2 + ball_radius_2 >= player_y and
            ball_x_2 + ball_radius_2 >= player_x and
            ball_x_2 - ball_radius_2 <= player_x + player_width):
                game_over = True

        if (ball_y_3 + ball_radius_3 >= player_y and
            ball_x_3 + ball_radius_3 >= player_x and
            ball_x_3 - ball_radius_3 <= player_x + player_width):
                game_over = True
        screen.fill(white)
        pygame.draw.rect(screen,blue,(player_x,player_y,player_width,player_height))
        pygame.draw.circle(screen,red,(ball_x_1,ball_y_1),ball_radius_1)
        pygame.draw.circle(screen,red,(ball_x_2,ball_y_2),ball_radius_2)
        pygame.draw.circle(screen,red,(ball_x_3,ball_y_3),ball_radius_3)
    else:
        screen.fill(black)
        text=font.render("Game Over!",True,red)
        screen.blit(text,(400,300))
    pygame.display.flip()
    clock.tick(60)