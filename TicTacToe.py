
class Player:
    def __init__(self, name, token, num):
        self.name = name
        self.token = token
        self.num = num

    def __repr__(self):
        return f'Player {self.num}\'s name is {self.name} and their token is {self.token}'

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

    
    name1 = input('What is Player 1\'s name?: ')
    token1 = 'X'
    name2 = input('What is Player 2\'s name?: ')
    token2 = 'O'



    player_1 = Player(name1, token1, '1')
    player_2 = Player(name2, token2, '2')
   
    print(player_1)
    print(player_2)
    
main()
    

