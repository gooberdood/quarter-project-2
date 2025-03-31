import math, sys
from mazes import *



def renderText(what, color, where):
    text = font1.render(what, False, pygame.Color(color))
    window.blit(text, where)



def perFrame():
    global fpsShown, checking, reading, talking, interacting
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_f:
                if fpsShown:
                    fpsShown = False
                else:
                    fpsShown = True
            if event.key == pygame.K_z:
                if checking == False:
                    checking = True
                else:
                    if reading or talking:
                        checking = False
                        reading = False
                        talking = False
            else:
                checking = False
            if event.key == pygame.K_x:
                if interacting == False:
                    interacting = True
            else:
                interacting = False



def getInput():
    global playerX, playerY, walking, playerDirection, playerSprintMultiplier, playerStamina, oldX, oldY, checking, reading, talking
    oldX, oldY = playerX, playerY
    keys = pygame.key.get_pressed()
    
    if not(reading) and not(talking):
        if keys[K_LEFT]:
            playerX -= (playerWalkSpeed * playerSprintMultiplier * playerSpeedMultiplier)
            walking = True
            playerDirection = west
        elif keys[K_RIGHT]:
            playerX += (playerWalkSpeed * playerSprintMultiplier * playerSpeedMultiplier)
            walking = True
            playerDirection = east
        elif keys[K_UP]:
            playerY -= (playerWalkSpeed * playerSprintMultiplier * playerSpeedMultiplier)
            walking = True
            playerDirection = north
        elif keys[K_DOWN]:
            playerY += (playerWalkSpeed * playerSprintMultiplier * playerSpeedMultiplier)
            walking = True
            playerDirection = south
        else:
            walking = False
    else:
        walking = False
        
    if keys[K_LSHIFT]:
        if walking:
            if playerStamina > 0:
                playerSprintMultiplier = 2
                playerStamina -= .1
            else: playerSprintMultiplier = 1
    else:
        if playerStamina < 20:
            if not(walking):
                playerStamina += .1
        if playerStamina > 20:
            playerStamina = 20
        playerSprintMultiplier = 1
        
        
        

def animationTiming():
    global playerWalkFrame
    if walking:
        playerWalkFrame += (playerWalkSpeed * playerSprintMultiplier * playerSpeedMultiplier)/20
    else:
        playerWalkFrame = 0
    if playerWalkFrame >= 3:
        playerWalkFrame = 1
        
        

