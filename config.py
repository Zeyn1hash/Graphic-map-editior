from pygame import *

init()
size = 1280, 1024
window = display.set_mode(size)
clock = time.Clock()

block_images = {
    0: transform.scale(image.load("images/Земля (платформа).png"), (40*5, 13*5)),
    1: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    2: transform.scale(image.load("images/Земля (пв).png"), (40*5, 13*5)),
    3: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    4: transform.scale(image.load("images/Земля (піл).png"), (40*5, 13*5)),
    5: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    6: transform.scale(image.load("images/Земля (пв).png"), (40*5, 13*5)),
    7: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    8: transform.scale(image.load("images/Земля (пн).png"), (40*5, 13*5)),
    9: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    10: transform.scale(image.load("images/Земля (1).png"), (40*5, 13*5)),
    11: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    12: transform.scale(image.load("images/Земля (пн).png"), (40*5, 13*5)),
    13: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    14: transform.scale(image.load("images/Земля (1).png"), (40*5, 13*5)),
    15: transform.scale(image.load("images/Земля (нижче1).png"), (40*5, 13*5)),
    # ... до 15
}
