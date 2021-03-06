from typing import Iterable

import pygame
from pygame.locals import *


class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        App.screen.blit(self.img, self.rect)


class App:
    """Create a single-window app with multiple scenes."""

    screen: pygame.Surface
    t: Text
    scenes: Iterable['Scene']
    shortcuts = {
        (K_x, KMOD_LMETA): 'print("cmd+X")',
        (K_x, KMOD_LALT): 'print("alt+X")',
        (K_x, KMOD_LCTRL): 'print("ctrl+X")',
        (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
        (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
        (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        (K_f, KMOD_LMETA): 'self.toggle_fullscreen()',
        (K_r, KMOD_LMETA): 'self.toggle_resizable()',
        (K_g, KMOD_LMETA): 'self.toggle_frame()',
    }

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 240)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.scenes = []
        App.t = Text('Pygame App', pos=(20, 20))
        App.running = True

    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == KEYDOWN:
                    self.do_shortcut(event)

            App.screen.fill(Color('gray'))
            App.t.draw()
            pygame.display.update()

        pygame.quit()

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)


if __name__ == '__main__':
    App().run()
