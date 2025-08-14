from menu import menu_loop
from editor import editor_loop

def main():
    current_state = "menu"  # Починаємо з меню

    while True:
        if current_state == "menu":
            current_state = menu_loop()
        elif current_state == "editor":
            current_state = editor_loop()
        elif current_state == "quit":
            break

if __name__ == "__main__":
    main()
