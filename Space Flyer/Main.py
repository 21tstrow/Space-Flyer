##Space Flyer
##Imports
import pygame, pathlib, platform, math, random
#import Planet.py
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

def image(arg):
    return pygame.image.load(findImage(arg))

##Classes
class sprite():
    def __init__(self, image, size, location):
        self.image = image
        self.size = size
        self.x, self.y = location
        self.w, self.h = size
        self.location = location
        self.xywh = (self.x, self.y, self.w, self.h)

    def addX(self, amount):
        self.x += amount
        self.location = (self.x, self.y)
        self.xywh = (self.x, self.y, self.w, self.h)

    def addY(self, amount):
        self.y += amount
        self.location = (self.x, self.y)
        self.xywh = (self.x, self.y, self.w, self.h)

    def displaySprite(self):
        screen.blit(self.image, self.location)

class ship(sprite):
    def __init__(self, image, size, location, speed, fuelEcon, attackDam, crewCap, maxHp):
        super().__init__(image, size, location)
        self.speed = speed
        self.fuelEcon = fuelEcon
        self.attackDam = attackDam
        self.crewCap = crewCap
        self.maxHp = maxHp
        self.currentHp = maxHp

    def displayShip(self):
        super().displaySprite()

class namedSprite(sprite):
    def __init__(self, image, size, location,name):
        super().__init__(image, size, location)
        self.name = name

