import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
blue = (0, 255, 255)
pink = (255, 0, 255)
is_blue = True
screen.fill(blue)
pygame.display.update()
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if is_blue is True:
            screen.fill(pink)
            is_blue = False
        else:
            screen.fill(blue)
            is_blue = True
        pygame.display.update()
        print('Mouse Button Down Event!')
        print(f"Key Position is : {event.pos}")
        print(f"Key Button is : {event.button}")

    if event.type == pygame.QUIT:
        pygame.quit()
        break