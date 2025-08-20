from PyQt6.QtWidgets import QFileDialog, QApplication
from models.block import Block

def import_map():
    app = QApplication([])

    try:
        path, _ = QFileDialog.getOpenFileName()
        print(path)
        with open(path, "r") as file:
            text = file.read()
            file_name = path.split("/")[-1]
            # d =json.load(file)

        lines=text.splitlines()
        objects = {"grass": [], "spikes": [], "ice": [], "doors": [], "enemies": []}

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "g":
                    objects["grass"].append(Block(x, y, "images/Земля (1).png", 40*5, 13*5, char))
                if char == "#":
                    objects["grass"].append(Block(x, y, "images/Земля (нижче1).png", 40*5, 13*5, char))
                if char == "(":
                    objects["grass"].append(Block(x, y, "images/Земля (пв).png", 40 * 5, 13 * 5, char))
                if char == ")":
                    objects["grass"].append(Block(x, y, "images/Земля (пн).png", 40 * 5, 13 * 5, char))
                if char == "0":
                    objects["grass"].append(Block(x, y, "images/Земля (піл).png", 40 * 5, 13 * 5, char))
                if char == "p":
                    objects["grass"].append(Block(x, y, "images/Земля (платформа).png", 40 * 5, 13 * 5, char))
                if char == "^":
                    objects["spikes"].append(Block(x, y, "images/Шипи.png", 40 * 5, 13 * 5, char))
                if char == "i":
                    objects["ice"].append(Block(x, y, "images/Лід.png", 40 * 5, 13 * 5, char))
                if char == "S":
                    objects["doors"].append(Block(x, y, "images/Двері (block_S).png", 20*5, 39*5, char))
                if char == "F":
                    objects["doors"].append(Block(x, y, "images/Двері (block_F).png", 20*5, 39*5, char))

        return objects
    except Exception as e:
        print(e)