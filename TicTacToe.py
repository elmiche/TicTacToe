
class Player:
	def __init__(self, name, token):
		self.name = name
		self.token = token 

print()

		




class Game:
    def __init__(self):
        self.board = [['X','X','X'],['X','X','X'],['X','X','X']]
    
    def __repr__(self):
        for i in range(3):
            for j in range(3):
                print(f"{i}, {j}")

def main():
    board = Game()

    print(board)

main()

