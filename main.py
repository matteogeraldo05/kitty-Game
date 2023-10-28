#Matteo De Angelis gEraldo
#~ Meow Mewo Kirtty game!
import pygame
from pygame import mixer
import random
import sys
import time

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

def maxwellScreen():
    pygame.display.set_caption("THE LEGENDARY MAXWELL") 
    
#@ THE PEN15 (EEK)! :O
    mixer.music.load("audio/maxwell.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.9)

    #& take all the maxwell frames to animate gif later
    maxwell = []
    for i in range(30):
        filePath = f"sprites/maxwell/frame_{i}.png"
        image = pygame.image.load(filePath)
        maxwell.append(image)

    while True:
        for event in pygame.event.get():  
        #& Quit 
            if event.type == pygame.QUIT: 
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                elif event.key == pygame.K_p:
                    reactionTime()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game()

        currentFrame = pygame.time.get_ticks() // 100 % 30
        gameScreen.fill((255, 255, 255))
        gameScreen.blit(maxwell[currentFrame], (0, 50))
    #& Game Text    
        maxwellText = font.render("DO NOT THE CAT", True, (0, 0, 0), (255, 255, 255))
        bottomText = font.render("BOTTOM TEXT", True, (0, 0, 0), (255, 255, 255))
        gameScreen.blit(maxwellText, (100, 20))
        gameScreen.blit(bottomText, (100, 300))
        pygame.display.update()    

#~ -------------------------------------------BUG-SQUISG-------------------------------------------------------------------

def game():
    pygame.display.set_caption("The kitty Game") 

#@ mew mew mewsi
    mixer.music.load("audio/MewMew.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.7)
#@ sound effects
    splat = mixer.Sound("audio/splat.wav")
    miss = mixer.Sound("audio/mwomp.wav")
    yay = mixer.Sound("audio/yay.wav")
    
    clock = pygame.time.Clock()

#$ i am losing my grip on rythm :333
    pawImg = pygame.image.load("sprites/pawUp.png")
    hitImg = pygame.image.load("sprites/pawHit.png")
    restImg = pygame.image.load("sprites/rest.png")
    thumbsUpImg = pygame.image.load("sprites/thumbsUp.png")

    def fadeInOut(thumbsUpImg):
        for i in range(0, 256, 10):
            thumbsUpImg.set_alpha(i)
            gameScreen.blit(thumbsUpImg, (0, 0))
            pygame.display.update()
            pygame.time.delay(int(1.5 * 1000 / 51)) 
        
        for i in range(255, 0, -10):
            gameScreen.fill((135, 206, 235))
            gameScreen.blit(table, (0, screenHeight-110))
            gameScreen.blit(restImg, (0, 0)) 
            
        #& Game Text
            killCountText = font.render(f"bugs squashed: {bugKillCount}", True, (255, 255, 255))
            gameScreen.blit(killCountText, (5, 5)) 
            livesCountText = font.render(f"Lives:{catLives}", True, (255, 255, 255))
            gameScreen.blit(livesCountText, (275, 5)) 
            
            thumbsUpImg.set_alpha(i)
            gameScreen.blit(thumbsUpImg, (0, 0))
            pygame.display.update()
            pygame.time.delay(int(1.5 * 1000 / 51))
    
    bugImg = pygame.image.load("sprites/cock.png")
    table = pygame.image.load("sprites/table.png")

    hit = False
    bugKillCount = 0
    lastTick = pygame.time.get_ticks()
    xPos = 360
    spawnBug = False
    hitRect = None
    catLives = 9
    scoreRewarded = False

    def randomBugSpeed():
        bugSpeed = random.randint(3, 9)
        #print(bugSpeed)
        return bugSpeed

#& Game loop
    notRatiod = True  
    while notRatiod:       
        pygame.display.flip() #update
        
        for event in pygame.event.get():   
        #& Quit 
            if event.type == pygame.QUIT: 
                pass
            #^ HAHHHAH NO EXIT FROM GATO!!!
                #sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit = True
                    lastTick = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit = True
                lastTick = pygame.time.get_ticks()
        
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
    
    #$ Reward player with image and sound for meowing meow mao mew mew mrrp mamaamakspdjsohfhj
        if (bugKillCount % 10) == 0 and bugKillCount > 0 and not scoreRewarded:
            yay.play()
            fadeInOut(thumbsUpImg) 
            scoreRewarded = True
            
        elif (bugKillCount % 10) != 0:
            scoreRewarded = False



    #@ Update screen
        clock.tick(60)
        pygame.display.update()

#~ -------------------------------------------REACTION-TIME-------------------------------------------------------------------

def reactionTime():
    pygame.display.set_caption("Reaction kitty (SECRET MODE!!)!") 

#@ mew mew mewsi
    mixer.music.load("audio/yooo.wav") #! STRONGER DOES NOT EXIST
    mixer.music.play()
    mixer.music.set_volume(1)
#@ sound effects
    boom = mixer.Sound("audio/vineBoom.wav")
    miau = mixer.Sound("audio/miau.wav")
    
    clock = pygame.time.Clock()

#$ i am losing my grip on reality :333
    doNot = pygame.image.load("sprites/doNot.png")
    theCat = pygame.image.load("sprites/theCat.png")
    thumbsUpImg = pygame.image.load("sprites/thumbsUp.png")
    
    score = 0
    catLives = 9
    randomSeconds = random.randint(7000, 11000)
    startTime = pygame.time.get_ticks()
    reactionTimer = False
    reactionWindow = 1000 
    pressed = False  

#& Game loop
    notRatiod = True  
    while notRatiod:       
        pygame.display.flip() #update
        gameScreen.fill((150, 108, 230))

        for event in pygame.event.get(): 
            #& Quit 
            if event.type == pygame.QUIT: 
                #pass
                sys.exit()   
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed = True  
        
        currentTime = pygame.time.get_ticks()
        if currentTime - startTime >= randomSeconds and not reactionTimer:
            doNot = theCat
            miau = miau.play()
            reactionTimer = True
            reactionStartTime = pygame.time.get_ticks()   

    #! penalty for early click
        if pressed and (reactionTimer == False):
            print("TO EARLY")
            endScreen()

    #& spacebar check within 1 second window
        if reactionTimer:
            reactionTime = pygame.time.get_ticks() - reactionStartTime
            if pressed:
                if reactionTime <= reactionWindow:
                    miau.stop()
                    boom.play()
                    maxwellScreen()
                else:
                    endScreen()
            
            
        pressed = False  
        if catLives <= 0:
            endScreen()

        
        gameScreen.blit(doNot, (0, 0))

        clock.tick(60)
        pygame.display.update()


titleScreen()