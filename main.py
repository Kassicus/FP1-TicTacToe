import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

pygame.init()

BLACK = pygame.Color(0, 0, 0, 255)
WHITE = pygame.Color(255, 255, 255, 255)

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("FP1 - TicTacToe")

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.delta_time = 0
        self.frame_limit = 120

    def start(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self):
        self.events = pygame.event.get()

        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        self.screen.fill(BLACK)

    def update(self):
        pygame.display.update()
        self.delta_time = self.clock.tick(self.frame_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()