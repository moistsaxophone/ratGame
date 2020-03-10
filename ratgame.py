#Shop in act2.scene1 is not working going to make it  selector for next version

import pygame
pygame.init()
pygame.mixer.init()

#loading images and sprites beep boop
walkRight = pygame.image.load('sprites/giantratR.png')
walkLeft = pygame.image.load('sprites/giantratL.png')
walkLeftSusej = pygame.image.load('sprites/giantratLsusej.png')
walkRightSusej = pygame.image.load('sprites/giantratRsusej.png')
bg1 = pygame.image.load('bg/bg1.jpg')
bg2 = pygame.image.load('bg/bg2.jpg')
bg3 = pygame.image.load('bg/bg3.png')
bg4 = pygame.image.load('bg/bg4.png')
bg5 = pygame.image.load('bg/bg5.png')
bg6 = pygame.image.load('bg/bg6.png')
malc = pygame.image.load('sprites/malcolm.png')
donkeyKong = pygame.image.load('sprites/donkeykong.png')
malcinv = pygame.image.load('sprites/malcolminv.png')
menuimg = pygame.image.load('bg/mainmenu.png')
credit = pygame.image.load('bg/credits.png')
selector1yes = pygame.image.load('sprites/selecyes.png')
selector1no = pygame.image.load('sprites/selecno.png')
selector1L = pygame.image.load('sprites/selectorL.png')
selector1M = pygame.image.load('sprites/selectorM.png')
selector1R = pygame.image.load('sprites/selectorR.png')
coconutguninv = pygame.image.load('sprites/coconutguninv.png')
coconutimg = pygame.image.load('sprites/coconut.png')
deadGuy = pygame.image.load('sprites/dead.png')
winrar = pygame.image.load('sprites/winrar.png')
zip7 = pygame.image.load('sprites/7zip.png')
zip7inv = pygame.image.load('sprites/7zipinv.png')
obamapng = pygame.image.load('sprites/obama.png')
winrarinv = pygame.image.load('sprites/winrarinv.png')
pac = pygame.image.load('sprites/pukman.png')
pacUp = pygame.image.load('sprites/puckmanUp.png')
swag = pygame.image.load('sprites/susej.png')
dollarimg = pygame.image.load('sprites/dollar.png')
liceimg = pygame.image.load('sprites/lice.png')

#loading music and sounds beep boop
goodjob = pygame.mixer.Sound('music/goodjob.wav')
hyrule = pygame.mixer.Sound('music/hyrule.wav')
dkrap = pygame.mixer.Sound('music/dkrap.wav')
dkrap.set_volume(.6)
matt1 = pygame.mixer.Sound('music/shootyou.wav')
matt1.set_volume(.99)
matt2 = pygame.mixer.Sound('music/firesinspurts.wav')
matt2.set_volume(.66)
matt3 = pygame.mixer.Sound('music/isthatmalcolm.wav')
matt4 = pygame.mixer.Sound('music/coconutgun.wav')
matt5 = pygame.mixer.Sound('music/oof.wav')
log1 = pygame.mixer.Sound('music/log.wav')
iceman1 = pygame.mixer.Sound('music/iceman1.wav')
theend = pygame.mixer.Sound('music/theend.wav')
jesus1 = pygame.mixer.Sound('music/jesus1.wav')
mexico = pygame.mixer.Sound('music/mexico.wav')
mexico.set_volume(.99)
saviomiggyi = pygame.mixer.Sound('music/saviomiggyi.wav')
nomoney = pygame.mixer.Sound('music/nomoney.wav')
hasmoney = pygame.mixer.Sound('music/hasmoney.wav')
moneymiggy = pygame.mixer.Sound('music/moneymiggy.wav')
moneysavio = pygame.mixer.Sound('music/moneysavio.wav')
pygame.mixer.music.load('music/ratsong.mp3')


clock = pygame.time.Clock()

#global variables
screenWidth = 1600
screenHeight = 900
green = (0, 255, 0)
running = True
mainMenu = True
freezeTime = False
intro = False
green = (57, 255, 20)
bg = menuimg

#Draws updates and stores currency
balance = 0
lice = 0
def drawCurrency(win, text, size, x, y):
    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', size)
    text_surface = font.render(text, True, green)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    win.blit(text_surface, text_rect)

