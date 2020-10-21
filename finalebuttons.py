import pygame

#myfont = pygame.font.SysFont('Arial', 20)
class done:
    coordinate_x = 0
    coordinate_y = 0
    text = ""
    def __init__(self, x: int, y: int, text: str, surface: pygame.surface):
        this_rect = pygame.Rect((x,y),(50,50))
        pygame.draw.rect(surface, (0, 255, 0, 255), this_rect)
        self.coordinate_x = x
        self.coordinate_y = y
        self.text = text
    def is_location(coord,otherarg)->bool:
        if coordinate_x <= cord[0] <= coordinate_x + 50 and coordinate_y <= cord[1] <= coordinate_y + 50:
            return False
        else:
            return True

#class tasknames:
    #def __init__(self, x: int, y: int, text: str):
     #   self.textsurface = myfont.render(text, False, (0, 0, 0))

