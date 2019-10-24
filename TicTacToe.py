
class Player:
	def __init__(self, name, token):
		self.name = name
		self.token = token 

print()

		




class Game:
    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    def __repr__(self):
        board = ''
        for i in range(3):
            row = ''
            for j in range(3):
                row += f" {self.board[i][j]} "
                if j < 2:
                    row += "|"
            board += f"{row}\n"

        return board

def main():
    board = Game()

    print(board)

main()

