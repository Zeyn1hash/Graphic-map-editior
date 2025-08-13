def export_map_as_symbols(objects_dict, tile_width, tile_height):
    max_col = 0
    max_row = 0

    obj_list=sum(objects_dict.values(), [])
    x_offset = min(block.rect.x for block in obj_list)
    y_offset = min(block.rect.y for block in obj_list)
    print("Offset:", x_offset, y_offset)

    for block_list in objects_dict.values():
        for block in block_list:
            #y_offset=-block_list[0].rect.y
            #print("Відступ:", x_offset, y_offset)
            col = (block.rect.x-x_offset) // tile_width
            row = (block.rect.y-y_offset) // tile_height
            max_col = max(max_col, col)
            max_row = max(max_row, row)

    # Створюємо порожню карту, заповнену пробілами
    map_data = [["_" for _ in range(max_col + 1)] for _ in range(max_row + 1)]


    for block_list in objects_dict.values():
        for block in block_list:
            col = (block.rect.x-x_offset) // tile_width
            row = (block.rect.y-y_offset) // tile_height
            symbol = block.symbol
            map_data[row][col] = symbol

    with open("data/map test", "w") as f:
        for row in map_data:
            f.write("".join(row) + "\n")

    return map_data
