import pyttsx3
import pygame
import time

pygame.init()

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg1 = pygame.image.load('../sprite/01.png')
carImg2 = pygame.image.load('../sprite/02.png')

def car():
    gameDisplay.blit(carImg1, (300,200))
def car2():
    gameDisplay.blit(carImg2, (300,200))

x =  (display_width * 0.45)
y = (display_height * 0.8)
i = 0
c = i
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            """ RATE"""
            rate = engine.getProperty('rate')   # getting details of current speaking rate
            print (rate)                        #printing current voice rate
            engine.setProperty('rate', 125)     # setting up new voice rate


            """VOLUME"""
            volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
            print (volume)                          #printing current volume level
            engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

            """VOICE"""
            voices = engine.getProperty('voices')       #getting details of current voice
            #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

            engine.say("Sa was dee")
            engine.say('My name is Guitar ' + str(rate))
            engine.runAndWait()
            engine.stop()

            """Saving Voice to a file"""
            # On linux make sure that 'espeak' and 'ffmpeg' are installed
            engine.save_to_file('Hello World', 'test.mp3')
            engine.runAndWait()
            gameDisplay.fill(white)
    
    if(c == 0):
        car()
        time.sleep(0.4)
        i+=1
        c = i%2
        
    else:
        car2()
        time.sleep(0.4)
        i+=1%2
        c = i%2
        
        
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()



