from typing import List

import pygame
from pygame.locals import *

SizeType = List[int]
PositionType = List[int]


class Square(pygame.sprite.Sprite):
    size: SizeType
    pos: PositionType
    speed: PositionType

    surf: pygame.Surface
    rect: Rect

    def __init__(self, size: SizeType = None, color: str = 'black', pos=None, speed=None):
        super(Square, self).__init__()

        if size is None:
            size = [25, 25]
        if speed is None:
            speed = [1, 2]
        if pos is None:
            pos = [0, 0]

        self.size = size
        self.color = color
        self.pos = pos
        self.speed = speed

        self.surf = pygame.Surface(size)
        self.surf.fill(Color(color))
        self.rect = self.surf.get_rect(topleft=pos)
        print(self.color, self.top, self.left)

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    def update(self, container: Rect):
        self.rect.move_ip(*self.speed)
        if self.left < container.left:
            # Bounce off left wall: move to the right (in pos x direction)
            self.speed[0] = abs(self.speed[0])
        elif self.right > container.right:
            # Bounce off right wall: move to the left (in neg x direction)
            self.speed[0] = -abs(self.speed[0])
        elif self.top < container.top:
            # Bounce off top wall: move to the bottom (in pos y direction)
            self.speed[1] = abs(self.speed[1])
        elif self.bottom > container.bottom:
            # Bounce off bottom wall: move to the top (in neg y direction)
            self.speed[1] = -abs(self.speed[1])

    def collide(self, square: 'Square'):
        collision = self.left < square.left < self.left + self.size[0] and \
                    self.top < square.top < self.top + self.size[1]
        if collision:
            square.speed[0] = -square.speed[0]
            square.speed[1] = -square.speed[1]
        return collision


class App:
    running: bool = True
    screen_size: SizeType = [800, 600]
    screen: pygame.Surface = None
    squares: List[Square] = []
    player: Square

    def __init__(self):
        pygame.init()
        App.screen = pygame.display.set_mode(self.screen_size, RESIZABLE)
        App.squares = [
            Square(color='black', pos=[0, 0]),
            Square(color='red', pos=[800, 0]),
            Square(color='green', pos=[0, 600]),
            Square(color='blue', pos=[800, 600]),
        ]
        App.player = Square(color='orange', pos=[400, 300])

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == MOUSEMOTION:
                    App.player.pos = event.pos

            App.screen.fill(Color('white'))

            for square in self.squares:
                square.update(App.screen.get_rect())
                App.screen.blit(square.surf, square.rect)
            App.screen.blit(App.player.surf, App.player.pos)
            collided_square = next((square for square in App.squares if App.player.collide(square)), None)
            if collided_square:
                msg = f'The {collided_square.color} square hit you'
                print(msg)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    App().run()
