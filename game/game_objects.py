import pygame

from settings import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    max_speed = 10
    jump_speed = 7
    def __init__(self, image, image2, ch, WIDTH, HEIGHT):
        super(Player, self).__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT - 10

        self.current_x = 0
        self.current_y = 0

# Кулдаун
        self.last = pygame.time.get_ticks()
        self.cooldown = 1000


# Аргументы в update
        self.tut = image2
        self.tam = image
        self.number = ch
        self.p_now = 1

# Платформы и кнопки

    def update(self, choosen_player):
        keys = pygame.key.get_pressed()

        #self.coller = players_colided

        if choosen_player == 1:
            self.p_now = 1
        if choosen_player == 2:
            self.p_now = 2
        if choosen_player == 3:
            self.p_now = 3


        #print(self.coller)
        self.current_y = 6


# Движения
        if choosen_player == self.number:
            if keys[pygame.K_LEFT] and self.rect.centerx > 39:
                self.current_x = - self.max_speed
            elif keys[pygame.K_RIGHT] and self.rect.centerx < 769:
                self.current_x = self.max_speed
            elif keys[pygame.K_UP]:
                self.jump()
            else:
                self.current_x = 0


            self.image = pygame.image.load(self.tut)
        if choosen_player != self.number:
            self.image = pygame.image.load(self.tam)
            self.current_x = 0


# Антибаг с пролетанием за границы карты прыжком
        if self.rect.centerx < 30:
            self.rect.centerx = 40
        elif self.rect.centerx > 780:
            self.rect.centerx =768
        elif self.rect.y < 50:
            self.rect.y = 200

        #print('x - ', self.current_x)
        #print('y - ', self.current_y)

        if choosen_player is not self.number:
                self.current_x = 0

        self.rect.move_ip((self.current_x, self.current_y))

    def jump(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.current_y = -105

# Столкновения игроков
    def collide(self, p2, p3):

        ps = [p2, p3]
        for item in ps:
            if pygame.sprite.collide_rect(self, item):

                if self.current_x > 0 and self.current_y == 0:
                    self.rect.right = item.rect.left
                elif self.current_x < 0 and self.current_y == 0:
                    self.rect.left = item.rect.right
                elif self.current_y > 0:
                    self.current_y = 0
                    self.rect.bottom = item.rect.top
                elif self.current_y < 0:
                    self.rect.top = item.rect.bottom
                    self.current_y = 0


# Столкновения игрока о платформы
    def collide_platforms(self, platformz):
        for item in platformz:
            if pygame.sprite.collide_rect(self, item):
                if self.current_x > 0 and self.current_y == 0:
                    self.rect.right = item.rect.left
                    self.rect.centerx = self.rect.centerx - 10
                elif self.current_x < 0 and self.current_y == 0:
                    self.rect.left = item.rect.right
                elif self.current_y > 0:
                    self.rect.bottom = item.rect.top
                    self.current_y = 0
                elif self.current_y < 0:
                    self.current_y = 0
                    self.rect.top = item.rect.bottom

# Столкновения с юзабельными платформами
    def collide_u_platforms(self, group):
        if pygame.sprite.spritecollide(self, group, False):
            self.rect.centerx = self.rect.centerx - 10
class Platform(pygame.sprite.Sprite):
    def __init__(self, image, WIDTH, HEIGHT):
        super(Platform, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT

class HitPlatform(pygame.sprite.Sprite):
    def __init__(self, image, WIDTH, HEIGHT):
        super(HitPlatform, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT

class UsablePlatform(pygame.sprite.Sprite):
    def __init__(self, image, WIDTH, HEIGHT, change, p_num, znak):
        super(UsablePlatform, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT
        self.b_num = p_num
        self.pressed = 0
        self.nu_znak = znak
        self.nu_change = change
    def update(self):
        print('self b_num', self.b_num)
        print('self pressed', self.pressed)

        if self.b_num == self.pressed:
            if self.nu_znak:
                self.rect.centery = self.nu_change
            elif not self.nu_znak:
                self.rect.centery = self.nu_change
        else:
            self.rect.centery = self.rect.centery

        print(self.nu_znak)
        #if self.b_num != self.pressed:
        #    self.rect.centery = HEIGHT

    def activated(self, num):
        self.pressed = num

class Button(pygame.sprite.Sprite):
    def __init__(self, image, WIDTH, HEIGHT):
        super(Button, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT
        self.been_activated = False

    def collide(self, group, obj, number):
        if pygame.sprite.spritecollide(self, group, False):
            print('button activated - ', number)
            obj.activated(number)
            self.been_activated = True
        else:
            print('not button')
            obj.activated(0)

        if self.been_activated:
            self.image = pygame.image.load('assets/button_0.png')
class Background(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super(Background, self).__init__()

        self.image = pygame.image.load('assets/Background.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH
        self.rect.y = HEIGHT
