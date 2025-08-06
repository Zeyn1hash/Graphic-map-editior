def export_map_as_symbols(objects_dict, tile_width, tile_height):
    max_col = 0
    max_row = 0

    for block_list in objects_dict.values():
        for block in block_list:
            col = block.rect.x // tile_width
            row = block.rect.y // tile_height
            max_col = max(max_col, col)
            max_row = max(max_row, row)

    # Створюємо порожню карту, заповнену пробілами
    map_data = [["_" for _ in range(max_col + 1)] for _ in range(max_row + 1)]


    for block_list in objects_dict.values():
        for block in block_list:
            col = block.rect.x // tile_width
            row = block.rect.y // tile_height
            symbol = block.symbol
            map_data[row][col] = symbol

    with open("data/map test", "w") as f:
        for row in map_data:
            f.write("".join(row) + "\n")

    return map_data
