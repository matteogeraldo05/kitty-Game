import pygame
import random

def main():

    pygame.init()
    pygame.display.set_caption("The kitty Game") 
    flappyIcon = pygame.image.load("favicon.ico")
    pygame.display.set_icon(flappyIcon)

    
#&Window Settings
    screenWidth = 360
    screenHeight = 360
    gameScreen = pygame.display.set_mode(size=(screenWidth, screenHeight))
    
    clock = pygame.time.Clock()

    #$ i am losing my grip on reality :333
    pawImg = pygame.image.load("sprites/pawUp.png")
    hitImg = pygame.image.load("sprites/pawHit.png")
    restImg = pygame.image.load("sprites/rest.png")
    
    table = pygame.image.load("sprites/table.png")

    hit = False
    bugKillCount = 0
    lastTick = pygame.time.get_ticks()
    xPos = 360
    spawnBug = False

    def randomBug(bugHeight):
        bugHeight = random.randint(100, 300)
        print(bugHeight)
        

#& Game loop
    notRatiod = True  
    while notRatiod:       
        pygame.display.flip() #update
        
        for event in pygame.event.get():      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit = True
                    spawnBug = True
                    lastTick = pygame.time.get_ticks()
                    
        #& Quit 
            if event.type == pygame.QUIT: 
                notRatiod = False    
        
        nowTick = pygame.time.get_ticks()
        if hit:
            if nowTick - lastTick <= 100:
                uniImg = pawImg
            elif 100 < nowTick - lastTick <= 450:
                uniImg = hitImg
                
            else:
                hit = False
                uniImg = restImg
        else:
            uniImg = restImg
        
        if xPos > 0:
            xPos -= 5
        else:
            xPos = 360

        gameScreen.fill((135, 206, 235)) #& fill screen before kitty so gato show not screen :3p
    #! TABLE
        gameScreen.blit(table, (0, screenHeight-110))
    #$ BUG YUCK!
        if spawnBug == True:
            pygame.draw.rect(gameScreen, (1, 1, 1), pygame.Rect(xPos, 315, 10, 10))
    #? UNI the CAT
        gameScreen.blit(uniImg, (0, 0))
        
    #& Debug Menu Text
        font = pygame.font.Font("freesansbold.ttf", 16)
        killCountText = font.render(f"bugs squashed: {bugKillCount}", True, (255, 255, 255))
        killCountTextRect = killCountText.get_rect()
        gameScreen.blit(killCountText, killCountTextRect) 

    #@ Update screen
        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()