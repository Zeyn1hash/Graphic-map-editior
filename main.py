from main_menu import menu_loop
from editor import editor_loop
from new_map_menu import new_map_loop
#from create import create_menu

def main():
    current_state = "menu"  # Починаємо з меню

    while True:
        if current_state == "menu":
            current_state = menu_loop()
        elif current_state == "editor":
            current_state = editor_loop()
        elif current_state == "new map":
            current_state = new_map_loop()
        elif current_state == "quit":
            break

if __name__ == "__main__":
    main()