class planet():
    def __init__(self, alienSprite, postLandScene, portType, minigame):
        self.alien = alienSprite
        self.postLandScene = postLandScene
        self.portType = portType
        self.minigame = minigame
        self.colorScheme = self.generateRandomColorScheme()
        self.relations = 0
        self.inventory = self.generateInventory()

    def generateRandomColorScheme(self):
        return ((random.randint(50,205),random.randint(50,205),random.randint(50,205)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    def getColors(self):
        return self.colorScheme

    def changeRelations(val):
        self.relations += val

    def generateInventory(self):#!
        return ['Shotgun', 'Cereal Bar', 'Star Lazer']

class econPlanet():
    def __init__(self):
        ''
##File Management
def mainpath():
    if platform.system() == "Windows":
        f = "C:\\Users"
    elif platform.system() == "Darwin":
        f = "/Users"
    elif platform.system() == "Linux":
        f = None
    else:
        print("System not found!")
    return pathlib.Path(f).glob('**/*') 


def search(path, file):
    for x in path:
        if (x.name == file):
            return x

def findImage(file):
    m = mainpath()
    fname = search(m, file)
    print(fname)
    print("Done")
    return str(fname)

##Static Variables
shipSize = (70,110)
diaFont = pygame.font.SysFont("timesnewroman", 14)
shotImg = image("SpaceFlyerShot.png")
valueChart = {
    'Star Lazer' : 300,
    'Shotgun' : 50,
    'Cereal Bar' : 10,
}

##Ships
redSquare = image("meteor.jpg")
spaceShipBasic = image("spaceShipBasic.jpg")
starterShip = {
    'image': spaceShipBasic,#!
    'size': shipSize,
    'speed': 10,#!
    'fuel economy': 10,#!
    'attack damage': 10,#!
    'crew capacity': 10,#!
    'hp': 10,
    }

ships = [starterShip]
##Dynamic Variables
currentScene = 'planet'
activeObjects = []
currentPlanet = planet('n','n','n','n')
inventory = ['Star Lazer', 'Shotgun', 'Cereal Bar']
##Class Variables        
playerShip = ship(starterShip['image'], starterShip['size'], (0,0), starterShip['speed'],starterShip['fuel economy'], starterShip['attack damage'], starterShip['crew capacity'], starterShip['hp'])

##Functioning Funcitons



def loadObjects():#!
    ''

def runDeath():
    print('dead')
    '''
    global activeObjects
    for i in activeObjects:
        print(i.location)
        print(i.xywh)
    print('\n\n' + str(playerShip.location)
    pygame.quit()
    '''

def landingScene():#!
    ''

def rectangle(rectColor, lineColor, cords):
    global screen
    x,y,w,h = cords
    pygame.draw.rect(screen, lineColor, (x,y,w,h))
    pygame.draw.rect(screen, rectColor, (x + 3,y + 3,w-6,h-6))
    

#Dialouge and Communication
'''
Options: Shop, Diplomacy, Cancel

Shop
    buy
        wares and prices
    sell
        inventory and offers
    back

Diplomacy
    compliment
        response
        <LOOP>
    threat
        responce
        action
        <LOOP>
'''
    #Dialouge related variables
currentDialouge = 'start'


#waresPrices(), inventoryOffers(), getRandomCompliment(), getRandomThreat(), compliment(), threat(), leave()


def processDia():
    global currentPlanet
    mainColor, accentColor = currentPlanet.getColors()
    for i in range(3):
        rectangle((0,0,0), accentColor, (50, 385 + 110 * i, 540, 90))
    rectangle((0,0,0), accentColor, (690, 385, 540, 310))
    try:
        dialouges[currentDialouge][0]
    except:
        functionDialouge(dialouges[currentDialouge])
        return
    count = 0
    for dia in dialouges[currentDialouge]:
        text = diaFont.render(dia, True, (255,255,255))
        screen.blit(text, (55, 390 + 110 * count))
        count += 1
    print('HRM')
    pygame.display.update()
    pygame.time.wait(250)



def diaOne():
    global currentDialouge
    if currentDialouge == 'start':
        currentDialouge = 'shop'
    elif currentDialouge == 'shop':
        currentDialouge = 'buy'
    if currentDialouge == 'diplomacy':
        currentDialouge = 'compliment'
    processDia()

def diaTwo():
    global currentDialouge
    if currentDialouge == 'start':
        currentDialouge = 'diplomacy'
    elif currentDialouge == 'diplomacy':
        currentDialouge = 'threat'
    elif currentDialouge == 'shop':
        currentDialouge =  'sell'
    processDia()

def diaThree():
    global currentDialouge
    if currentDialouge == 'start':
        leave()
    elif currentDialouge == 'shop':
        currentDialouge = 'start'
    elif currentDialouge == 'diplomacy':
        currentDialouge = 'start'
    processDia()

def waresPrices():
    global currentPlanet, screen
    mainColor, accentColor = currentPlanet.getColors()
    rectangle((0,0,0), accentColor, (690, 385, 540, 310))
    offers = []
    inventory = currentPlanet.inventory
    for i in inventory:
        offers.append([i,valueChart[i] - ((currentPlanet.relations/500 - .5) * valueChart[i])])
    count = 0
    for i in offers:
        text = diaFont.render(i[0] + ": " + str(i[1]), True, (255,255,255))
        screen.blit(text, (695, 390 + 20 * count))
        count += 1
    print('Skeet')
    pygame.display.update()
    pygame.time.wait(250)

def inventoryOffers():
    global inventory, currentPlanet, screen
    mainColor, accentColor = currentPlanet.getColors()
    rectangle((0,0,0), accentColor, (690, 385, 540, 310))
    offers = []
    for i in inventory:
        offers.append([i,valueChart[i] + ((currentPlanet.relations/500 - .5) * valueChart[i])])
    count = 0
    for i in offers:
        text = diaFont.render(i[0] + ": " + str(i[1]), True, (255,255,255))
        screen.blit(text, (695, 390 + 20 * count))
        count += 1
    print('Skeet')
    pygame.display.update()
    pygame.time.wait(250)

def getRandomCompliment():
    return "Damn Daniel"

def getRandomThreat():
    return "Fuck Daniel"

def compliment():
    ''

def threat():
    ''

def leave():
    global currentScene
    done = False
    rectangle((0,0,0),(255,255,255),(0,0,1280,720))
    currentScene = 'outer space'

dialouges = {
    'start' : ["I\'ve come to bargain.", "Let\'s talk diplomacy", "[LEAVE]"],
    'shop' : ["Show me your wares.", "I have some items I\'d like to sell", "[BACK]"],
    'buy' : 0,
    'sell' : 1,
    'diplomacy' : ['Compliment','Threat',"[BACK]"],
    'compliment' : 2,
    'threat' : 3,
    }

def functionDialouge(n):
    if n == 0:
        waresPrices()
    elif n == 1:
        inventoryOffers()
    elif n == 2:
        compliment()
    elif n == 3:
        threat()

##Game running Functions
def runScene(currentScene):
    if currentScene == 'outer space':
        outerSpace()
    if currentScene == 'planet':
        landingScene()
        planetScene()

def outerSpace():
    global activeObjects
    shots = []
    count = 0
    done = False
    while not done:
        loadObjects
        while len(activeObjects) < 10:
            activeObjects.append(namedSprite(redSquare, (50,50), (random.randint(0, 1280), 0), 'meteor'))#!
        for event in pygame.event.get():
            ''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            playerShip.addY(-playerShip.speed)
        if pressed[pygame.K_s]:
            playerShip.addY(playerShip.speed)
        if pressed[pygame.K_a]:
            playerShip.addX(-playerShip.speed)
        if pressed[pygame.K_d]:
            playerShip.addX(playerShip.speed)
        if pygame.mouse.get_pressed() == (1,0,0) and count >= 15:
            count = 0
            mouseLocation = pygame.mouse.get_pos()
            mX,mY = mouseLocation
            shots.append([namedSprite(shotImg, (5,5), ((playerShip.x + 33, playerShip.y)), 'shot'), (mX - playerShip.x, mY - playerShip.y)])
        count += 1
        pygame.draw.rect(screen,(0,0,0),(0,0,1280,720))
        playerShip.displayShip()
        sX, sY, sW, sH = playerShip.xywh
        for obj in activeObjects:
            screen.blit(obj.image, obj.location)
            oX, oY, oW, oH = obj.xywh
            sX, sY, sW, sH = playerShip.xywh
            if sX + sW >= oX and sX <= oX + oW and sY + sH >= oY and sY <= oY + oH:
                try:
                    if obj.name == 'meteor':
                        runDeath()#!
                        done = True
                        break
                except:
                    loadObject(obj.name)#!
                    done = True
                    break
            else:
                try:
                    if obj.name == 'meteor':
                        obj.addY(playerShip.speed /2)
                except:
                    continue
                if obj.y > 720:
                        activeObjects.remove(obj)
            for shot in shots:
                shX, shY, shW, shH = shot[0].xywh
                slopeX, slopeY = shot[1]
                if oX + oW >= shX and oX <= shX + shW and oY + oH >= shY and oY <= shY + shH:
                    try:
                        activeObjects.remove(obj)
                    except:
                        ''
                    shots.remove(shot)
                else:
                    shot[0].addX(.01 * slopeX)
                    shot[0].addY(.01 * slopeY)
                screen.blit(shot[0].image, shot[0].location)
        pygame.display.update()
        pygame.time.wait(10)
        
                
def planetScene():
    global currentPlanet
    mainColor, accentColor = currentPlanet.getColors()
    print(currentPlanet.getColors())
    m1,m2,m3 = mainColor
    pygame.draw.rect(screen,(m1-50,m2-50,m3-50),(0,0,1280,720))
    rectangle(mainColor, accentColor,(0,335,1280,360))
    for i in range(4):
        rectangle(mainColor, accentColor,((100* i + 10),0,50,338))
        rectangle(mainColor, mainColor,((100* i + 13),0,44,338))
        rectangle(mainColor, accentColor,((100* i),0,50,363))
        rectangle(mainColor, mainColor,((100* i + 3),0,44,363))
        pygame.draw.line(screen, accentColor, [100*i + 49, 363], [100*i + 57, 338], 3)
    for i in range(4):
        rectangle(mainColor, accentColor,((1230 -  100* i - 10),0,50,338))
        rectangle(mainColor, mainColor,((1230 -  100* i - 7),0,44,338))
        rectangle(mainColor, accentColor,((1230 -  100* i),0,50,363))
        rectangle(mainColor, mainColor,((1230 -  (100* i - 3)),0,44,363))
        pygame.draw.line(screen, accentColor, [1230 - (100*i), 363], [1230 - (100*i + 8), 338], 3)
    rectangle(mainColor, accentColor,(0,360,1280,360))
    for i in range(3):
        rectangle((0,0,0), accentColor, (50, 385 + 110 * i, 540, 90))
    rectangle((0,0,0), accentColor, (690, 385, 540, 310))
    pygame.display.update()
    processDia()
    done = False
    while not done:
        for event in pygame.event.get():
            ''
        if pygame.mouse.get_pressed() == (1,0,0):
            mouseLocation = pygame.mouse.get_pos()
            mX,mY = mouseLocation
            if mX > 50 and mX < 590:
                if mY > 385 and mY < 475:
                    diaOne()
                if mY > 495 and mY < 585:
                    diaTwo()
                if mY > 605 and mY < 695:
                    diaThree()
        if currentScene != 'planet':
            done = True

    
##Game loop
pygame.display.set_caption('Space Flyer')
while True:
    runScene(currentScene)