#screen
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Rat Game: The Game")

#classes and objects
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.ratJump = False
        self.jumpCount = 10

    #detects if player is pressing right or left
    #and shows appropriate sprite
    def draw(self,win):
        if self.left and not susej.got:
            win.blit(walkLeft, (self.x,self.y))
        elif self.right and not susej.got:
            win.blit(walkRight, (self.x,self.y))
        elif self.left and susej.got:
            win.blit(walkLeftSusej, (self.x,self.y))
        elif self.right and susej.got:
            win.blit(walkRightSusej, (self.x,self.y))

class npc(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25
        self.dead = False
        self.interaction = 0

    def draw(self,win):
        if act1.scene3 and not self.dead:
            win.blit(donkeyKong, (self.x,self.y))

    def drawShopMan(self,win):
        if act2.scene1 and rat.x + rat.width <= 810:
            win.blit(pygame.transform.flip(deadGuy, True, False), (self.x,self.y))
        elif act2.scene1 and rat.x + rat.width >= 811:
            win.blit(deadGuy, (self.x, self.y))

    def drawPuckMan(self,win):
        if act2.scene2 and self.interaction == 0:
            win.blit(pac, (self.x, self.y))
        if act2.scene2 and self.interaction == 1:
            win.blit(pacUp, (self.x, self.y))

    def drawObama(self,win):
        if act2.scene1:
            win.blit(obamapng, (self.x,self.y))

class item(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.got = False

    #detects if player has malcolm and
    #decides which sprite to display
    def draw(self,win):
        if not self.got and act1.scene2 and not dk.dead and not coconutGun.got:
            win.blit(malc, (self.x,self.y))
        elif self.got:
            win.blit(malcinv, (52,23))
        if not self.got and dk.dead and act1.scene3:
            win.blit(malc, (1245, 510))

    def drawGun(self,win):
        if self.got:
            win.blit(coconutguninv, (self.x,self.y))

    def drawWinrar(self,win):
        if self.got:
            win.blit(winrarinv, (196, 15))
        if not self.got and act2.scene1:
            win.blit(winrar, (self.x,self.y))

    def drawSzip(self,win):
        if self.got:
            win.blit(zip7inv, (196,20))
        if not self.got and act2.scene1:
            win.blit(zip7, (self.x,self.y))

    def drawSusej(self,win):
        if not self.got and act2.scene3:
            win.blit(swag, (self.x,self.y))

    def drawDollar(self,win):
        if not self.got and act2.scene3:
            win.blit(dollarimg, (self.x,self.y))
    def drawLice(self,win):
        if act2.scene3:
            win.blit(liceimg, (self.x,self.y))


class projectile(object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 25 * facing

    def draw(self,win):
        win.blit(coconutimg, (self.x,self.y))

class selector(object):
    def __init__(self):
        self.no = False
        self.yes = False
        self.left = False
        self.mid = False
        self.right = False

    def draw (self,win):
        if self.yes:
            win.blit(selector1yes, (0,0))
        elif self.no:
            win.blit(selector1no, (0,0))

    def drawSelec2(self,win):
        if self.left:
            win.blit(selector1L, (0,0))
        if self.mid:
            win.blit(selector1M, (0,0))
        if self.right:
            win.blit(selector1R, (0,0))

class acts(object):
    def __init__(self):
        self.scene1 = False
        self.scene2 = False
        self.scene3 = False
        self.scene4 = False
        self.scene5 = False

#draws the stuff
def drawStuff():
    win.blit(bg, (0,0))
    if not mainMenu and bg != credit:
        drawCurrency(win, "  : " + str(lice), 44, 1430, 82)
        drawCurrency(win, "    : $" + str(balance), 44, 1430, 20)
    shopMan.drawShopMan(win)
    obama.drawObama(win)
    susej.drawSusej(win)
    giveLice.drawLice(win)
    rat.draw(win)
    winRar.drawWinrar(win)
    szip.drawSzip(win)
    dk.draw(win)
    dollar.drawDollar(win)
    pacman.drawPuckMan(win)
    for coconut in coconuts:
        coconut.draw(win)
    coconutGun.drawGun(win)
    dkselector.draw(win)
    susejSelector.drawSelec2(win)
    malcolm.draw(win)
    pygame.display.update()

#main
pygame.mixer.music.play(10)

rat = player(1200, 760, 333,168)
dollar = item(1163,536,135,111)
giveLice = item(1377,568,79,69)
malcolm = item(228,500, 137, 213)
coconutGun = item(40, 13, 65, 65)
jesus = npc(0, 0, 0, 0)
shopMan = npc(458,175,235,232)
obama = npc(863,166,146,227)
dk = npc(-1000,-1000,436,435)
winRar = item(445,356,111,110)
szip = item(856,369,100,57)
coconut = projectile(0, 0, 0)
pacman = npc(-222,470,223,334)
susej = item(896,510,158,160)
act1 = acts()
act2 = acts()
dkselector = selector()
susejSelector = selector()
coconuts = []
while running:

    clock.tick(30)

    #closes game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for coconut in coconuts:
        if coconut.x < screenWidth and coconut.x > 0:
            coconut.x += coconut.vel
        else:
            coconuts.pop(coconuts.index(coconut))

    #controls
    if not freezeTime:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x] and coconutGun.got:
            if rat.left:
                facing = -1
            else:
                facing = 1
            if len(coconuts) < 5:
                coconuts.append(projectile(round(rat.x + rat.width //2), round(rat.y + rat.height//2), facing))
        if keys[pygame.K_r] and mainMenu:
            bg = bg1
            mainMenu = False
            act1.scene1 = True
            intro = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(hyrule)
        if keys[pygame.K_c] and mainMenu:
            bg = credit
        if keys[pygame.K_LEFT] and not mainMenu:
            rat.x -= rat.vel
            rat.left = True
            rat.right = False
        if keys[pygame.K_RIGHT] and not mainMenu:
            rat.x += rat.vel
            rat.right = True
            rat.left = False
        if not(rat.ratJump):
            if keys[pygame.K_SPACE]:
                rat.ratJump = True
        else:
            if rat.jumpCount >= -10:
                neg = 1
                if rat.jumpCount < 0:
                    neg = -1
                rat.y -= (rat.jumpCount ** 2) /2 * neg
                rat.jumpCount -= 1
            else:
                rat.ratJump = False
                rat.jumpCount = 10

    #Controls for the selection screen in act1.scene3
    if freezeTime and dkselector.no or dkselector.yes and act1.scene3:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dkselector.yes = True
            dkselector.no = False
        if keys[pygame.K_DOWN]:
            dkselector.no = True
            dkselector.yes = False
        if dkselector.yes and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.Sound.stop(matt3)
            pygame.mixer.Sound.play(matt4)
            dkselector.yes = False
            coconutGun.got = True
            malcolm.got = False
            freezeTime = False

    #pacman shenans
    if freezeTime and act2.scene3:
        keys = pygame.key.get_pressed()
        if jesus.interaction == 1:
            susejSelector.right = True
        if keys[pygame.K_LEFT] and susejSelector.mid and not susej.got:
            jesus.interaction += 1
            susejSelector.left = True
            susejSelector.mid = False
            susejSelector.right = False
        if keys[pygame.K_RIGHT] and susejSelector.left and not dollar.got:
            jesus.interaction += 1
            susejSelector.left = False
            susejSelector.mid = True
            susejSelector.right = False
        if keys[pygame.K_RIGHT] and susejSelector.left and dollar.got:
            jesus.interaction += 1
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = True
        if keys[pygame.K_RIGHT] and susejSelector.mid:
            jesus.interaction += 1
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = True
        if keys[pygame.K_LEFT] and susejSelector.right and not dollar.got:
            jesus.interaction += 1
            susejSelector.left = False
            susejSelector.mid = True
            susejSelector.right = False
        if keys[pygame.K_LEFT] and susejSelector.right and dollar.got:
            jesus.interaction += 1
            susejSelector.left = True
            susejSelector.mid = False
            susejSelector.right = False
        if keys[pygame.K_LEFT] and susejSelector.right and susej.got:
            jesus.interaction += 1
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = True
        if susejSelector.left and lice >= 20 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            susej.got = True
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = False
            freezeTime = False
            rat.x = 200
            lice -= 20
            jesus.interaction = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = False
            freezeTime = False
            rat.x = 200
            jesus.interaction = 1
        if susejSelector.mid and lice >= 2 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dollar.got = True
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = False
            freezeTime = False
            rat.x = 200
            lice -= 2
            balance += 1000
            jesus.interaction = 1
        if susejSelector.right and lice >= 10 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            lice -= 10
            susejSelector.left = False
            susejSelector.mid = False
            susejSelector.right = False
            jesus.interaction = 1


    #plays logans lines at beginning of game
    if intro:
        pygame.mixer.Sound.play(log1)
        intro = False

   #detects if rat gets malcolm after killing dk
    if dk.dead and act1.scene3 and rat.x + rat.width >= 1245 and rat.y >= 510 and not malcolm.got:
        malcolm.got = True
        pygame.mixer.Sound.play(goodjob)
        coconutGun.x = 117
        coconutGun.y = 36

    #beginning of act2
    #act2.scene1
    if rat.x + rat.width >= screenWidth and act1.scene3 and dk.dead and malcolm.got:
        bg = bg4
        lice += 1
        rat.x = 20
        pygame.mixer.Sound.stop(dkrap)
        pygame.mixer.Sound.play(hyrule)
        shopMan.interaction += 1
        act2.scene1 = True
        act1.scene3 = False
        if shopMan.interaction == 1:
            pygame.mixer.Sound.play(saviomiggyi)
        elif balance == 0 and shopMan.interaction > 1:
            pygame.mixer.Sound.play(nomoney)
        elif 0 < balance < 9999999999999:
            pygame.mixer.Sound.play(hasmoney)

#Maybe just make this into a selector to reduce headache
#Ask savio and miggy to record new selector lines
######
    if 900 <= rat.x <= 1000 and rat.y <= 750 and balance >= 1000 and act2.scene1 and not szip.got and not winRar.got:
        szip.got = True
        pygame.mixer.Sound.play(moneymiggy)
        pygame.mixer.Sound.stop(hasmoney)

    if winRar.x <= rat.x <= winRar.x - winRar.width and rat. y <= 800 and balance == 1000 and act2.scene1 and not winRar.got and not szip.got:
        winRar.got = True
        pygame.mixer.Sound.play(moneysavio)
        pygame.mixer.Sound.stop(hasmoney)
#######

    if rat.x <= 0 and act2.scene1:
        bg = bg3
        lice += 1
        pygame.mixer.Sound.stop(hyrule)
        pygame.mixer.Sound.play(dkrap)
        rat.x = 1200
        act2.scene1 = False
        act1.scene3 = True

    #act2.scene2
    if act2.scene2 and pacman.interaction == 0 and rat.x == 300:
        while pacman.x < 1600:
            freezeTime = True
            pacman.x += pacman.vel
            drawStuff()
            if pacman.x >= 1600:
                rat.x == 301
                freezeTime = False
        pacman.interaction = 1
    if act2.scene2 and pacman.interaction == 1 and rat.x == 700:
        pacman.x = 500
        pacman.y = 900
        while pacman.y > -342:
            freezeTime = True
            pacman.y -= pacman.vel
            drawStuff()
            if pacman.y <= -342:
                rat.x = 701
                freezeTime = False
        pacman.interaction = 2

    if rat.x + rat.width >= screenWidth and act2.scene1:
        bg = bg5
        lice += 1
        rat.x = 20
        pygame.mixer.Sound.stop(nomoney)
        pygame.mixer.Sound.stop(hasmoney)
        pygame.mixer.Sound.stop(saviomiggyi)
        act2.scene1 = False
        act2.scene2 = True
    if rat.x <= 0 and act2.scene2:
        bg = bg4
        lice += 1
        rat.x = 1200
        shopMan.interaction += 1
        if balance == 0 and shopMan.interaction > 1:
            pygame.mixer.Sound.play(nomoney)
        elif 0 < balance < 99999999999999999999999:
            pygame.mixer.Sound.play(hasmoney)
        act2.scene2 = False
        act2.scene1 = True

    #changes to act2.scene3
    if rat.x + rat.width >= screenWidth and act2.scene2:
        if jesus.interaction == 0:
            pygame.mixer.Sound.play(jesus1)
            jesus.interaction = 1
        pygame.mixer.Sound.stop(hyrule)
        pygame.mixer.Sound.play(mexico)
        bg = bg6
        lice += 1
        rat.x = 20
        act2.scene2 = False
        act2.scene3 = True
    if rat.x >= 500 and act2.scene3:
        freezeTime = True
    if rat.x <= 0 and act2.scene3:
        pygame.mixer.Sound.stop(mexico)
        pygame.mixer.Sound.play(hyrule)
        pygame.mixer.Sound.stop(jesus1)
        bg = bg5
        lice +=1
        rat.x = 1200
        act2.scene3 = False
        act2.scene2 = True


    #changes to act1.scene3
    if rat.x + rat.width >= 900 and act1.scene3 and not malcolm.got and not coconutGun.got:
        rat.x = 533
        pygame.mixer.Sound.stop(matt1)
        pygame.mixer.Sound.play(matt2)
        while dk.y >= 100:
            dk.y -= dk.vel
            drawStuff()
        freezeTime = True
        if dk.y <= 99:
            bg = credit
            rat.y = -1000
            dk.x = -1000

    if coconutGun.got and act1.scene3 and dk.x + dk.width > coconut.x >= dk.x and coconut.y <= dk.y + dk.height:
        dk.dead = True
        pygame.mixer.Sound.play(matt5)
        pygame.mixer.Sound.stop(matt4)

    if rat.x + rat.width >= 900 and act1.scene3 and malcolm.got and not dk.dead:
        rat.x = 533
        pygame.mixer.Sound.stop(matt1)
        pygame.mixer.Sound.play(matt3)
        freezeTime = True
        dkselector.no = True

    #still act1.scene3 garbage
    if rat.x + rat.width >= 1600 and act1.scene1 and not malcolm.got:
        bg = bg3
        lice += 1
        pygame.mixer.Sound.stop(log1)
        pygame.mixer.Sound.stop(hyrule)
        pygame.mixer.Sound.play(dkrap)
        pygame.mixer.Sound.play(matt1)
        if dk.dead:
            pygame.mixer.Sound.stop(matt1)
        rat.x = 20
        dk.x = 1115
        dk.y = 348
        act1.scene1 = False
        act1.scene3 = True

    elif rat.x + rat.width >= 1600 and act1.scene1 and malcolm.got:
        bg = bg3
        lice += 1
        pygame.mixer.Sound.stop(hyrule)
        pygame.mixer.Sound.play(dkrap)
        rat.x = 20
        dk.x = 1115
        dk.y = 348
        act1.scene1 = False
        act1.scene3 = True
    if rat.x <= 0 and act1.scene3:
        bg = bg1
        lice += 1
        pygame.mixer.Sound.stop(dkrap)
        pygame.mixer.Sound.stop(matt1)
        pygame.mixer.Sound.play(hyrule)
        rat.x = 1200
        act1.scene3 = False
        act1.scene1 = True

    #act1.scene2
    #detects if the player collides with malcolm
    if rat.x <= malcolm.x + malcolm.width and rat.y <= malcolm.y + malcolm.height \
     and act1.scene2 and not malcolm.got and not dk.dead:
        malcolm.got = True
        pygame.mixer.Sound.play(goodjob)

    #change act1.scene 1 to 2 and checks if the player has malcolm
    if rat.x <= 0 and not malcolm.got and act1.scene1:
        bg = bg2
        lice += 1
        rat.x = 1200
        pygame.mixer.Sound.stop(log1)
        pygame.mixer.Sound.play(iceman1)
        act1.scene2 = True
        act1.scene1 = False
    elif rat.x <= 0 and malcolm.got and act1.scene1:
        bg = bg2
        lice += 1
        rat.x = 1200
        act1.scene2 = True
        act1.scene1 = False

    #Checks if the player has malcolm before returning to bg1
    if rat.x >= 1300 and act1.scene2:
        bg = bg1
        lice += 1
        rat.x = 20
        act1.scene1 = True
        act1.scene2 = False

    drawStuff()

pygame.quit()
