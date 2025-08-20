from config import *
from models.sprite import Sprite
from models.map_import import import_map

def menu_loop():

    new_project_button=Sprite(window.get_width()/2-141*4/2, 150, "images/New Project button.png", 141*4, 65*4)
    load_button=Sprite(window.get_width()/2-126*4/2, 450, "images/Upload button2.png", 126*4, 40*4)

    list_button=Sprite(window.get_width()/2-83*4/2, 750, "images/List button.png", 83*4, 40*4)


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
                if new_project_button.rect.collidepoint(e.pos):
                    return "new map"
                if load_button.rect.collidepoint(e.pos):
                    import_map()
        window.fill("lightblue")
        new_project_button.draw()
        load_button.draw()

        list_button.draw()

        display.update()
        clock.tick(60)