# Tile 1 template (just for copy n paste lol)
#                if checkedTile == 1:
#                    if ((y*16-36 < playerY < y*16-20) and (x*16-28 < playerX < x*16-4)):
#                        playerX, playerY = oldX, oldY
def collisionDetection():
    global playerX, playerY, oldX, oldY, checking, reading, talking, checkedTileX, checkedTileY, heldKeys, maze1Objects
    for y in range(len(maze1)):
        for x in range(len(maze1[y])):
            checkedTile = maze1[y][x]
            #done so far: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
            if checkedTile != 0:
                if checkedTile == 1 or checkedTile == 16 or checkedTile == 17 or checkedTile == 18 or checkedTile == 21 or checkedTile == 22:
                    if ((y*16-52 < playerY < y*16-35) and (x*16-20 < playerX < x*16+4)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 2 or checkedTile == 12 or checkedTile == 23 or checkedTile == 24:
                    if ((y*16-47 < playerY < y*16-35) and (x*16-20 < playerX < x*16+4)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 3 or checkedTile == 14:
                    if (((y*16-52 < playerY < y*16-35) and (x*16-18 < playerX < x*16+2)) or ((y*16-47 < playerY < y*16-35) and (x*16-18 < playerX < x*16+4))):
                        playerX, playerY = oldX, oldY
                if checkedTile == 4 or checkedTile == 13:
                    if (((y*16-52 < playerY < y*16-35) and (x*16-18 < playerX < x*16+2)) or ((y*16-47 < playerY < y*16-35) and (x*16-20 < playerX < x*16+2))):
                        playerX, playerY = oldX, oldY
                if checkedTile == 5 or checkedTile == 8:
                    if ((y*16-52 < playerY < y*16-35) and (x*16-18 < playerX < x*16+4)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 6 or checkedTile == 10:
                    if ((y*16-52 < playerY < y*16-35) and (x*16-20 < playerX < x*16+2)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 7:
                    if ((y*16-52 < playerY < y*16-35) and (x*16-18 < playerX < x*16+2)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 9:
                    if ((y*16-47 < playerY < y*16-35) and (x*16-18 < playerX < x*16+4)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 11:
                    if ((y*16-47 < playerY < y*16-35) and (x*16-20 < playerX < x*16+2)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 15:
                    if (((y*16-47 < playerY < y*16-35) and (x*16-20 < playerX < x*16+4)) or ((y*16-52 < playerY < y*16-35) and (x*16-18 < playerX < x*16+2))):
                        playerX, playerY = oldX, oldY
                if checkedTile == 19:
                    if ((y*16-52 < playerY < y*16-35) and (x*16-17 < playerX < x*16+1)):
                        playerX, playerY = oldX, oldY
                if checkedTile == 20:
                    if (((y*16-52 < playerY < y*16-35) and (x*16-17 < playerX < x*16+1)) or ((y*16-47 < playerY < y*16-35) and (x*16-20 < playerX < x*16+4))):
                        playerX, playerY = oldX, oldY
    
    for i in range(len(maze1Objects)):
        if (((maze1Objects[i][0]-1)*16-20 < playerX < (maze1Objects[i][0]-1)*16+4) and ((maze1Objects[i][1]-1)*16-52 < playerY < (maze1Objects[i][1]-1)*16-35)):
            if (maze1Objects[i][2] == closedGateTopObj) or (maze1Objects[i][2] == closedGateBottomObj):
                playerX = oldX
                playerY = oldY
    
    if checking:
        for y in range(len(maze1)):
            for x in range(len(maze1[y])):
                checkedTile = maze1[y][x]
                if playerDirection == north:
                    if ((x*16-20 < playerX < x*16+4) and (y*16-52 < playerY-4 < y*16-35)):
                        if checkedTile == 17:
                            reading = True
                            checkedTileX = x+1
                            checkedTileY = y+1
    
    if interacting:
        for i in range(len(maze1Objects)):
            if (((maze1Objects[i][0]-1)*16-20 < playerX < (maze1Objects[i][0]-1)*16+4) and ((maze1Objects[i][1]-1)*16-52 < playerY < (maze1Objects[i][1]-1)*16-35)):
                if maze1Objects[i][2] == keyObj:
                    del maze1Objects[i]
                    heldKeys += 1
                    break



def renderFrame():
    global checkedTileX, checkedTileY
    window.fill(backgroundColor)
    
    playerXOffset = playerX % 16
    playerYOffset = playerY % 16
    for x in range(21):
        for y in range(16):
            window.blit(floor1, ((x * 16 - playerXOffset), (y * 16 - playerYOffset)))
    
    for y in range(len(maze1)):
        for x in range(len(maze1[y])):
            window.blit(tileList[maze1[y][x]], (((x * 16) - playerX)+144, ((y * 16) - playerY)+80))
    
    for i in range(len(maze1Objects)):
        mazeObjectCoords = (((maze1Objects[i][0]-1)*16-playerX+144), ((maze1Objects[i][1]-1)*16-playerY+80))
        if maze1Objects[i][2] == keyObj:
            window.blit(keySprite, mazeObjectCoords)
        if maze1Objects[i][2] == closedGateTopObj:
            window.blit(lockedGateTop, mazeObjectCoords)
        if maze1Objects[i][2] == closedGateBottomObj:
            window.blit(lockedGateBottom, mazeObjectCoords)
        
    
    roundedWalkFrame = math.floor(playerWalkFrame)
    
    #player sprite rendering
    for x in range(4):
        for y in range(3):
            if x == playerDirection:
                if y == roundedWalkFrame:
                    window.blit(playerSpriteList[y][x], guyRect)
    
    #reading/talking checks
    shownDialogue = []
    if reading or talking:
        window.blit(dialogueBox, (0,0))
    if reading:
        window.blit(signPortrait, (34, 162))
        for i in range(len(signText)):
            if signText[i][0] == checkedTileX and signText[i][1] == checkedTileY:
                for j in range(len(signText[i])):
                    if isinstance(signText[i][j], str):
                        shownDialogue.append(signText[i][j])
        if len(shownDialogue) >= 1:
            dialogueLine1 = font1.render(shownDialogue[0], False, (255,255,255))
            dialogueLine1Rect = dialogueLine1.get_rect()
            dialogueLine1Rect.topleft = (100,150)
            dialogueLine1Shadow = font1.render(shownDialogue[0], True, (0,0,0))
            dialogueLine1ShadowRect = dialogueLine1Shadow.get_rect()
            dialogueLine1ShadowRect.topleft = (99,151)
        else:
            dialogueLine1 = font1.render("", False, (255,255,255))
            dialogueLine1Rect = dialogueLine1.get_rect()
            dialogueLine1Rect.topleft = (100,150)
            dialogueLine1Shadow = font1.render("", True, (0,0,0))
            dialogueLine1ShadowRect = dialogueLine1Shadow.get_rect()
            dialogueLine1ShadowRect.topleft = (99,151)
        if len(shownDialogue) >= 2:
            dialogueLine2 = font1.render(shownDialogue[1], False, (255,255,255))
            dialogueLine2Rect = dialogueLine2.get_rect()
            dialogueLine2Rect.topleft = (100,175)
            dialogueLine2Shadow = font1.render(shownDialogue[1], True, (0,0,0))
            dialogueLine2ShadowRect = dialogueLine2Shadow.get_rect()
            dialogueLine2ShadowRect.topleft = (99,176)
        else:
            dialogueLine2 = font1.render("", False, (255,255,255))
            dialogueLine2Rect = dialogueLine2.get_rect()
            dialogueLine2Rect.topleft = (100,175)
            dialogueLine2Shadow = font1.render("", True, (0,0,0))
            dialogueLine2ShadowRect = dialogueLine2Shadow.get_rect()
            dialogueLine2ShadowRect.topleft = (99,176)
        if len(shownDialogue) >= 3:
            dialogueLine3 = font1.render(shownDialogue[2], False, (255,255,255))
            dialogueLine3Rect = dialogueLine3.get_rect()
            dialogueLine3Rect.topleft = (100,200)
            dialogueLine3Shadow = font1.render(shownDialogue[2], True, (0,0,0))
            dialogueLine3ShadowRect = dialogueLine3Shadow.get_rect()
            dialogueLine3ShadowRect.topleft = (99,201)
        else:
            dialogueLine3 = font1.render("", False, (255,255,255))
            dialogueLine3Rect = dialogueLine3.get_rect()
            dialogueLine3Rect.topleft = (100,200)
            dialogueLine3Shadow = font1.render("", True, (0,0,0))
            dialogueLine3ShadowRect = dialogueLine3Shadow.get_rect()
            dialogueLine3ShadowRect.topleft = (99,201)
        window.blit(dialogueLine1Shadow, dialogueLine1ShadowRect)
        window.blit(dialogueLine1, dialogueLine1Rect)
        window.blit(dialogueLine2Shadow, dialogueLine2ShadowRect)
        window.blit(dialogueLine2, dialogueLine2Rect)
        window.blit(dialogueLine3Shadow, dialogueLine3ShadowRect)
        window.blit(dialogueLine3, dialogueLine3Rect)
        
    #UI rectangle thing
    rect(window, (10, 37, 86), (0, 0, 320, 48))
    window.blit(statBars,  (3, 8))
    #stamina bar rectangles
    for i in range(20):
        if i <= playerStamina:
            rect(window, (19, 121, 55), ((33 + (i*6)), 10, 5, 11))
    #health bar rectangles
    for i in range(20):
        if i <= playerHealth:
            rect(window, (190, 14, 14), ((33 + (i*6)), 27, 5, 11))
    #keys and items and stuff
    window.blit(keySprite, (160, 8))
    keyTotalText = font1.render(("x " + str(heldKeys)), False, (255,255,255))
    keyTotalTextRect = keyTotalText.get_rect()
    keyTotalTextRect.midleft = (175, 16)
    keyTotalShadow = font1.render(("x " + str(heldKeys)), True, (0,0,0))
    keyTotalShadowRect = keyTotalText.get_rect()
    keyTotalShadowRect.midleft = (174, 17)
    window.blit(keyTotalShadow, keyTotalShadowRect)
    window.blit(keyTotalText, keyTotalTextRect)
    
    #fps counter
    if fpsShown:
        renderText(str(int(clock.get_fps())), (255, 255, 255), (0, 220))
    
    pygame.display.flip()