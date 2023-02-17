import pygame
pygame.init()

canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption('hello world')
run = True


def button(button_x, button_y, button_width, button_height, mouse_pressed, mouse_position):
    pygame.draw.rect(canvas, (255, 0, 0), (button_x, button_y, button_width, button_height))
    if mouse_pressed[0]:
        if mouse_position[0] >= button_x and mouse_position[0] <= button_x + button_width \
                and mouse_position[1] >= button_y and mouse_position[1] <= button_y + button_width:
            return True
    return False


x = 400
y = 350

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

while run:
    milliseconds = clock.tick(128)

    canvas.fill((255, 255, 255))
    seconds = milliseconds / 1000
    if pygame.key.get_pressed() [pygame.K_RIGHT]:
        x += 10
    if pygame.key.get_pressed() [pygame.K_LEFT]:
        x -= 10
    if pygame.key.get_pressed() [pygame.K_UP]:
        y -= 10
    if pygame.key.get_pressed() [pygame.K_DOWN]:
        y += 10

    f = pygame.mouse.get_pressed()
    gps = pygame.mouse.get_pos()

    if button(60, 20, 60, 50, f, gps):
        y -= 10
    if button(10, 80, 60, 50, f, gps):
        x -= 10
    if button(110, 80, 60, 50, f, gps):
        x += 10
    if button(60, 150, 60, 50, f, gps):
        y += 10

    pygame.draw.circle(canvas, (0, 130, 0), (x, y), 70)

    if seconds != 0:
        text_surface = font.render(str(int(1 // seconds)), False, (0, 0, 0))
        canvas.blit(text_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
