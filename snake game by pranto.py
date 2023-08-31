import pygame
import random
import os

pygame.mixer.init()




pygame.init()


#creating window
screen_width=1000
screen_height=500
gameWindow=pygame.display.set_mode((screen_width,screen_height))
#background image
#bgimg = pygame.image.load("background.jpg")
#bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
#game title
pygame.display.set_caption(" Snakes by Pranto ")
pygame.display.update()
#game variable
clock=pygame.time.Clock()

score=0
#colors
white=(	144, 238, 144)
red=(255,0,0)
black=(30,30,30)
yellow=(255, 255, 0)
orange=(255, 191, 0)

font=pygame.font.SysFont(None,30)



def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.circle(gameWindow, color,[ x, y],13)
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to SNAKES BY PRANTO",black,screen_width/2-150,screen_height/2-25)
        text_screen("Press SPACE BAR to Play",black,screen_width/2-110,screen_height/2+10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_SPACE:

                   gameloop()
        pygame.display.update()
        clock.tick(60)
#creating game loop
def gameloop():
    # game variable
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    snake_size = 20

    #check if hiscore file exists
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")


    with open("highscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(50, screen_width - 50)
    food_y = random.randint(30, screen_height - 30)

    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    fps = 120
    score = 0


    snk_list = []
    snk_lenght = 1

    food_color=red
    snake_color=black



    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game over! Press ENTER to continue",black,screen_width/2-150,screen_height/2)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_x =0
                        velocity_y=-init_velocity
                    if event.key==pygame.K_DOWN:
                        velocity_x =0
                        velocity_y =init_velocity

                    #if event.key==pygame.K_c:
                        #score+=20
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10

                snk_lenght +=5
                food_x = random.randint(50, screen_width - 50)
                food_y = random.randint(30, screen_height - 30)
                if score>int(hiscore):
                    hiscore=score


            gameWindow.fill(white)
            #gameWindow.blit(bgimg, (0, 0))
            text_screen("score :" + str(score)+" Highscore :"+str(hiscore), red, 5, 5)
            pygame.draw.circle(gameWindow,food_color,[food_x,food_y],10)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True


            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,snake_color,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
