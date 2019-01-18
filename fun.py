import random
import pygame
import time
import os
import sys
prog = True
while prog:
    pygame.init()
    def text(screen, text, x, y, size = 50,
                color = (200, 200, 200), font_type = 'comic sans MS'):

                text = str(text)
                font = pygame.font.Font('ufont.ttf', size)
                text = font.render(text, True, color)
                screen.blit(text, (x, y))

    width = 1000
    score = 0
    height = 700
    s = pygame.display.set_mode((width,height))
    #loop
    running = False
    #classes
    class base_sprite(pygame.sprite.Sprite):
            def __init__(self, color=(0,0,0), width=0, height=0, image=None,xk=0,yk=0, scale=None, surface=False):
                pygame.sprite.Sprite.__init__(self)
                if "Surface" in type(image).__name__ or surface:
                    self.image = image
                else:
                    self.image = pygame.image.load(image)
                if scale != None:
                    self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
                pygame.draw.rect(self.image, color, [5000000,5000000,width,height])
                self.rect = self.image.get_rect()
                self.rect.x = xk
                self.rect.y = yk
    #vars
    wait = random.randint(50,100)
    wait1 = random.randint(50,100)
    wait2 = random.randint(50,100)
    wait3 = random.randint(50,100)
    wait4 = random.randint(50,100)
    sptW = 50
    sptH = 100
    y = (height/2 - sptH)
    x = (width/2 - sptW)
    pos = []
    index = 1
    while index < 100:
        cx = random.randint(0,900)
        pos.append(cx)
        index += 1
    spritei = pygame.image.load('images/sprite.png')
    back = pygame.image.load('images/back.png')
    mouth = pygame.image.load('images/mouth.png')
    cokei = pygame.image.load('images/coke.png')
    fantai = pygame.image.load('images/fanta.png')
    blank = pygame.image.load('images/blank.png')
    spriteZeroi = pygame.image.load('images/spriteZero.png')
    minMadei = pygame.image.load('images/minMade.png')
    rootBeeri = pygame.image.load('images/rootBeer.png')
    poweri = pygame.image.load('images/power.png')
    button1i = pygame.image.load('images/button1.png')
    startButtoni = pygame.image.load('images/startButton.png')
    home = pygame.sprite.Group()
    me = pygame.sprite.Group()
    butt = pygame.sprite.Group()
    pre = pygame.sprite.Group()
    xmin = False
    xplus = False
    ymin = False
    yplus = False
    dead = False
    after = False
    spawn = False
    dif = 150
    badY = 0
    bad = [cokei,fantai,]
    badxs = []
    bY = -200
    cY = -200
    dY = 0
    eY = 0
    tempY = 0
    coke = base_sprite(image = cokei, xk = pos[1], yk = tempY)
    fanta = base_sprite(image = fantai, xk = pos[2], yk = bY)
    coke2 = base_sprite(image = spriteZeroi, xk = pos[3], yk = bY)
    rootBeer = base_sprite(image = rootBeeri, xk = pos[4], yk = bY)
    minMade = base_sprite(image = minMadei, xk = pos[5], yk = bY)
    power = base_sprite(image = poweri, xk = pos[6], yk = bY)
    button1 = base_sprite(image = button1i, xk = (width/2) - 100, yk = (height/2)-200)
    startButton = base_sprite(image = startButtoni, xk = (width/2) - 100, yk = (height/2)-200)
    a = bad[random.randint(0, len(bad) -1)]
    b = bad[random.randint(0, len(bad) -1)]
    c = bad[random.randint(0, len(bad) -1)]
    d = bad[random.randint(0, len(bad) -1)]
    e = bad[random.randint(0, len(bad) -1)]
    a1 = False
    b1 = False
    c1 = False
    d1 = False
    e1 = False
    trans = True
    prep = True
    pygame.mixer.init()
    sounda= pygame.mixer.Sound("cool.wav")
    coin = pygame.mixer.Sound('can.wav')
    die = pygame.mixer.Sound('death.wav')
    ending = pygame.mixer.Sound('end.wav')
    fail = pygame.mixer.Sound('fail.wav')

    names = [a, b, c, d, e]
    num = 0
    sprite = base_sprite (image = spritei, xk = x, yk = y)

    while prep:
        s.blit(back,(0,0))
        pre.add(startButton)
        pre.draw(s)

        for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if startButton.rect.collidepoint(event.pos):
                            pre.empty()
                            running = True
                            prep = False
        pygame.display.update()
        pygame.display.flip()
    #main loop
    if running:
        sounda.play()
        me.add(sprite)
        home.add(coke2)
        home.add(rootBeer)
        home.add(minMade)
        home.add(power)
        home.add(coke)
        home.add(fanta)
        home.draw(s)
    while running:

            s.blit(back,(0,0))
            s.blit(mouth,(0,(height-100)))

            spit = None

            tempX = 0
            tempX = random.randint(0, width - 100)
            spawn = False
            chance = 0
            badX = random.randint(0, width - 100)
            #movement
            for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_LEFT):
                                    xmin = True
                            if (event.key == pygame.K_RIGHT):
                                    xplus = True
                            if (event.key == pygame.K_UP):
                                    ymin = True
                            if (event.key == pygame.K_DOWN):
                                    yplus = True

                            else:
                                    None
                    if event.type == pygame.KEYUP:
                            if (event.key == pygame.K_LEFT):
                                    xmin = False
                            if (event.key == pygame.K_RIGHT):
                                    xplus = False
                            if (event.key == pygame.K_UP):
                                    ymin = False
                            if (event.key == pygame.K_DOWN):
                                    yplus = False
                            else:
                                    None

            if xmin:
                    sprite.rect.x -= 10
                    if sprite.rect.x <= 0:
                            sprite.rect.x = 0
            if xplus:
                    sprite.rect.x += 10
                    if sprite.rect.x >=  (width-(sptW*2)):
                            sprite.rect.x = (width - (sptW*2))
            if ymin:
                    sprite.rect.y -= 10
                    if sprite.rect.y <= 0:
                            sprite.rect.y = 0
            if yplus:
                    sprite.rect.y += 10
                    if sprite.rect.y >= ((height - 100)-(sptH*2)):
                            sprite.rect.y = ((height - 100) - (sptH*2))
            #can spawn
            chance = random.randint(0,dif)
            if chance == 72:
                    spawn = True
            val = 1



            a1 = True
            coke.rect.y += 5
            if coke.rect.y > height - 180:
                dead = True


            if a1 and num > wait:

                fanta.rect.y += 5
                b1 = True
                if fanta.rect.y > height- 180:
                    dead = True
            if b1 and num > wait + 50:
                coke2.rect.y += 2
                c1 = True
                if coke2.rect.y > height - 180:
                    score += 5
                    c2x = -100
                    c2y = -500
                    coke2.rect.y = -300
                    coke2.rect.x = random.randint(0, 950)
            if c1 and num > wait2 + 50:
                rootBeer.rect.y += 5
                d1 = True
                if rootBeer.rect.y > height - 180:
                    dead = True

            if d1 and num > wait3 + 50:
                minMade.rect.y += 4
                e1 = True
                if minMade.rect.y > height - 180:
                    dead = True
            if e1 and num > wait4 + 1000:
                power.rect.y += 2
                if power.rect.y > height - 180:
                    dead = True

            col = pygame.sprite.spritecollide(sprite,home,True)
            for i in col:
                if i == coke2:
                    score -= 5
                    fail.play()

            for i in col:
                score += 1
                coin.play()
                home.add(i)
                i.rect.x = random.randint(0, 950)
                i.rect.y = -200
            if score < 0:
                score = 0
            #scoreing
            num += 1
            scr = 'Score: '+str(score)+'!'
            text(s, scr, 700, 0, )

            dt = 'You Died!'
            if dead:

                die.play()
                running = False
                after = True
                sounda.stop()
            home.draw(s)
            me.draw(s)
            pygame.display.update()
            pygame.display.flip()
            if dead:
                prog = False
while after:
    butt.add(button1)
    butt.draw(s)
    text(s, dt, 400, 350)
    for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.rect.collidepoint(event.pos):
                        trans = True
                        running = True
                        after = False
    pygame.display.update()
    pygame.display.flip()
if trans:
    me.empty()
    home.empty()
    butt.empty()
    prog = True
    pygame.quit()
    file = open('fun.py')
    os.execv(file, )
