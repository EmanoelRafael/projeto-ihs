import pygame
import os, sys
import time
import random
#from fcntl import ioctl
#from iotcl_cmds import *
"""
if len(sys.argv) < 2:
    print("Error: expected more command line arguments")
    print("Syntax: %s </dev/device_file>"%sys.argv[0])
    exit(1)

fd = os.open(sys.argv[1], os.O_RDWR)"""

pygame.init()
pygame.font.init()

width, height = 1200, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo IHS")
circlesPosX = 300
circlesPosY = 150
switchesPosX = 170
switchesPosY = 350
switchNumber = 0
switchNumberPosX = 180 
switchNumberPosY = 570

randomTicks = []

WHITE = (255, 255, 255)
GREEN = 9, 125, 30
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
LIGHTBLUE = (42, 194, 245)
GRAY = 80, 80, 82
YELLOw = 247,191,64

MENU_BACKGROUND = pygame.transform.scale(pygame.image.load("menu-background.jpg"), (width, height))

def game():
    global level
    global speed
    speed = 0.8
    FPS = 60
    running = True
    clock = pygame.time.Clock()
    level = 1
    gameFont = pygame.font.SysFont("comicsans", 50)

    def redraw():

        screen.fill(YELLOw)

        global randomTicks
        global level
        global speed

        levelLabel = gameFont.render("Nível : " + str(level), 1, WHITE)
        screen.blit(levelLabel, (20, 20))

        randomTicks = []
        userInput = []

        testLabel = gameFont.render("Jogo da memória", 1, (255, 255, 255))
        switchNumber = 1
        a = 0

        for i in range(0, 4):
            pygame.draw.circle(screen, WHITE, [circlesPosX + 200 * i, circlesPosY], 50, 120)
        
        for i in range(0, 18):
            pygame.draw.rect(screen, WHITE, pygame.Rect(switchesPosX + 50*i, switchesPosY, 40, switchesPosX+20))
            numberLabel = gameFont.render(str(switchNumber), 1, WHITE)
            screen.blit(numberLabel, (switchNumberPosX + 50 * i, switchNumberPosY))
            switchNumber += 1

        for i in range(0, level):
            if i % 2 == 0:
                a = random.randint (0, 3)
            else:
                a = random.randint(0, 17)
            
            randomTicks.append((i % 2, a))

        for rr in randomTicks:
            print(rr)

        print("\n")

        for rr in randomTicks:
            if rr[0] == 0:
                pygame.draw.circle(screen, GRAY, [circlesPosX + 200 * rr[1], circlesPosY], 50, 120)
                pygame.display.update()
                time.sleep(speed)
                pygame.draw.circle(screen, WHITE, [circlesPosX + 200 * rr[1], circlesPosY], 50, 120)
                pygame.display.update()
                time.sleep(speed)
            else:
                pygame.draw.rect(screen, GRAY, pygame.Rect(switchesPosX + 50 * rr[1] , switchesPosY, 40, switchesPosX+20))
                pygame.display.update()
                time.sleep(speed)
                pygame.draw.rect(screen, WHITE, pygame.Rect(switchesPosX + 50 * rr[1] , switchesPosY, 40, switchesPosX+20))
                pygame.display.update()
                time.sleep(speed)

        #while len(userInput) < level: 
        """ if len(userInput) % 2 == 0:
                ioctl(fd, RD_PBUTTONS)
                userInput.append(( len(userInput % 2), os.read(fd, 1) ))
            else:
                ioctl(fd, RD_SWITCHES)
                userInput.append(( len(userInput % 2), os.read(fd, 1) )) """
        
        # Como só pode ler um periférico por vez, vou ler cada um dos periféricos por vez.
            # Get input from user.
        # Aqui realizar o teste de leitura dos periféricos -> Ver se dá match com o o que tem no random.
        
        correct = True

        userInput = randomTicks
        #for i in range(0, level):
        #    userInput.append((i, 1))

        for i in range(0, level):
            if userInput[i] != randomTicks[i]:
                correct = False
        
        if not correct:
            levelLoseLabel = gameFont.render("Perdeu", 1, RED)
            screen.blit(levelLoseLabel, (550, 300))
            pygame.display.update()
            time.sleep(1.5)
            #se errou ligar todos os leds vermelhos e apagar todos os leds verdes.
            
            """data = 0xFFFFFFFF
            ioctl(fd, WR_RED_LEDS)
            os.write(fd, data.to_bytes(4, 'little'))
            data = 0x0
            ioctl(fd, WR_GREEN_LEDS)
            os.write(fd, data.to_bytes(4, 'little'))"""

        else:
            
            screen.fill(YELLOw)
            levelWinLabel = gameFont.render("Venceu", 1, GREEN)
            screen.blit(levelWinLabel, (530, 300))
            levelWinInstructionLabel = gameFont.render("Desligue todos os switches", 1, GREEN)
            levelWinClick = gameFont.render("Clique em algum botão para avançar para o próximo nível", 1, GREEN)
            screen.blit(levelWinInstructionLabel, (380, 500))
            screen.blit(levelWinClick, (130, 550))
            pygame.display.update()
            time.sleep(8)
            speed -= 0.02
            level += 1

            # Se acertou, ligar os leds verdes e apagar os leds vermelhos.
            """data = 0x0
            ioctl(fd, WR_RED_LEDS)
            os.write(fd, data.to_bytes(4, 'little'))
            data = 0xFFFFFFFF
            ioctl(fd, WR_GREEN_LEDS)
            os.write(fd, data.to_bytes(4, 'little'))"""
        

        pygame.display.update()

    while running:

        clock.tick(FPS)
        redraw()
        randomTicks = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
        # A partir daqui testes com a leitura nos periféricos.
        
        # A partir daqui testes com escrita nos periféricos. 

        # Joguinho da memória? sim...
        # Precisa criar menu?????

def main_menu():
    # OUTPUT 
    screen.blit(MENU_BACKGROUND, (0, 0))
    menuFont = pygame.font.SysFont("Helvetica", 50)
    menuLabel = menuFont.render("Jogo da memória", 1, WHITE)
    screen.blit(menuLabel, (140, 300))
    startLabel = menuFont.render("Clique para iniciar o jogo", 1, WHITE)
    screen.blit(startLabel, (50, 500))
    pygame.display.update()
    
    runningMenu = True
    while runningMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningMenu = False
            elif event.type == pygame.MOUSEBUTTONUP:
                game()

main_menu()

#os.close(fd)
