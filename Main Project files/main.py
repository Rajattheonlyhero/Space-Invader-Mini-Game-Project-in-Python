import pygame
import random
import math
from pygame import mixer

# initialisation very important
pygame.init()

# creating the Screen Window
screen = pygame.display.set_mode((700, 600))
playsound = True
# background
backgroundImg = pygame.image.load('background.jpg')
# Title & icon
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# music
mixer.music.load('background.wav')
mixer.music.play(-1)

# player
PlayerImg = pygame.image.load('space-invaders.png')
PlayerX = 320
PlayerY = 480
PlayerX_change = 0

# Enemy_list
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 2

EnemyImg1 = []
EnemyX1 = []
EnemyY1 = []
EnemyX_change1 = []
EnemyY_change1 = []
num_of_enemies1 = 2

EnemyImg2 = []
EnemyX2 = []
EnemyY2 = []
EnemyX_change2 = []
EnemyY_change2 = []
num_of_enemies2 = 2

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('monsters.png'))
    EnemyX.append(random.randint(0, 668))
    EnemyY.append(random.randint(50, 150))
    EnemyY_change.append(40)
    EnemyX_change.append(4)

for i in range(num_of_enemies1):
    EnemyImg1.append(pygame.image.load('monster2.png'))
    EnemyX1.append(random.randint(0, 668))
    EnemyY1.append(random.randint(50, 150))
    EnemyY_change1.append(40)
    EnemyX_change1.append(4)

for i in range(num_of_enemies2):
    EnemyImg2.append(pygame.image.load('monster3.png'))
    EnemyX2.append(random.randint(0, 668))
    EnemyY2.append(random.randint(50, 150))
    EnemyY_change2.append(40)
    EnemyX_change2.append(4)

# bullet
bulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletY_change = 10
BulletX_change = 0
Bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 15
textY = 15

# game_over text
game_over_font = pygame.font.Font('Copperplate Gothic Bold Regular.ttf', 72)
final_score_font = pygame.font.Font('Copperplate Gothic Bold Regular.ttf', 25)
wanna_play_again = pygame.font.Font('Copperplate Gothic Bold Regular.ttf', 25)

def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def enemy1(x, y, i):
    screen.blit(EnemyImg1[i], (x, y))


def enemy2(x, y, i):
    screen.blit(EnemyImg2[i], (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(EnemyX, EnemyY, BulletX, BulletY):
    collision = math.sqrt((math.pow((EnemyX - BulletX), 2)) + math.pow((EnemyY - BulletY), 2))
    if collision <= 27:
        return True
    else:
        return False


def isCollision1(EnemyX1, EnemyY1, BulletX, BulletY):
    collision1 = math.sqrt((math.pow((EnemyX1 - BulletX), 2)) + math.pow((EnemyY1 - BulletY), 2))
    if collision1 <= 27:
        return True
    else:
        return False


def isCollision2(EnemyX2, EnemyY2, BulletX, BulletY):
    collision2 = math.sqrt((math.pow((EnemyX2 - BulletX), 2)) + math.pow((EnemyY2 - BulletY), 2))
    if collision2 <= 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    global playsound
    game_over_text = game_over_font.render("GAME OVER ", True, (255, 255, 255))
    final_score_text = final_score_font.render("FINAL SCORE :"+str(score_value), True, (255, 255, 255))
    screen.blit(game_over_text, (118, 345))
    screen.blit(final_score_text, (250,325))
    pygame.mixer.music.stop()
    if playsound:
        gameover_sound = mixer.Sound('smb_mariodie.wav')
        mixer.Sound.play(gameover_sound)
        playsound = False
    wanna_play_again_text = wanna_play_again.render("Press Enter to play again ", True, (255, 255, 255))
    screen.blit(wanna_play_again_text, (180, 450))





# Looping the events inside the game window
running = True
FPS=75
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    # screen background(R,G,B)
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change -= 7
            if event.key == pygame.K_RIGHT:
                PlayerX_change += 7
            if event.key == pygame.K_SPACE:
                bullet_Sound = mixer.Sound('laser.wav')
                mixer.Sound.play(bullet_Sound)
                if Bullet_state == "ready":
                    BulletX = PlayerX
                    fire_bullet(BulletX, BulletY)
            if event.key == pygame.K_RETURN:
                print("Rajat")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    # PlayerX Movememnt boundary
    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 636:
        PlayerX = 636
    # Enemy Movememnt & boundary
    for i in range(num_of_enemies):
        if EnemyY[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
                EnemyY1[j] = 2000
                EnemyY2[j] = 2000
            game_over()
            break
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 4
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 668:
            EnemyX_change[i] = -4
            EnemyY[i] += EnemyY_change[i]

        collision = isCollision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            collision_Sound = mixer.Sound('explosion.wav')
            mixer.Sound.play(collision_Sound)
            BulletY = 480
            Bullet_state = "ready"
            score_value += 1
            print(score_value)
            EnemyX[i] = random.randint(0, 668)
            EnemyY[i] = random.randint(50, 150)
        enemy(EnemyX[i], EnemyY[i], i)

    for i in range(num_of_enemies):
        if EnemyY1[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
                EnemyY1[j] = 2000
                EnemyY2[j] = 2000
            game_over()
            break
        EnemyX1[i] += EnemyX_change1[i]
        if EnemyX1[i] <= 0:
            EnemyX_change1[i] = 4
            EnemyY1[i] += EnemyY_change1[i]
        elif EnemyX1[i] >= 668:
            EnemyX_change1[i] = -4
            EnemyY1[i] += EnemyY_change1[i]

        collision1 = isCollision1(EnemyX1[i], EnemyY1[i], BulletX, BulletY)
        if collision1:
            collision_Sound1 = mixer.Sound('explosion.wav')
            mixer.Sound.play(collision_Sound1)
            BulletY = 480
            Bullet_state = "ready"
            score_value += 1
            print(score_value)
            EnemyX1[i] = random.randint(0, 668)
            EnemyY1[i] = random.randint(50, 150)
        enemy1(EnemyX1[i], EnemyY1[i], i)

    for i in range(num_of_enemies):
        if EnemyY2[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
                EnemyY1[j] = 2000
                EnemyY2[j] = 2000
            game_over()
            break
        EnemyX2[i] += EnemyX_change2[i]
        if EnemyX2[i] <= 0:
            EnemyX_change2[i] = 4
            EnemyY2[i] += EnemyY_change2[i]
        elif EnemyX2[i] >= 668:
            EnemyX_change2[i] = -4
            EnemyY2[i] += EnemyY_change2[i]

        collision2 = isCollision2(EnemyX2[i], EnemyY2[i], BulletX, BulletY)
        if collision2:
            collision_Sound2 = mixer.Sound('explosion.wav')
            mixer.Sound.play(collision_Sound2)
            BulletY = 480
            Bullet_state = "ready"
            score_value += 1
            print(score_value)
            EnemyX2[i] = random.randint(0, 668)
            EnemyY2[i] = random.randint(50, 150)
        enemy2(EnemyX2[i], EnemyY2[i], i)

    # Bullet Movement & boundary
    if BulletY <= 40:
        BulletY = 480
        Bullet_state = "ready"
    if Bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    player(PlayerX, PlayerY)
    show_score(textX, textY)
    pygame.display.update()
