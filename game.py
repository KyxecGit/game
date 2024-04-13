from pygame import *

window = display.set_mode((700,500))
background = image.load('flag.png')
background = transform.scale(background,(700,500))

gitler = transform.scale(image.load('gitler.png'),(100,100))
stalin = transform.scale(image.load('stalin.png'),(100,100))

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    window.blit(gitler,(300,100))
    window.blit(stalin,(100,100))
    display.update()