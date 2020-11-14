from rect import *

rect = Rect(100, 50, 50, 50)
v = [2, 2]

rect_is_moving = True
rect_is_hit = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            rect_is_moving = False
            rect_is_hit = rect.collidepoint(event.pos)
        elif event.type == MOUSEBUTTONUP:
            rect_is_moving = True
            rect_is_hit = False

    if rect_is_moving:
        rect.move_ip(v)

    if rect.left < 0:
        v[0] *= -1
    if rect.right > width:
        v[0] *= -1
    if rect.top < 0:
        v[1] *= -1
    if rect.bottom > height:
        v[1] *= -1
   
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if rect_is_hit:
        pygame.draw.rect(screen, BLUE, rect, 4)
    pygame.display.flip()

pygame.quit()
