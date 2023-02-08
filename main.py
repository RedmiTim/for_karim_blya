import pygame
pygame.init()

canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption('hello world')
run = True

x = 400
y = 350




clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

while run:

    clock.tick(60)

    canvas.fill((255, 255, 255))


    """
    milliseconds = clock.tick()
    seconds = milliseconds / 1000
    if seconds != 0:
        text_surface = font.render(str(1 / seconds), False, (0, 0, 0))
        canvas.blit(text_surface, (10, 10))
    if pygame.key.get_pressed() [pygame.K_RIGHT]:
        x += 1
    if pygame.key.get_pressed() [pygame.K_LEFT]:
        x -= 1
    if pygame.key.get_pressed() [pygame.K_UP]:
        y -= 1
    if pygame.key.get_pressed() [pygame.K_DOWN]:
        y += 1
    """
    f = pygame.mouse.get_pressed()
    gps = pygame.mouse.get_pos()

    if f[0]:
        if gps[0] >= 60 and gps[0] <= 120 and gps[1] >= 20 and gps[1] <= 70:
            y = y - 10

    if f[0]:
        if gps[0] >= 10 and gps[0] <= 70 and gps[1] >= 80 and gps[1] <= 130:
            x = x - 10

    if f[0]:
        if gps[0] >= 110 and gps[0] <= 170 and gps[1] >= 60 and gps[1] <= 110:
            x = x + 10

    if f[0]:
        if gps[0] >= 60 and gps[0] <= 120 and gps[1] >= 150 and gps[1] <= 200:
            y = y + 10



    pygame.draw.rect(canvas, (255, 0, 0), (60, 20, 60, 50))
    pygame.draw.rect(canvas, (255, 0, 0), (10, 80, 60, 50))
    pygame.draw.rect(canvas, (255, 0, 0), (110, 80, 60, 50))
    pygame.draw.rect(canvas, (255, 0, 0), (60, 150, 60, 50))
    pygame.draw.circle(canvas, (0, 130, 0), (x, y), 70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
