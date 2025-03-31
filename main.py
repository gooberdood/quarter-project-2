from pygame.locals import *
from functions import *

#main loop
while running:
    #stuff done once a frame (fps cap, events, etc)
    perFrame()
    #gets player input and does stuff with it IE movement
    getInput()
    #detects collision (duh)
    collisionDetection()
    #timing for sprite animations
    animationTiming()
    #lastly, renders everything to the open "mazegame" window
    renderFrame()