import pygame
import finalebuttons
import finale_functions

pygame.init()
pygame.font.init()

for i in range(0,5):
    finale_functions.add_task("test","test")
button_array = []
screen = pygame.display.set_mode([1280, 720])
def main():
    '''Runs the main GUI loop'''
    running = True
    while running:
        screen.fill((255, 255, 255))
        current_y = 10
        tasks = finale_functions.read_tasks()
        for task in tasks:
            button_array.append(finalebuttons.done(700, current_y, "", screen))
            current_y += 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for button in button_array:
                    print(pos)
                    if button.is_location(pos):
                        finale_functions.delete_task(int(button.text))
        task_list_length = len(tasks)
        pygame.display.flip()
        button_array.clear()

if __name__ == "__main__":
    main()
    pygame.quit()
