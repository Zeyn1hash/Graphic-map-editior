from config import window
from models.block import Block
from models.sprite import Sprite

buttons=[{"button": Sprite(window.get_width() - 220, 33, "images/Земля (1).png", 40 * 5, 13 * 5),
          "activated": False,
          "object": Block(0, 0, "images/Земля (1).png", 40*5, 13*5, "g")},
         {"button": Sprite(window.get_width() - 220, 118, "images/Шипи.png", 40 * 5, 13 * 5),
          "activated": False,
          "object": Block(0, 0, "images/Шипи.png", 40*5, 13*5, "^")},
         {"button": Sprite(window.get_width() - 220, 203, "images/Лід.png", 40 * 5, 13 * 5),
          "activated": False,
          "object": Block(0, 0, "images/Лід.png", 40*5, 13*5, "i")},
         {"button": Sprite(window.get_width() - 220, 287, "images/Двері (S).png", 20 * 5, 20 * 5),
          "activated": False,
          "object": Block(0, 0, "images/Двері (block_S).png", 20*5, 39*5, "S")},
         {"button": Sprite(window.get_width() - 100, 287, "images/Двері (F).png", 20 * 5, 20 * 5),
          "activated": False,
          "object": Block(0, 0, "images/Двері (block_F).png", 20*5, 39*5, "F")}
         ]
button_color = (20, 20, 20)