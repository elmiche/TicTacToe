
class Player:
    def __init__(self, name, token, num):
        self.name = name
        self.token = token
        self.num = num

    def __repr__(self):
        return f'Player {self.num}\'s name is {self.name} and their token is {self.token}'

#needs move function
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
    
    def move(self, row, column, token):
        if self.board[row][column] != ' ':
            return False
        else:
            self.board[row][column] = token
            return True

    def is_full(self):
        full = True
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ' ':
                    full = False
                    return full
                else:
                    continue
        return full

game = Game()
print(game.is_full())


def main():
    game = Game()

    print(game)

    
    name1 = input('What is Player 1\'s name?: ')
    token1 = 'X'
    name2 = input('What is Player 2\'s name?: ')
    token2 = 'O'

    player_1 = Player(name1, token1, 1)
    player_2 = Player(name2, token2, 2)


    print(player_1)
    print(player_2)

#TODO print position on board
    x = int(input('enter x:'))
    y = int(input('enter y:'))
#replace with token
#
    valid_move = game.move(x, y, player_1.token) # think self.token at player_1.token
    if valid_move: 
        print(game)
    else:
        print('Invalid Move')






main()
    

