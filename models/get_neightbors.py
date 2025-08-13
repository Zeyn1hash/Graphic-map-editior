def get_neighbors(obj, all_blocks):
    neighbors = []  # список сусідів для збереження
    x, y = obj.rect.x, obj.rect.y  # координати поточного блоку
    w, h = obj.rect.width, obj.rect.height  # розміри блоку

    # Зсуви по 4 напрямках: ліво, право, вверх, вниз
    offsets = [(-w, 0), (w, 0), (0, -h), (0, h)]

    # Для кожного напрямку
    for dx, dy in offsets:
        # Перевіряємо всі блоки у списку
        for block in all_blocks:
            # Якщо координати блоку відповідають сусідній позиції
            if block.rect.x == x + dx and block.rect.y == y + dy:
                neighbors.append(block)  # додаємо в список сусідів

    return neighbors  # повертаємо список сусідів
