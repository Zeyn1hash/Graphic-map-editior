from config import *
from models.sprite import Sprite
from models.line_edit import LineEdit
from models.draw_multiline_text import draw_multiline_text

def give_name_loop():

    upload_button=Sprite(window.get_width()/2-20*10/2, 450, "images/Upload button.png", 20*10, 20*10)
    #list_button=Sprite(window.get_width()/2-83*5/2, 550, "images/List button.png", 83*5, 40*5)
    input_name=LineEdit(window.get_width()/2-100*10/2, 180, 100*10, 100,"AuX_DotBitC_Xtra.ttf", "Map name")
    start_button=Sprite(window.get_width()/2-103*5/2, 750, "images/Start button disabled.png", 103*5, 40*5)

    start_buttons=[transform.scale(image.load("images/Start button disabled.png"), (103*5, 40*5)),
                   transform.scale(image.load("images/Start button enabled.png"), (103*5, 40*5))]
    start_enabled=False

    while True:
        for e in event.get():
            if e.type == QUIT:
                return "quit"
            if e.type == KEYDOWN:
                if e.key == K_1:
                    return "game"
                elif e.key == K_2:
                    return "editor"
                elif e.key == K_ESCAPE:
                    return "menu"

            if e.type == MOUSEBUTTONDOWN:
                if upload_button.rect.collidepoint(e.pos):
                    return "editor"
                if start_button.rect.collidepoint(e.pos) and start_enabled:
                    return "editor"
            input_name.handle_event(e)

        if len(input_name.text)>0:
            start_button.image=start_buttons[1]
            start_enabled=True
        else:
            start_button.image = start_buttons[0]
            start_enabled = False

        window.fill("lightblue")
        upload_button.draw()
        #list_button.draw()
        start_button.draw()
        input_name.draw(window)

        window.blit(font.Font("AuX_DotBitC_Xtra.ttf", 50).render("Enter a name for the new map below", True, "black"), (60, 100))
        window.blit(font.Font("AuX_DotBitC_Xtra.ttf", 50).render("Or upload an existing one", True, "black"), (250, 380))


        #draw_multiline_text("Enter a name for the new map below\n a", font.Font("AuX_DotBitC_Xtra.ttf", 50),
        #                    "black", window, 60, 100, 50)

        display.update()
        clock.tick(60)