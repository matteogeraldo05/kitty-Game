#Matteo De Angelis gEraldo
#~ Meow Mewo Kirtty game!
import pygame
from pygame import mixer
import random
import sys

pygame.init()
mixer.init()
kittyIcon = pygame.image.load("favicon.ico")
pygame.display.set_icon(kittyIcon)
screenWidth = 360
screenHeight = 360
gameScreen = pygame.display.set_mode(size=(screenWidth, screenHeight)) #&Window Settings

def titleScreen():
    pygame.display.set_caption("The kitty Menu") 
    tileImg = pygame.image.load("sprites/uniChicken.png")
#@ THE PEN15 (EEK)! :O
    mixer.music.load("audio/thePen15EEK.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.8)
    while True:
        gameScreen.blit(tileImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                sys.exit()
                

def endScreen():
    pygame.display.set_caption("The kitty Game Over :(") 
    gameOverImg = pygame.image.load("sprites/thisCannotContinue.png")
    mixer.music.stop()
    scream = mixer.Sound("audio/gameOver.wav")
    scream.play() #$ THJSI SIOS SO GOOD HAAHAWBAWHWHAHH
    while True:
        gameScreen.blit(gameOverImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                sys.exit()

def game():
    pygame.display.set_caption("The kitty Game") 

#@ mew mew mewsi
    mixer.music.load("audio/MewMew.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.7)
#@ sound effects
    splat = mixer.Sound("audio/splat.wav")
    miss = mixer.Sound("audio/mwomp.wav")
    

    
    clock = pygame.time.Clock()

#$ i am losing my grip on reality :333
    pawImg = pygame.image.load("sprites/pawUp.png")
    hitImg = pygame.image.load("sprites/pawHit.png")
    restImg = pygame.image.load("sprites/rest.png")
    
    bugImg = pygame.image.load("sprites/cock.png")
    table = pygame.image.load("sprites/table.png")

    hit = False
    bugKillCount = 0
    lastTick = pygame.time.get_ticks()
    xPos = 360
    spawnBug = False
    hitRect = None
    catLives = 9

    def randomBugSpeed():
        bugSpeed = random.randint(3, 9)
        #print(bugSpeed)
        return bugSpeed

#& Game loop
    notRatiod = True  
    while notRatiod:       
        pygame.display.flip() #update
        
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit = True
                    lastTick = pygame.time.get_ticks()
        #& Quit 
            if event.type == pygame.QUIT: 
                break
        
    #? UNI ANIMATION - DONT TOUCH
        nowTick = pygame.time.get_ticks()
        if hit:
            if nowTick - lastTick <= 100:
                uniImg = pawImg
            elif 100 < nowTick - lastTick <= 450:
                uniImg = hitImg
                hitRect = pygame.Rect(80, 260, 20, 110)
                
            else:
                hit = False
                uniImg = restImg
                hitRect = None
        else:
            uniImg = restImg

    #& spawn bug
        if spawnBug == False:
            spawnBug = True
            randomSpeed = randomBugSpeed()
            xPos = 500
            bugHeight = 215
        else:
            gameScreen.blit(bugImg, (xPos, bugHeight))
        
    #& If uni misses bug
        if xPos <= -30:
            if spawnBug == True:
                miss.play()
                catLives -= 1
                spawnBug = False
            xPos = 380
        else:
            xPos -= randomSpeed #? default is 8.8
        
        #& GameOver Check
        if catLives <= 0:
            endScreen() #todo possible idea: if catLives = 0, delete system 32

        gameScreen.fill((135, 206, 235)) #& fill screen before kitty so gato show not screen :3p
    #! TABLE
        gameScreen.blit(table, (0, screenHeight-110))

    #$ BUG YUCK!
        if spawnBug == True:
            bugRect = pygame.Rect(xPos, 315, 10, 10)
            gameScreen.blit(bugImg, (bugRect.x, 300))
            #pygame.draw.rect(gameScreen, (1, 1, 1), bugRect)

            if hitRect is not None and hitRect.colliderect(bugRect):
                #pygame.draw.rect(gameScreen, (255, 0, 0), hitRect) #show uni hurtbox
                splat.play()
                bugKillCount += 1
                spawnBug = False
                print("KILLED BUG@!")
    #? UNI the CAT
        gameScreen.blit(uniImg, (0, 0))
        
        
    #& Debug Menu Text
        font = pygame.font.Font("freesansbold.ttf", 20)
        killCountText = font.render(f"bugs squashed: {bugKillCount}", True, (255, 255, 255))
        gameScreen.blit(killCountText, (5, 5)) 

        livesCountText = font.render(f"Lives:{catLives}", True, (255, 255, 255))
        gameScreen.blit(livesCountText, (285, 5)) 

    #@ Update screen
        clock.tick(60)
        pygame.display.update()


titleScreen()
#game()