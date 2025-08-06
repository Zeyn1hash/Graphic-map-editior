from config import *
from core.buttons import *
from core.grid import create_grid
from models.map_export import export_map_as_symbols

a=1
# block.image = transform.scale(image.load(block_images[block.type]), (width, height))
def get_object_category(obj, obj_dict):
    for key, lst in obj_dict.items():
        if obj in lst:
            return key
    return None


grid, horizontal, vertical, grid_screen = create_grid(window.get_width(), window.get_height())
objects = {"grass": [], "spikes": [], "ice": [], "doors": [], "enemies": []}
block_type = {0: "grass", 1: "spikes", 2: "ice", 3: "doors", 4: "enemies"}
#grid_screen = Surface((window.get_width(), window.get_height()), SRCALPHA)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            for btn in buttons:
                if btn["button"].rect.collidepoint(e.pos):
                    for b in buttons:
                        b["activated"] = False
                    btn["activated"] = True
    keys = key.get_pressed()
    if keys[K_e]:  # Експорт при натисканні E
        export_map_as_symbols(objects, 40 * 5, 13 * 5)

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
                        # for list in objects:
                        #    print(list)
                        #    for object in objects[list]:
                        #        print(object.rect.x, object.rect.y)
                        category = get_object_category(new_block, objects)
                        if category == "grass":
                            for obj in objects[category]:
                                # print("Об'єкт:", category)
                                obj.update_type(objects[category])
                                obj.image = transform.scale(image.load(block_images[obj.type]),
                                                            (obj.rect.width, obj.rect.height))

                # for list in objects.values():
                #    for obj in list:
                #        if list.index(obj)==1 or list.index(obj)==3:
                #            obj.update_type(objects)
                #            obj.image = transform.scale(image.load(block_images[obj.type]), (obj.rect.width, obj.rect.height))

    if mouse_buttons[2]:
        for l_key in objects:
            for obj in objects[l_key]:
                if obj.rect.collidepoint(x, y):
                    objects[l_key].remove(obj)
                if objects[l_key] == "grass":
                    obj.update_type(objects[l_key])
                    obj.image = transform.scale(image.load(block_images[obj.type]), (obj.rect.width, obj.rect.height))

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

    display.update()
    clock.tick(60)
