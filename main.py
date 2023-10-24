#Matteo De Angelis gEraldo
#~ Meow Mewo Kirtty game!
import pygame
from pygame import mixer
import random

def showtitleScreen():
    tileScreen = pygame.image.load("sprites/uniChicken.png")
    pass

def endScreen():
    gameOver = pygame.image.load("sprites/thisCannotContinue.png")
    pygame.init()
    pygame.display.set_caption("The kitty Game Over :(") 
    kittyIcon = pygame.image.load("favicon.ico")
    pygame.display.set_icon(kittyIcon)

    gameOverScreen = pygame.display.set_mode(size=(360, 360))
    gameOverScreen.blit(gameOver, (0, 0))
    mixer.music.stop()
    scream = mixer.Sound("audio/gameOver.wav")
    scream.play() #$ THJSI SIOS SO GOOD HAAHAWBAWHWHAHH

    pygame.display.update()

def main():

    pygame.init()
    pygame.display.set_caption("The kitty Game") 
    kittyIcon = pygame.image.load("favicon.ico")
    pygame.display.set_icon(kittyIcon)

#@ mew mew mewsic
    mixer.init()
    mixer.music.load("audio/MewMew.wav")
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.7)
#@ sound effects
    splat = mixer.Sound("audio/splat.wav")
    miss = mixer.Sound("audio/mwomp.wav")
    
#&Window Settings
    screenWidth = 360
    screenHeight = 360
    gameScreen = pygame.display.set_mode(size=(360, 360))
    
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

    def randomBug():
        bugHeight = random.randint(250, 300)
        print(bugHeight)
        return bugHeight
        

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
                notRatiod = False    
        
        #? UNI ANIMATION - DONT TOUCH
        nowTick = pygame.time.get_ticks()
        if hit:
            if nowTick - lastTick <= 100:
                uniImg = pawImg
            elif 100 < nowTick - lastTick <= 450:
                uniImg = hitImg
                hitRect = pygame.Rect(100, 250, 20, 110)
                
            else:
                hit = False
                uniImg = restImg
                hitRect = None
        else:
            uniImg = restImg

        #& spawn bug
        if spawnBug == False:
            spawnBug = True
            xPos = 500
            bugHeight = random.randint(250, 300)
        else:
            gameScreen.blit(bugImg, (xPos, bugHeight))
        
        #& If uni misses bug
        if xPos <= 0:
            if spawnBug == True:
                miss.play()
                catLives -= 1
                spawnBug = False
            xPos = 380
        else:
            xPos -= 6.6
        
        #& GameOver Check
        if catLives <= 0:
            endScreen() #todo possible idea: if catLives = 0, delete system 32

        gameScreen.fill((135, 206, 235)) #& fill screen before kitty so gato show not screen :3p
    #! TABLE
        gameScreen.blit(table, (0, screenHeight-110))

    #$ BUG YUCK!
        if spawnBug == True:
            bugRect = pygame.Rect(xPos, 315, 10, 10)
            pygame.draw.rect(gameScreen, (1, 1, 1), bugRect)

            if hitRect is not None and hitRect.colliderect(bugRect):
                splat.play()
                bugKillCount += 1
                spawnBug = False
                print("KILLED BUG@!")
    #? UNI the CAT
        gameScreen.blit(uniImg, (0, 0))
        
    #& Debug Menu Text
        font = pygame.font.Font("freesansbold.ttf", 16)
        killCountText = font.render(f"bugs squashed: {bugKillCount} \n lives:{catLives}", True, (255, 255, 255))
        killCountTextRect = killCountText.get_rect()
        gameScreen.blit(killCountText, killCountTextRect) 

    #@ Update screen
        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()