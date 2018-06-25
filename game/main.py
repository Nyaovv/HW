import pygame
import sys

from settings import RESOLUTION
from game_objects import Player, Platform, UsablePlatform, HitPlatform, Button, Background

pygame.init()
pygame.display.set_caption('Pygame Monster')

screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Game objects
player1 = Player('assets/player1.png', 'assets/player1_0.png', 1, 50, 510)
player2 = Player('assets/player2.png', 'assets/player2_0.png', 2, 120, 510)
player3 = Player('assets/player3.png', 'assets/player3_0.png', 3, 200, 510)

background = Background(400, 300)

# Уровень - платформы
platform1 = Platform('assets/platforms/platform1.png', 400, 600) # пол
#platform2 = Platform('assets/platforms/platform2.png', 320, 100)
platform3 = Platform('assets/platforms/platform1.png', 400, 0)   # потолок
platform4 = Platform('assets/platforms/platform4.png', 290, 400)
#platform5 = Platform('assets/platforms/platform5.png', 550, 150)
platform6 = Platform('assets/platforms/platform6.png', 520, 399)
platform7 = Platform('assets/platforms/platform7.png', 770, 450)

# HitPlatforms (debug)
hit_platform1 = HitPlatform('assets/platforms/platform2_0.png', 320, 100)
hit_platform2 = HitPlatform('assets/platforms/platform5_0.png', 550, 150)

# Уровень - активируемые
u_platform1 = UsablePlatform('assets/usable_platforms/platform1.png', 320, 355, 300, 1, True)
u_platform2 = UsablePlatform('assets/usable_platforms/platform2.png', 320, 475, 600, 2, True)
u_platform3 = UsablePlatform('assets/usable_platforms/platform1.png', 500, 445, 570, 3, False)
u_platform4 = UsablePlatform('assets/usable_platforms/platform1.png', 500, 503, 570, 4, False)
u_platform5 = UsablePlatform('assets/platforms/victory.png', 400, -500, 300, 5, False)


# Уровень - Кнопки
button1 = Button('assets/button.png', 270, 372)
button2 = Button('assets/button.png', 440, 521)
button3 = Button('assets/button.png', 500, 370)
button4 = Button('assets/button.png', 600, 521)
final = Button('assets/door.png', 768, 306)


# Groups
playerss = pygame.sprite.Group()
playerss.add(player1, player2, player3)


platformss = pygame.sprite.Group()
platformss.add(platform1, platform3, platform4,
                platform6, platform7)


hit_platforms = pygame.sprite.Group()
hit_platforms.add(hit_platform1, hit_platform2)

u_platformss = pygame.sprite.Group()
u_platformss.add(u_platform1, u_platform2, u_platform3, u_platform4, u_platform5)


buttons = pygame.sprite.Group()
buttons.add(button1, button2, button3, button4, final)

back = pygame.sprite.Group()
back.add(background)

# ~~~
keys = pygame.key.get_pressed()
global choosen_player
choosen_player = 1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)

# Выбор игрока
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if choosen_player == 1:
                    choosen_player = 2
                    print('Pink ', choosen_player)

                elif choosen_player == 2:
                    choosen_player = 3
                    print('Blue ', choosen_player)

                elif choosen_player == 3:
                    choosen_player = 1
                    print('Green', choosen_player)
    """
    col_p1_p2 = pygame.sprite.collide_rect(player1, player2)
    col_p1_p3 = pygame.sprite.collide_rect(player1, player3)
    col_p2_p3 = pygame.sprite.collide_rect(player2, player3)

    if col_p1_p2:
        print('col_p1_p2 ', col_p1_p2)
    if col_p1_p3:
        print('col_p1_p3', col_p1_p3)
    if col_p2_p3:
        print('col_p2_p3', col_p2_p3)
    """
    screen.fill((135, 106, 105))

    player1.update(choosen_player)
    player2.update(choosen_player)
    player3.update(choosen_player)

    #for player in playerss:
    #    player.collide(playerss)

    player1.collide(player2, player3)
    player2.collide(player1, player3)
    player3.collide(player1, player2)

    player1.collide_platforms(platformss)
    player2.collide_platforms(platformss)
    player3.collide_platforms(platformss)

    player1.collide_platforms(u_platformss)
    player2.collide_platforms(u_platformss)
    player3.collide_platforms(u_platformss)

    player1.collide_u_platforms(hit_platforms)
    player2.collide_u_platforms(hit_platforms)
    player3.collide_u_platforms(hit_platforms)

    button1.collide(playerss, u_platform1, 1)
    button2.collide(playerss, u_platform2, 2)
    button3.collide(playerss, u_platform3, 3)
    button4.collide(playerss, u_platform4, 4)
    final.collide(playerss, u_platform5, 5)

    u_platform1.update()
    u_platform2.update()
    u_platform3.update()
    u_platform4.update()
    u_platform5.update()

    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)
    screen.blit(player3.image, player3.rect)






    platformss.draw(screen)
    platformss.update()

    hit_platforms.draw(screen)
    hit_platforms.update()

    buttons.draw(screen)
    buttons.update()

    back.draw(screen)
    back.update()

    u_platformss.draw(screen)
    u_platformss.update()


    #print(pygame.sprite.groupcollide(playerss, playerss, False, False))

    pygame.display.flip()
    clock.tick(30)
