import pygame, sys, time, winsound, math
from pygame.locals import *
import random
import ui
pygame.init()
pygame.mixer.init()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1024

clock = pygame.time.Clock()

SCORE_1 = 0
SCORE_2 = 0

#player 1
UP_PLAYER_1 = False
DOWN_PLAYER_1 = False
STATIC_1 = True
#player 2
UP_PLAYER_2 = False
DOWN_PLAYER_2 = False
STATIC_2 = True


# ball movement
UL = 0 # up and left
DL = 1 # down and left
UR = 2 # up and right
DR = 3 # down and right
music = pygame.mixer.music.load(r'C:\Users\roberts\Desktop\PONG\resources\music.mp3')


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (219, 31, 31)
BLUE = (31, 141, 219)

GAMEWINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))         #set w and h values for main game window
GAMEWINDOW_RECT = GAMEWINDOW.get_rect()

pygame.mouse.set_visible(False)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)    
        self.player = player
        self.image = pygame.Surface([40,100])       # draws the paddles
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 8
    #=-=-=-= paddle for each player =-=-=-=-=-=
    #left
        if self.player == 1:
            self.rect.centerx = GAMEWINDOW.get_rect().left
            self.rect.centerx += 50
    #right        
        elif self.player == 2:
            self.rect.centerx = GAMEWINDOW.get_rect().right     # alligns the paddles for both player  1 and 2, also centers them to the screen y
            self.rect.centerx -=50
        self.rect.centery = GAMEWINDOW.get_rect().centery    

    def movePaddle(self):
        if self.player == 1:
            if UP_PLAYER_1 == True and self.rect.y > 5:
                self.rect.y -= self.speed
            elif DOWN_PLAYER_1 == True and self.rect.bottom < WINDOW_HEIGHT - 5:        # moves the paddles depending on paddle.speed 
                self.rect.y += self.speed
            elif STATIC_1 == True:
                pass        

        if self.player == 2:
            if UP_PLAYER_2 == True and self.rect.y > 5:
                self.rect.y -= self.speed
            elif DOWN_PLAYER_2 == True and self.rect.bottom < WINDOW_HEIGHT - 5:
                self.rect.y += self.speed
            elif STATIC_2 == True:
                pass
        #self.update()      
    #def update(self):
        #self.rect = (self.rect.x, self.rect.y, self.rect.centerx, self.rect.centery)   


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_bord = pygame.Surface([25,25])
        self.image = pygame.Surface([20,20])
        #self.image.fill(lcol)
        self.rect = self.image.get_rect()                              # draws the ball, centers it to screen and sets its direction to random
        self.rect2 = self.image_bord.get_rect()
        self.rect.centerx = GAMEWINDOW_RECT.centerx
        self.rect2.centerx = GAMEWINDOW_RECT.centerx
        self.rect.centery = GAMEWINDOW_RECT.centery
        self.rect2.centery = GAMEWINDOW_RECT.centery
        self.direction = random.randint(0,3)
        self.speed = 5
#UL = 0 # up and left
#DL = 1 # down and left
#UR = 2 # up and right
#DR = 3 # down and right

    def moveBall(self):
        if self.direction == UL:
            self.rect.x -= self.speed
            self.rect2.x -= self.speed
            self.rect.y -= self.speed
            self.rect2.y -= self.speed
        if self.direction == UR:
            self.rect.x += self.speed
            self.rect2.x += self.speed
            self.rect.y -= self.speed       # depending on its diagonal direction it changes its x and y values
            self.rect2.y -= self.speed
        if self.direction == DL:
            self.rect.x -= self.speed
            self.rect2.x -= self.speed
            self.rect.y += self.speed
            self.rect2.y += self.speed
        if self.direction == DR:
            self.rect.x += self.speed
            self.rect2.x += self.speed
            self.rect.y += self.speed
            self.rect2.y +=  self.speed       

    def changeDirection(self):
        if self.rect.y < 0 and self.direction == UL:
            self.direction = DL
            musicPlayPlop()
        if self.rect.y < 0 and self.direction == UR:    # checks if ball touches arena walls and changes its direction accordingly
            self.direction = DR
            musicPlayPlop()
        if self.rect.y > GAMEWINDOW_RECT.bottom and self.direction == DL:
            self.direction = UL
            musicPlayPlop()
        if self.rect.y > GAMEWINDOW_RECT.bottom and self.direction == DR:
            self.direction = UR
            musicPlayPlop()
             
paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()                                                                       # calls class constructor
render_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball)                  # assigns render to variable 

def paddleCol():
    if pygame.sprite.collide_rect(ball, paddle2):
        if ball.rect.top >= paddle2.rect.bottom:
            if (ball.direction == UR):
                ball.direction = DR
            elif (ball.direction == DR):                        # checks for collisions with paddles and changes ball direction
                ball.direction = UR
        else:    
            if (ball.direction == UR):
                ball.direction = UL
            elif (ball.direction == DR):                        # checks for collisions with paddles and changes ball direction
                ball.direction = DL
        musicPlayBeep()
        if not ball.speed > 20:
            ball.speed +=1                                  # checks for speed, max speed cap = 19, increase speed while not 19
            paddle1.speed +=1    
    elif pygame.sprite.collide_rect(ball, paddle1):
        print(ball.rect.bottom , paddle1.rect.top)
        if ball.rect.top + 20 >= paddle1.rect.bottom:
            if (ball.direction == UL):
                ball.direction = DR
        elif ball.rect.bottom <= paddle1.rect.top + 20:
            if (ball.direction == DL):
                ball.direction = UR
        else:            
            if (ball.direction == UL):
                ball.direction = UR
            elif (ball.direction == DL):
                ball.direction = DR
        musicPlayBeep()
        if not ball.speed > 20:
            ball.speed +=1
            paddle1.speed +=1     


def musicPlayBeep():
    pygame.mixer.music.load(r'C:\Users\roberts\Desktop\PONG\resources\beep.ogg')    
    pygame.mixer.music.play()
def musicPlayPlop():
    pygame.mixer.music.load(r'C:\Users\roberts\Desktop\PONG\resources\plop.ogg')        # loads game sounds
    pygame.mixer.music.play()    
def musicPlayGoal():
    pygame.mixer.music.load(r'C:\Users\roberts\Desktop\PONG\resources\goal.ogg')    
    pygame.mixer.music.play()  

basic_font = pygame.font.SysFont("ArcadeClassic", 120)

INIT_ERRORS = pygame.init()
pygame.display.set_caption('PONG')
if INIT_ERRORS[1] > 0:
    print(f"[!] {INIT_ERRORS} errors launching the game, now exiting.. ")
    pygame.quit()
else:
    print("[!] Game succesfully launched!")
#-=-=-=-=-=- AI -=-=-=-=-=-=

def AI():


    if ball.rect.right > WINDOW_WIDTH / 4:
        if ball.direction == DL or ball.direction == DR:
            paddle2.speed = ball.speed
            paddle2.rect.y = (paddle2.rect.y + paddle2.speed)       
        elif ball.direction == UL or ball.direction == UR:
            paddle2.speed = ball.speed
            paddle2.rect.y = (paddle2.rect.y - paddle2.speed)                   # basic AI for player 2

        if paddle2.rect.bottom > WINDOW_HEIGHT - 5:
            paddle2.rect.bottom = 590
        elif paddle2.rect.top < 0:
            paddle2.rect.top = 0    





