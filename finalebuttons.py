import pygame

myfont = pygame.font.SysFont('Arial', 20)
class done:
    def __init__(self, x: int, y: int, text: str, surface: pygame.surface):
        this_rect = pygame.Rect((x,y),(50,50))
        pygame.draw.rect(surface, (0, 255, 0, 255), this_rect)
class tasknames:
    def __init__(self, x: int, y: int, text: str):
        self.textsurface = myfont.render(text, False, (0, 0, 0))

