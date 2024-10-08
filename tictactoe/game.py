import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # a list to 3 X 3 board
        self.c_winner = None  # keep track of the winner

    def print_board(self):
        # Corrected slicing to display rows correctly
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def winner(self, square, letter):
        r_ind = square // 3
        row = self.board[r_ind * 3 : (r_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in col):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False

    @staticmethod
    def numberboard():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def availablemoves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def number_of_empty_squares(self):
        return len(self.availablemoves())

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.c_winner = letter
            return True
        return False


def play(game, x_player, o_player, printgame=True):
    if printgame:
        game.numberboard()

    letter = "X"  # Starting letter

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if printgame:
                print(letter, f"makes a move to square {square}")
                game.print_board()
                print("")

            if game.c_winner:
                if printgame:
                    print(letter, "wins!!")
                return letter

            # Alternate letters
            letter = "O" if letter == "X" else "X"

            # Add a 2-second delay
            time.sleep(2)

    # Only print "It's a tie" if the loop ends without a winner
    if printgame:
        print("It's a tie.")

    return "Tie"


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, printgame=True)
