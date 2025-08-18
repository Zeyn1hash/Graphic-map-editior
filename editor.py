from config import *
from core.buttons import *
from core.grid import create_grid
from models.map_export import export_map_as_symbols
from models.get_neightbors import get_neighbors
from models.draw_multiline_text import draw_multiline_text


def editor_loop():
    message_font=font.Font("AuX_DotBitC_Xtra.ttf", 30)
    objects_warring=message_font.render("Для збереження повинні бути \n старт і фініш", 1, 'red')
    warring=False
    warring_cooldown=60

    # def draw_multiline_text(text, font, color, surface, x, y, line_height=5):
    #     lines = text.split("\n")
    #     for i, line in enumerate(lines):
    #         txt_surf = font.render(line, True, color)
    #         surface.blit(txt_surf, (x, y + i * (txt_surf.get_height() + line_height)))


    grid, horizontal, vertical, grid_screen = create_grid(window.get_width(), window.get_height())
    objects = {"grass": [], "spikes": [], "ice": [], "doors": [], "enemies": []}
    block_type = {0: "grass", 1: "spikes", 2: "ice", 3: "doors", 4: "enemies"}
    # grid_screen = Surface((window.get_width(), window.get_height()), SRCALPHA)
    save_button=Sprite(window.get_width() - 120, window.get_height()-120, "images/Discette.png", 20 * 5, 20 * 5)

    while True:
        for e in event.get():
            if e.type == QUIT:
                quit()
            if e.type == MOUSEBUTTONDOWN:
                #-Вибір-блоку---
                for btn in buttons:
                    if btn["button"].rect.collidepoint(e.pos):
                        for b in buttons:
                            b["activated"] = False
                        btn["activated"] = True
                #-Збереження-карти---
                if save_button.rect.collidepoint(e.pos):
                    #show_doors_warring()
                    if len(sum(objects.values(), []))!=0:
                        if buttons[3]["object"] in objects["doors"] and buttons[4]["object"] in objects["doors"]:
                            export_map_as_symbols(objects, 40 * 5, 13 * 5)
                    else:
                        warring=True


        keys = key.get_pressed()
        if keys[K_e]:  # Експорт при натисканні E
            print("Map", export_map_as_symbols(objects, 40 * 5, 13 * 5))

        mouse_buttons = mouse.get_pressed()
        x, y = mouse.get_pos()
        if mouse_buttons[0]:
            for rectangle in grid:
                if rectangle.collidepoint(x, y):

                    # Додати новий блок
                    for button in buttons:
                        if button["activated"]:
                            new_block = button["object"].copy()
                            new_block.rect.x = rectangle.x
                            new_block.rect.y = rectangle.y

                            for list in objects.values():
                                list[:] = [obj for obj in list if not obj.rect.colliderect(new_block.rect)]
                            type_key = block_type[buttons.index(button)]
                            print(len(objects["grass"]))
                            objects[type_key].append(new_block)

                            # print("Список:", objects)
                            # print(new_block.rect.x, new_block.rect.y)
                            # Оновити тип і зображення для всіх блоків

                    for obj in objects["grass"]:
                        obj.update_type(objects["grass"])
                        obj.image = block_images[obj.type]


        if mouse_buttons[2]:

            for l_key in objects:
                for obj in objects[l_key]:
                    if obj.rect.collidepoint(x, y):
                        print("Сусіди:", get_neighbors(obj, sum(objects.values(), [])))
                        objects[l_key].remove(obj)

            for block in objects["grass"]:
                block.update_type(objects["grass"])
                block.image = block_images[block.type]

        window.fill("lightblue")
        # window.blit(grid_screen, (0, 0))
        # grid_screen.fill("lightblue")

        for frame in grid:
            draw.rect(window, (60, 60, 60, 100), frame, 2)
            if frame.x <= -frame.width:
                frame.x += 8 * frame.width
            if frame.x >= window.get_width():
                frame.x -= 8 * frame.width
            if frame.y >= window.get_height():
                frame.y -= 17 * frame.height
            if frame.y <= -frame.height:
                frame.y += 17 * frame.height

        keys = key.get_pressed()

        for list in objects.values():
            # print(list)
            for obj in list:
                # print(obj)
                # draw.rect(window, "red", obj, 4)
                obj.draw()
                if keys[K_w]: obj.rect.y += 5
                if keys[K_s]: obj.rect.y -= 5
                if keys[K_a]: obj.rect.x += 5
                if keys[K_d]: obj.rect.x -= 5

        for frame in grid:
            if keys[K_w]: frame.y += 5
            if keys[K_s]: frame.y -= 5
            if keys[K_a]: frame.x += 5
            if keys[K_d]: frame.x -= 5

        for button in buttons:
            button["button"].draw()
            button["button"].show_hitbox()
            if button["activated"]:
                button["button"].color = "red"
            else:
                button["button"].color = (100, 100, 100)

        save_button.draw()
        if warring:
            if warring_cooldown>0:
                draw_multiline_text("Для збереження повинні \n бути старт і фініш", message_font, "red", window, 800, window.get_height()-200)
                warring_cooldown-=1
            else:
                warring=False
                warring_cooldown=60

        display.update()
        clock.tick(60)
