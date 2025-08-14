from config import *
from models.sprite import Sprite

def menu_loop():

    create_button=Sprite(window.get_width()/2-120*5/2, 250, "images/Create button.png", 120*5, 40*5)
    list_button=Sprite(window.get_width()/2-83*5/2, 550, "images/List button.png", 83*5, 40*5)


    while True:
        for e in event.get():
            if e.type == QUIT:
                return "quit"
            if e.type == KEYDOWN:
                if e.key == K_1:
                    return "game"
                elif e.key == K_2:
                    return "editor"
            if e.type == MOUSEBUTTONDOWN:
                if create_button.rect.collidepoint(e.pos):
                    return "editor"
        window.fill("lightblue")
        create_button.draw()
        list_button.draw()

        display.update()
        clock.tick(60)

menu_loop()