#-=-=-=-= MAIN GAME LOOP -=-=-=-=--==
#music = pygame.mixer.Sound(r'C:\Users\roberts\Desktop\PONG\resources\music.wav') 
#pygame.mixer.music.play(-1)
while True:
    clock.tick(60)
    posIndex= 0
    txm = int(round(time.time() * 1000)) / 100  # bigger the divider the slover is radian
    lr = math.sin(math.radians(0   + 360 / len(GAMEWINDOW_RECT) * posIndex + txm)) * 127.5 + 127.5
    lg = math.sin(math.radians(120 + 360 / len(GAMEWINDOW_RECT) * posIndex + txm)) * 127.5 + 127.5      # draws background color using radians
    lb = math.sin(math.radians(240 + 360 / len(GAMEWINDOW_RECT) * posIndex + txm)) * 127.5 + 127.5
    posIndex = posIndex + 1
    lcol = pygame.Color(int(lr), int(lg), int(lb))
    # if a player scores , centers ball back to the center
    # player2 goal
    if (ball.rect.x > WINDOW_WIDTH):
        ball.rect.centerx = GAMEWINDOW_RECT.centerx
        ball.rect2.centerx = ball.rect.centerx
        ball.rect.centery = GAMEWINDOW_RECT.centery             # if a player scores, re centers the ball and sets its dir to random, also resets all speeds from previous round
        ball.rect2.centery = ball.rect.centery
        ball.direction = random.randint(0, 1)
        ball.speed = 5
        paddle1.speed = 8
    # pplayer 1 goal    
    elif (ball.rect.x < 0):
        ball.rect.centerx = GAMEWINDOW_RECT.centerx
        ball.rect2.centerx = ball.rect.centerx
        ball.rect.centery = GAMEWINDOW_RECT.centery             
        ball.rect2.centery = ball.rect.centery
        ball.direction = random.randint(2, 3)
        ball.speed = 5
        paddle1.speed = 8

    # key logging    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()  
            elif event.key == ord('w'):             # player 1 = w - up , s - down       player 2 = arrow_key_up - up, arrow_key_down - down
                UP_PLAYER_1 = True
                DOWN_PLAYER_1 = False
                STATIC_1 = False
            elif event.key == ord('s'):             # player 1 keypress, logs keys while keys are held down
                UP_PLAYER_1 = False
                DOWN_PLAYER_1 = True
                STATIC_1 = False
            elif event.key == pygame.K_UP:
                UP_PLAYER_2 = True
                DOWN_PLAYER_2 = False
                STATIC_2 = False
            elif event.key == pygame.K_DOWN:
                UP_PLAYER_2 = False
                DOWN_PLAYER_2 = True
                STATIC_2 = False 

        elif event.type == KEYUP:
            if event.key == ord('w') or event.key == ord('s'):
                UP_PLAYER_1 = False
                DOWN_PLAYER_1 = False
                STATIC_1 = True 
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:            # if player stops holding down a key, paddles are set to static pos depending on their last pos
                UP_PLAYER_2 = False
                DOWN_PLAYER_2 = False
                STATIC_2 = True
# -=-=-=-=-==-=- DRAW GAME -=-=-=--=
    score_board = basic_font.render(str(SCORE_1) + "           " + str(SCORE_2), True, WHITE)           # sets scoreboard values to variables, also centers it
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = GAMEWINDOW_RECT.centerx 
    #paddle2.rect.y = (ball.rect.y - random.randint(80,90))#random.randint(30,40)
               
    #paddle1.rect.centery = ball.rect.centery - 35
    paddle2.rect.centery = ball.rect.centery - 35
    #if paddle1.rect.bottom > 599:
        #paddle1.rect.bottom = 600
    ball.image.fill(lcol)
    ball.image_bord.fill(WHITE)    
        
    pygame.draw.line(GAMEWINDOW, WHITE, ((WINDOW_WIDTH//2), WINDOW_HEIGHT), ((WINDOW_WIDTH//2), 0), 6)              # center game line
    paddle1.image.fill(RED)
    paddle2.image.fill(BLUE)
    GAMEWINDOW.fill(BLACK)                                           # background fill
    GAMEWINDOW.blit(score_board, score_board_rect) 
    GAMEWINDOW.blit(ball.image_bord, ball.rect2)                     #scoreboard draw
    #pygame.Color(108, 219, 57)
    render_sprites.draw(GAMEWINDOW)                                         # draws ball and paddles 
    #AI()
    paddle1.movePaddle()
    paddle2.movePaddle()
    ball.moveBall()
    ball.changeDirection()
    paddleCol()
    
    
    if ball.rect.x > WINDOW_WIDTH:
        SCORE_1 +=1                                         #if a player scores, adds score
        musicPlayGoal()
    elif ball.rect.x < 0:
        SCORE_2 +=1
        musicPlayGoal()
    #print(ball.speed)
    
    
    
    pygame.display.set_caption("fps: " + str(round(clock.get_fps(), 0)) + " PONG")
    pygame.display.update()   