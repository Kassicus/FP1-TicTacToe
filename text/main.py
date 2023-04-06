class Game():
    def __init__(self):
        self.current_player = "X"

        self.running = True

        self.commands = {
                "exit": self.terminate,
                }

    def main_menu(self):
        while self.running:
            c = str(input(">> "))

            if c in self.commands:
                self.commands[c]()
            else:
                print("Invalid Command...")

    def terminate(self):
        self.running = False

    def toggle_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"

if __name__ == '__main__':
    game = Game()
    game.main_menu()
