class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        for i in range(3):
            print(" | ".join(self.board[i]))
            if i < 2:
                print("--+---+--")
        print()

    def make_move(self, row, col):
        if self.board[row][col] != " ":
            print("Posição ocupada. Tente outra.")
            return False
        self.board[row][col] = self.current_player
        return True

    def check_winner(self):
        b = self.board
        lines = (
            b,                          # linhas
            zip(*b),                    # colunas
            [[b[i][i] for i in range(3)]],        # diagonal principal
            [[b[i][2 - i] for i in range(3)]]     # diagonal secundária
        )
        for group in lines:
            for line in group:
                if all(cell == self.current_player for cell in line):
                    return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Jogo da Velha!\nJogador X começa.")
        while True:
            self.print_board()
            try:
                move = input(f"Jogador {self.current_player}, informe linha e coluna (0-2) separadas por espaço: ")
                row, col = map(int, move.strip().split())
                if row not in range(3) or col not in range(3):
                    print("Coordenadas inválidas. Use valores de 0 a 2.")
                    continue
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue

            if not self.make_move(row, col):
                continue

            if self.check_winner():
                self.print_board()
                print(f"Jogador {self.current_player} venceu!")
                break

            if self.is_full():
                self.print_board()
                print("Empate!")
                break

            self.switch_player()


if __name__ == "__main__":
    jogo = TicTacToe()
    jogo.play()