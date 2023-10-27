#Matteo De Angelis gEraldo
#~ Meow Mewo Kirtty game!
import pygame
from pygame import mixer
import random
import sys
import math

pygame.init()
mixer.init()
kittyIcon = pygame.image.load("favicon.ico")
pygame.display.set_icon(kittyIcon)
screenWidth = 360
screenHeight = 360
gameScreen = pygame.display.set_mode(size=(screenWidth, screenHeight)) #&Window Settings
font = pygame.font.Font("fontFolder/SuperSedan-YzmXv.ttf", 20)

def titleScreen():
    pygame.display.set_caption("The kitty Menu") 
    tileImg = pygame.image.load("sprites/uniChicken.png")
#@ THE PEN15 (EEK)! :O
    mixer.music.load("audio/thePen15EEK.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.8)
    while True:
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                elif event.key == pygame.K_p:
                    reactionTime()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game()
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                sys.exit()
            #& Game Text
        
        gameScreen.blit(tileImg, (0, 0))
        titleText = font.render("Press SPACE/CLICK to play ", True, (255, 255, 255), (22, 32, 42))
        gameScreen.blit(titleText, (3, screenHeight/3.3))
        pygame.display.update()

                

def endScreen():
    pygame.display.set_caption("The kitty Game Over :(") 
    gameOverImg = pygame.image.load("sprites/thisCannotContinue.png")
    mixer.music.stop()
    #scream = mixer.Sound("audio/gameOver.wav") #$ THJSI SIOS SO GOOD HAAHAWBAWHWHAHH
    scream = mixer.Sound("audio/aww.wav") #~ >:( politically corrct end souynd
    scream.play() #$ THJSI SIOS SO GOOD HAAHAWBAWHWHAHH
    while True:
        gameScreen.blit(gameOverImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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

#$ i am losing my grip on rythm :333
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                hit = True
                lastTick = pygame.time.get_ticks()
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                pass
            #^ HAHHHAH NO EXIT FROM GATO!!!
                #sys.exit()
        
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
        
        
    #& Game Text
        killCountText = font.render(f"bugs squashed: {bugKillCount}", True, (255, 255, 255))
        gameScreen.blit(killCountText, (5, 5)) 

        livesCountText = font.render(f"Lives:{catLives}", True, (255, 255, 255))
        gameScreen.blit(livesCountText, (275, 5)) 

    #@ Update screen
        clock.tick(60)
        pygame.display.update()

def reactionTime():
    pygame.display.set_caption("Reaction kitty (SECRET MODE!!)!") 

#@ mew mew mewsi
    #mixer.music.load("audio/Stronger.wav") #! STRONGER DOES NOT EXIST
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.7)
#@ sound effects
    huh = mixer.Sound("audio/huh.wav")
    aww = mixer.Sound("audio/aww.wav")
    scream = mixer.Sound("audio/scream.wav")
    boom = mixer.Sound("audio/vineBoom.wav")
    
    clock = pygame.time.Clock()

#$ i am losing my grip on reality :333
    theGato = pygame.image.load("sprites/goodJob.png")
    
    #squishHeight = 0 #todo animate cat
    score = 0
    catLives = 9
    started = False
    
    threeSeconds = 0

    

#& Game loop
    notRatiod = True  
    while notRatiod:       
        pygame.display.flip() #update

        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
                    
                    
            #& sound effect test
                if event.key == pygame.K_1:
                    huh.play()
                if event.key == pygame.K_2:
                    aww.play()
                if event.key == pygame.K_3:
                    boom.play()
                if event.key == pygame.K_4:
                    scream.play()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                started = True
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                #pass
                sys.exit()
  
    #@ WAIT 3 seconds
        if started:
            #todo Wait three seconds
            pass
            
    #@ IF 3 SECONDS PASS  

    #& Reaction time code
        randomInt = random.randint(1, 300)
        if randomInt == 1:
            theGato = pygame.image.load("sprites/badJob.png")
        else:
            pass
            #print(randomInt)
        
    #& GameOver Check
        if catLives <= 0:
            endScreen()

        gameScreen.fill((150, 108, 230)) #& fill screen before kitty so gato show not screen :3p
    
    #? THE KANYE 
        pygame.draw.rect(gameScreen, (92, 64, 51), pygame.Rect(220, 220, 10, 10))
    #? the CAR
        gameScreen.blit(theGato, ((screenWidth/2)-120, (screenHeight/2)-60))

    #@ Update screen
        clock.tick(60)
        pygame.display.update()

titleScreen()