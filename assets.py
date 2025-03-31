import pygame, random
from pygame.locals import *
from pygame.draw import *

print('Loading...')
#window renderer setup
pygame.init()
window = pygame.display.set_mode((320, 240), pygame.SCALED | pygame.RESIZABLE, vsync=1)
clock = pygame.time.Clock()
icon = pygame.image.load('icon.png')
windowSplashes = ["The Movie: The Musical: The Game",
                  "Rated ARRRR By the Bureau of Gaming Pirates LTD",
                  "Matthew Grout is a Butt Head Edition",
                  "Better Than Fortnite",
                  "Matthew Grout is a Sigma Male Edition",
                  "Created By the Official Mr. Daniels Hate Club",
                  "More Than One Line of Code!"]
windowString = "Mazegame"
if random.randint(1,3) > 1:
    windowString += ": "
    windowString += random.choice(windowSplashes)
pygame.display.set_caption(windowString)
pygame.display.set_icon(icon)

#bg and font
backgroundColor = (255, 0, 255)
font1 = pygame.font.Font('assets/ui/font.otf', 20)

#player sprites
guyS1 = pygame.image.load('assets/guy/guyS1.png').convert_alpha()
guyS2 = pygame.image.load('assets/guy/guyS2.png').convert_alpha()
guyS3 = pygame.image.load('assets/guy/guyS3.png').convert_alpha()
guyW1 = pygame.image.load('assets/guy/guyW1.png').convert_alpha()
guyW2 = pygame.image.load('assets/guy/guyW2.png').convert_alpha()
guyW3 = pygame.image.load('assets/guy/guyW3.png').convert_alpha()
guyN1 = pygame.image.load('assets/guy/guyN1.png').convert_alpha()
guyN2 = pygame.image.load('assets/guy/guyN2.png').convert_alpha()
guyN3 = pygame.image.load('assets/guy/guyN3.png').convert_alpha()
guyE1 = pygame.image.load('assets/guy/guyE1.png').convert_alpha()
guyE2 = pygame.image.load('assets/guy/guyE2.png').convert_alpha()
guyE3 = pygame.image.load('assets/guy/guyE3.png').convert_alpha()

guyRect = guyS1.get_rect()
guyRect.center = (160, 120)

playerSpriteList = [[guyN1, guyE1, guyS1, guyW1],
                    [guyN2, guyE2, guyS2, guyW2],
                    [guyN3, guyE3, guyS3, guyW3]]

#tiles
floor1 = pygame.image.load('assets/tiles/floor1.png').convert_alpha()
wallFront1 = pygame.image.load('assets/tiles/wall front.png').convert_alpha()
wallFront2 = pygame.image.load('assets/tiles/wallfront2.png').convert_alpha()
wallFront3 = pygame.image.load('assets/tiles/wallfront3.png').convert_alpha()
wallTop1 = pygame.image.load('assets/tiles/wall top.png').convert_alpha()
wallTop2 = pygame.image.load('assets/tiles/wall top bottom left corner.png').convert_alpha()
wallTop3 = pygame.image.load('assets/tiles/walltop3.png').convert_alpha()
wallTop4 = pygame.image.load('assets/tiles/walltop4.png').convert_alpha()
wallTop5 = pygame.image.load('assets/tiles/walltop5.png').convert_alpha()
wallTop6 = pygame.image.load('assets/tiles/walltop6.png').convert_alpha()
wallTop7 = pygame.image.load('assets/tiles/walltop7.png').convert_alpha()
wallTop8 = pygame.image.load('assets/tiles/walltop8.png').convert_alpha()
wallTop9 = pygame.image.load('assets/tiles/wall top t south.png').convert_alpha()
wallTop10 = pygame.image.load('assets/tiles/wall top t west.png').convert_alpha()
wallTop11 = pygame.image.load('assets/tiles/wall top t north.png').convert_alpha()
wallTop12 = pygame.image.load('assets/tiles/wall top t east.png').convert_alpha()
wallFront4 = pygame.image.load('assets/tiles/wall front t south.png').convert_alpha()
wallFront5 = pygame.image.load('assets/tiles/wall front sign.png').convert_alpha()
wallFront6 = pygame.image.load('assets/tiles/wall front shop bar.png').convert_alpha()
floor2 = pygame.image.load('assets/tiles/floor shop bar.png').convert_alpha()
wallTop13 = pygame.image.load('assets/tiles/wall top shop bar.png').convert_alpha()
wallFront7 = pygame.image.load('assets/tiles/wall front left of gate.png').convert_alpha()
wallFront8 = pygame.image.load('assets/tiles/wall front right of gate.png').convert_alpha()
wallTop14 = pygame.image.load('assets/tiles/wall top left of gate.png').convert_alpha()
wallTop15 = pygame.image.load('assets/tiles/wall top right of gate.png').convert_alpha()

tileList = [floor1, wallFront1, wallTop1, wallTop2, wallTop3, wallFront2,
            wallFront3, wallTop4, wallTop5, wallTop6, wallTop7, wallTop8,
            wallTop9, wallTop10, wallTop12, wallTop11, wallFront4, wallFront5,
            wallFront6, floor2, wallTop13, wallFront7, wallFront8, wallTop14,
            wallTop15]

#ui
statBars = pygame.image.load('assets/ui/healthstamina.png').convert_alpha()
dialogueBox = pygame.image.load('assets/ui/dialogueBox.png').convert_alpha()
signPortrait = pygame.image.load('assets/ui/signPortrait.png').convert_alpha()

#directions
north = 0
east = 1
south = 2
west = 3

#objects
keySprite = pygame.image.load('assets/objects/key.png').convert_alpha()
lockedGateTop = pygame.image.load('assets/tiles/gate top.png').convert_alpha()
lockedGateBottom = pygame.image.load('assets/tiles/gate bottom.png').convert_alpha()

#object values
keyObj = 0
closedGateBottomObj = 1
closedGateTopObj = 2
openGateBottomObj = 3
openGateTopObj = 4

#misc gameplay vars
running = True
playerX = 8
playerY = -8
checkedTileX = 0
checkedTileY = 0
oldX = 0
oldY = 0
playerDirection = south
playerWalkFrame = 0
playerWalkSpeed = 1
playerSpeedMultiplier = 1
playerSprintMultiplier = 1
playerStamina = 20
playerHealth = 20
heldKeys = 0
checking = False
interacting = False
reading = False
talking = False
walking = False
fpsShown = False
print()
print('DONE!!!')