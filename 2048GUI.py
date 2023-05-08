import pygame
import random
import math
import sys

# Tile Images
IMAGENAME = "Assets/assets_2048.png"
TILE_SIZE = 100
HALF_TILE_SIZE = TILE_SIZE // 2
BORDER_SIZE = 45

# Other Images
# WIN = pygame.image.load('win.png')  # Replace with the local path to the win.png file
WIN = pygame.image.load("Assets/win.png")
WIN_WIDTH = 329
WIN_HEIGHT = 639

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Colors
BACKGROUND_COLOR = (188, 173, 161)
TEXT_COLOR = (51, 51, 26, 0.9)
BUTTON_COLOR = (115, 77, 38, 1)
BUTTON_TEXT_COLOR = (255, 255, 255, 0.9)
LOSE_OVERLAY_COLOR = (191, 191, 191, 0.5)

# Initialize Pygame
pygame.init()

class GUI:
    """
    Class to run game GUI.
    """

    def __init__(self, game):
        self._rows = game.get_grid_height()
        self._cols = game.get_grid_width()
        self.screen = pygame.display.set_mode(((self._cols * TILE_SIZE + 2 * BORDER_SIZE),
                                               (self._rows * TILE_SIZE + 2 * BORDER_SIZE)))
        pygame.display.set_caption('2048')
        self.clock = pygame.time.Clock()
        self._game = game
        self._tiles = pygame.image.load(IMAGENAME)
        self._directions = {pygame.K_UP: UP, pygame.K_DOWN: DOWN,
                            pygame.K_LEFT: LEFT, pygame.K_RIGHT: RIGHT}

        self.frame_width = (self._rows * TILE_SIZE) + HALF_TILE_SIZE + BORDER_SIZE
        self.frame_height = (self._cols * TILE_SIZE) + HALF_TILE_SIZE + BORDER_SIZE
        self.win = False
        self.lose = False
        self.font = pygame.font.Font(None, 50)

    def keydown(self, key):
        """
        Keydown handler
        """
        if not self.win:
            direction = self._directions.get(key)
            if direction:
                self._game.move(direction)
                self.win = self._game.win()
                self.lose = self._game.lose()

    def draw(self, surface):
        """
        Draw handler
        """
        surface.fill(BACKGROUND_COLOR)

        for row in range(self._rows):
            for col in range(self._cols):
                tile = self._game.get_tile(row, col)
                if tile == 0:
                    val = 0
                else:
                    val = int(math.log(tile, 2))
                source_rect = pygame.Rect(val * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)
                dest_rect = pygame.Rect(col * TILE_SIZE + BORDER_SIZE,
                                        row * TILE_SIZE + BORDER_SIZE,
                                        TILE_SIZE, TILE_SIZE)
                surface.blit(self._tiles, dest_rect, source_rect)

        if self.win:
            surface.blit(WIN, ((self.frame_width - WIN_WIDTH) // 2,
                               (self.frame_height - WIN_HEIGHT) // 2))

        if self.lose:
            lose_overlay = pygame.Surface((self.frame_width, self.frame_height),
                                          pygame.SRCALPHA, 32)
            lose_overlay.fill(LOSE_OVERLAY_COLOR)
            surface.blit(lose_overlay, (0, 0))
            lose_text = self.font.render("Game Over", True, TEXT_COLOR)
            lose_text_rect = lose_text.get_rect()
            lose_text_rect.center = (self.frame_width // 2, self.frame_height // 2)
            surface.blit(lose_text, lose_text_rect)

    def run(self):
        """
        Run the game loop.
        """
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.keydown(event.key)

            self.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    from ModelController2048 import TwentyFortyEight

    game = TwentyFortyEight(4, 4)  # You can set your desired grid size (height, width) here
    gui = GUI(game)
    gui.run()