import pygame
import finalebuttons
import finale_functions
pygame.init()
for i in range(0,40):
    finale_functions.add_task("test","test")
button_array = []
screen = pygame.display.set_mode([1280, 720])
def main():
    '''Runs the main GUI loop'''
    running = True
    while running:
        tasks = finale_functions.read_tasks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        task_list_length = len(tasks)
        current_y = 10
        for task in tasks:
            button_array.append(finalebuttons.done(700, current_y, "", screen))
            current_y += 60
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
