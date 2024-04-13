from pygame import *

window = display.set_mode((700,500))
background = image.load('flag.png')
background = transform.scale(background,(700,500))
clock = time.Clock()

gitler = transform.scale(image.load('gitler.png'),(100,100))
stalin = transform.scale(image.load('stalin.png'),(100,100))

gitler_y = 100
gitler_x = 400

stalin_y = 100
stalin_x = 400

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()
    if keys[K_w]:
        gitler_y -= 10
    if keys[K_s]:
        gitler_y += 10
    if keys[K_a]:
        gitler_x -= 10
    if keys[K_d]:
        gitler_x += 10

    if keys[K_UP]:
        stalin_y -= 10
    if keys[K_DOWN]:
        stalin_y += 10
    if keys[K_LEFT]:
        stalin_x -= 10
    if keys[K_RIGHT]:
        stalin_x += 10

    window.blit(background,(0,0))
    window.blit(gitler,(gitler_x,gitler_y))
    window.blit(stalin,(stalin_x,stalin_y))
    clock.tick(50)
    display.update()
