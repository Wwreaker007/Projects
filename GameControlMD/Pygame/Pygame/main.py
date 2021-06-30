import pygame, time,datetime
import random,math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Corona Game")

running = True

mixer.music.load('music.mp3')
mixer.music.play(-1)

windowImg = pygame.image.load('skyScreen.jpg')
groundImg = pygame.image.load('Ground.png')
characterImg = pygame.image.load('runC.png')
jumpImg = pygame.image.load('jumpC.png')
crouchImg = pygame.image.load('bendC.png')
ExitImg = pygame.image.load('FinalScreen.png')
nof_clouds =3
cloudImg = []
cloudX = []
cloudY = []

initialCloudX=100
initialCloudY=0

x = 100
y = 0
for i in range (nof_clouds):
    cloudImg.append(pygame.image.load('cloud1.png'))
    cloudX.append(x)
    cloudY.append(y)
    x+= 300

cloudImg[1] = pygame.image.load('cloud2.png')
cloudY[1] = 10
cloudImg[2] = pygame.image.load('cloud3.png')

viruses = []
upviruses = []

viruses.append(pygame.image.load('cv1.png'))
viruses.append(pygame.image.load('cv2.png'))
viruses.append(pygame.image.load('cv3.png'))
viruses.append(pygame.image.load('cv4.png'))
viruses.append(pygame.image.load('cv5.png'))
viruses.append(pygame.image.load('cv6.png'))
viruses.append(pygame.image.load('cv7.png'))
viruses.append(pygame.image.load('cv8.png'))
viruses.append(pygame.image.load('cv9.png'))

upviruses.append(pygame.image.load('cv1.png'))
upviruses.append(pygame.image.load('cv2.png'))
upviruses.append(pygame.image.load('cv3.png'))
upviruses.append(pygame.image.load('cv4.png'))
upviruses.append(pygame.image.load('cv5.png'))
upviruses.append(pygame.image.load('cv6.png'))
upviruses.append(pygame.image.load('cv7.png'))
upviruses.append(pygame.image.load('cv8.png'))
upviruses.append(pygame.image.load('cv9.png'))

virusX = []
virusY = []

upvirusX = []
upvirusY = []

nof_viruses = 9

VirusType = ["up","down","sanitizer"]

BType = []
BType =["chineseBats"]

for i in range (nof_viruses):
    x = 710
    virusX.append(x)
    virusY.append(387)

for i in range (nof_viruses):
    x = 720
    upvirusX.append(x)
    upvirusY.append(280)



Birds = []

Birds.append(pygame.image.load('bird1.png'))
Birds.append(pygame.image.load('bird2.png'))
Birds.append(pygame.image.load('bird3.png'))

nof_birds = 3

BirdsX = []
BirdsY = []

for i in range (nof_birds):
    x = random.randint(720,2000)
    y = random.randint(0,100)
    BirdsX.append(x)
    BirdsY.append(y)

sanitizerImg = pygame.image.load('sanitizer.png')
sanitizerX = random.randint(147,710)
sanitizerY = 387

BatsImg = pygame.image.load('fly1.png')
BatsX = random.randint(200,720)
BatsY = 280

BoomImg = pygame.image.load('whitesmoke.png')

home = pygame.image.load('ReachedHome.jpg')
homeX = 0
homeY = 0

characterX = 90
characterY = 300
characterY_change = 300
characterX_change = 0

up = False
crouch = False
right = False
collided = False
sanitized = False

# Creating No of Infections
MaxInfected = 8
font = pygame.font.Font('freesansbold.ttf',32)
#font1 = pygame.font.Font('freesansbold.tff',18)
font_x = 10
font_y = 10

font1_x = 150
font1_y = 100
def show_score(s,x,y):
    MaxInf = font.render("MaxInfection :" + str(MaxInfected),True,(1,234,255))
    Currinf = font.render("CurrInfected : "+ str(s),True,(255,124,196))
    screen.blit(MaxInf,(x+260,y+70))
    screen.blit(Currinf,(x+260,(y+102)))

def background():
    screen.blit(pygame.transform.scale(windowImg, (800, 450)), (0, 0))

def Home():
    screen.blit(pygame.transform.scale(home,(800,600)),(int(homeX),int(homeY)))

def ExitS():
    screen.blit(pygame.transform.scale(ExitImg, (800, 600)), (int(homeX), int(homeY)))


def ground():
    screen.blit(pygame.transform.scale(groundImg, (800, 600)), (0, 450))


def character(x, y):
    screen.blit(pygame.transform.scale(characterImg, (50, 200)), (int(x), int(y)))


def characterJump(x, y):
    screen.blit(pygame.transform.scale(jumpImg, (50, 200)), (int(x), int(y)))


def characterCrouch(x, y):
    screen.blit(pygame.transform.scale(crouchImg, (50, 200)), (int(x), int(y)))

def virusRun():

    for i in range(nof_viruses):
        screen.blit(pygame.transform.scale(viruses[i],(50,80)),(int(virusX[i]),int(virusY[i])))


def virusSelected(vx):
    screen.blit(pygame.transform.scale(viruses[vx],(40,60)),(int(virusX[vx]),int(virusY[vx])))

def upvirusSelected(vx):
    screen.blit(pygame.transform.scale(upviruses[vx],(40,60)),(int(upvirusX[vx]),int(upvirusY[vx])))

