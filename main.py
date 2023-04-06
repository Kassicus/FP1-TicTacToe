import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

pygame.init()

BLACK = pygame.Color(0, 0, 0, 255)
GRAY = pygame.Color(80, 80, 80, 255)
WHITE = pygame.Color(255, 255, 255, 255)
BLUE = pygame.Color(0, 0, 255, 255)

class Grid(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(200, 200)

        self.player = ""
        self.font = pygame.font.SysFont("Courier", 96)
        self.player_surf = self.font.render(self.player, True, WHITE)

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw_player(self, surface: pygame.Surface):
        surface.blit(self.player_surf, (
            self.pos.x + (self.size.x / 2) - (self.player_surf.get_width() / 2), self.pos.y + (self.size.y / 2) - (self.player_surf.get_height() / 2)
        ))

    def update(self):
        if self.check_hovered():
            self.image.fill(BLUE)
        else:
            self.image.fill(WHITE)

        if self.check_hovered():
            if self.check_clicked():
                self.update_player()

    def check_hovered(self) -> bool:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.pos.x < mouse_x < self.pos.x + self.size.x:
            if self.pos.y < mouse_y < self.pos.y + self.size.y:
                return True
            else:
                return False
        else:
            return False

    def check_clicked(self) -> bool:
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
            else:
                return False

    def update_player(self):
        self.player = game.current_player
        self.player_surf = self.font.render(self.player, True, BLACK)
        game.toggle_player()


class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = pygame.math.Vector2(50, 50)
        self.size = pygame.math.Vector2(600, 600)

        self.grid_group = pygame.sprite.Group()
        self.x_group = pygame.sprite.Group()
        self.o_group = pygame.sprite.Group()

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.create_grids()

    def draw_groups(self, surface: pygame.Surface):
        self.grid_group.draw(surface)
        for grid in self.grid_group:
            grid.draw_player(surface)

    def update(self, surface: pygame.Surface):
        self.grid_group.update()
        self.x_group.update()
        self.o_group.update()

        self.draw_groups(surface)

    def create_grids(self):
        for y in range(3):
            for x in range(3):
                g = Grid(int(x * 200) + 50, int(y * 200) + 50)
                self.grid_group.add(g)

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("FP1 - TicTacToe")

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.delta_time = 0
        self.frame_limit = 120

        self.current_player = "X"
        self.font = pygame.font.SysFont("Courier", 24)

        self.current_string = str("Current Player: " + self.current_player)
        self.current_surf = self.font.render(self.current_string, True, WHITE)

        self.board = Board()

        self.draw_group = pygame.sprite.Group()
        self.draw_group.add(self.board)

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

    def toggle_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"

        self.current_string = str("Current Player: " + self.current_player)
        self.current_surf = self.font.render(self.current_string, True, WHITE)

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_group.draw(self.screen)
        self.screen.blit(self.current_surf, (700, 50))

    def update(self):
        self.draw_group.update(self.screen)

        pygame.display.update()
        self.delta_time = self.clock.tick(self.frame_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()
