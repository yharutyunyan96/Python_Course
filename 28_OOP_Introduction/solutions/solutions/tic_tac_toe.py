class Cell:
    def __init__(self, number):
        self.is_occupied = False
        self.number = number
        self.symbol = " "

    def occupy(self, symbol):
        if not self.is_occupied:
            self.is_occupied = True
            self.symbol = symbol
            return True
        return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def change_cell_state(self, cell_number, symbol):
        if 1 <= cell_number <= 9:
            return self.cells[cell_number - 1].occupy(symbol)
        return False

    def check_game_end(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]

        for combo in winning_combinations:
            if self.cells[combo[0]].symbol == self.cells[combo[1]].symbol == self.cells[combo[2]].symbol != " ":
                return True
        return False

    def is_full(self):
        return all(cell.is_occupied for cell in self.cells)

    def display(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol}")
            if i < 6:
                print("--+---+--")


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_a_move(self):
        while True:
            try:
                cell_number = int(input(f"{self.name}, choose a cell (1-9): "))
                if 1 <= cell_number <= 9:
                    return cell_number
                else:
                    print("Invalid cell number. Please choose a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def start_turn(self, player):
        self.board.display()
        cell_number = player.make_a_move()
        if self.board.change_cell_state(cell_number, player.symbol):
            if self.board.check_game_end():
                player.wins += 1
                print(f"{player.name} wins!")
                return True
            if self.board.is_full():
                print("The game is a draw.")
                return True
        else:
            print("Cell is already occupied. Try another one.")
        return False

    def start_game(self):
        self.board = Board()
        current_player = 0
        while True:
            if self.start_turn(self.players[current_player]):
                break
            current_player = 1 - current_player  # Switch player
        self.board.display()

    def main_game_loop(self):
        while True:
            self.start_game()
            print(f"Scores: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            if input("Play again? (y/n): ").lower() != 'y':
                break


# Creating players and starting the game
player1 = Player("Gor", "X")
player2 = Player("Anna", "O")
game = Game(player1, player2)
game.main_game_loop()