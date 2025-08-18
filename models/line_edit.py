from config import *

class LineEdit:
    def __init__(self, x, y, w, h, t_font, ph_text, text=''):
        self.rect = Rect(x, y, w, h)
        self.color_inactive = (100, 100, 100)
        self.color_active = (0, 120, 215)
        self.color = self.color_inactive
        self.text = text
        self.font = font.Font(t_font, 110)
        self.txt_surface = self.font.render(text, True, (0, 0, 0))
        self.active = False
        self.min_width = w
        self.ph_text=self.font.render(ph_text, True, (100, 100, 100))

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # Перевіряємо, чи клікнув користувач в межах поля
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == KEYDOWN and self.active:
            if event.key == K_RETURN:
                print("Введено:", self.text)
                self.text = ''
            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, (0, 0, 0))

    def update(self):
        # Автоматично підлаштовуємо ширину поля
        width = max(self.min_width, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Малюємо текст і рамку
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        if len(self.text)==0:
            screen.blit(self.ph_text, (self.rect.x + 5, self.rect.y + 10))
        draw.rect(screen, self.color, self.rect, 8)