def BirdsFly():
    for i in range (nof_birds):
        screen.blit(pygame.transform.scale(Birds[i],(40,40)),(int(BirdsX[i]),int(BirdsY[i])))

def SanitizerDraw(x,y):
    screen.blit(pygame.transform.scale(sanitizerImg, (40, 79)), (int(x), int(y)))

def BatsDraw(x,y):
    screen.blit(pygame.transform.scale(BatsImg,(40,60)),(int(x),int(y)))


def cloudRun():

    for i in range (nof_clouds):
        if i!=0:
            screen.blit(pygame.transform.scale(cloudImg[i], (50, 80)), (int(cloudX[i]), cloudY[i]))
        if i==0:
            screen.blit(pygame.transform.scale(cloudImg[i], (50, 100)), (int(cloudX[i]), cloudY[i]))

def BoomDraw(x,y):
    screen.blit(pygame.transform.scale(BoomImg,(40,300)),(int(x),int(y)))

def showB():
    Msg = font.render(" BeCarefulChineVirus !! :", True, (255, 0, 0))
    screen.blit(Msg,(font1_x+40,font1_y-70))

def showm():
    Msg = font.render(" MaxImmunityReached !! :", True, (255, 1, 86))
    screen.blit(Msg,(font1_x,font1_y+52))


starttime = pygame.time.get_ticks()

virusStilPersists = False
BatStilPersists = False

nof_infectedTimes = 0

flag = False
timer_stop = datetime.datetime.utcnow()+datetime.timedelta(seconds=100)
while running :

    screen.fill((0, 0, 0))

    if nof_infectedTimes > MaxInfected:
        running = False
        ExitS()
        pygame.display.update()
        time.sleep(2)
        continue

    # seconds = (pygame.time.get_ticks()-starttime)/1000
    if (datetime.datetime.utcnow()>timer_stop):
        running = False
        Home()
        pygame.display.update()
        # print(seconds)
        time.sleep(2)
        continue

    # change the x coordinates of the character
    # characterX += 3
    #if characterX >= 750:
       # characterX = 0

    for i in range(nof_clouds):
        cloudX[i]-=0.6
        if cloudX[i] <= 0:
           cloudX[i] = random.randint(10,710)

    if BatStilPersists == False:
        btype = random.randint(0,1)
        BatStilPersists = True

    if virusStilPersists == False :
        type = random.randint(0,1)
        vx = random.randint(0, nof_viruses - 1)
        virusStilPersists = True




    if type>=0 and type <3 and VirusType[type] == "down":
        virusX[vx] -= 2
        if virusX[vx] < 0:
            virusX[vx] = 720
            virusStilPersists = False

        if virusX[vx] == characterX + 30 and characterY_change + 200 > virusY[vx] and virusStilPersists == True:
            nof_infectedTimes += 1
            virusX[vx] = 720
            virusStilPersists = False


    if type>=0 and type <3 and VirusType[type] == "up":
        upvirusX[vx] -= 2
        if upvirusX[vx] < 0:
            upvirusX[vx] = 720
            virusStilPersists = False

        if upvirusX[vx] == characterX + 30 and characterY_change < upvirusY[vx] + 60 and virusStilPersists == True:
            nof_infectedTimes += 1
            upvirusX[vx] = 720
            virusStilPersists = False

    if btype == 0 and BType[btype] == "chineseBats":
        BatsX-=2
        if BatsX < 0:
            BatsX = 720
            BatStilPersists = False
        if BatsX <= characterX + 30 and characterY_change < BatsY+60 and BatStilPersists == True:
            nof_infectedTimes += 1
            BatsX = 710
            BatStilPersists = False



    for i in range(nof_birds):
        BirdsX[i]-=1.2
        if BirdsX[i] <= 0:
           BirdsX[i] = 2000
           BirdsY[i] = random.randint(0,100)

    sanitizerX-=2

    if(sanitizerX==characterX+50 and characterY_change+200>sanitizerY):
        if nof_infectedTimes>0:
           nof_infectedTimes-=1
        if nof_infectedTimes ==0:
            flag = True
        sanitized = True

    if (sanitizerX <= characterX):
        sanitizerX = 2000
        sanitized = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if up key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # running = False
                characterY_change -= 200
                up = True
                crouch = False

            if event.key == pygame.K_DOWN:
                characterY_change+=42
                up = False
                crouch = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                characterY_change = characterY
                crouch = False
                up = False
    background()
    ground()

    if up == True:
        starttime = pygame.time.get_ticks()
        characterJump(characterX, characterY_change)

    if crouch == True:
        characterCrouch(characterX, characterY_change)

    if up == False and crouch == False:
        character(characterX, characterY_change)

    cloudRun()
    BirdsFly()
    # virusRun()

    if type >=0 and type<2 and virusStilPersists == True and VirusType[type]=="down":
       virusSelected(vx)

    if type >=0 and type<2 and virusStilPersists == True and VirusType[type]=="up":
       upvirusSelected(vx)

    if(sanitized == False):
       SanitizerDraw(sanitizerX,sanitizerY)

    if sanitized == True:
        BoomDraw(characterX,characterY_change)

    if btype == 0 and BatStilPersists == True:
        BatsDraw(BatsX,BatsY)
        showB()
    if flag == True:
        # showm()
        # time.sleep(0.7)
        flag = False

    show_score(nof_infectedTimes,font_x, font_y)
    pygame.display.update()