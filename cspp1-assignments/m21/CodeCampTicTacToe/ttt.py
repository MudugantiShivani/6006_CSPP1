'''
    finding who's is the winner
'''
def tictactoe(game):
    '''
    checking the possibilities
    '''
    flag = 0
    count = 0
    if (game[0][0] == game[1][0] == game[2][0] == "x"
            or game[0][1] == game[1][1] == game[2][1] == "x"
            or game[0][2] == game[1][2] == game[2][2] == "x"
            or game[0][0] == game[0][1] == game[0][2] == "x"
            or game[1][0] == game[1][1] == game[1][2] == "x"
            or game[2][0] == game[2][1] == game[2][2] == "x"
            or game[0][0] == game[1][1] == game[2][2] == "x"
            or game[0][2] == game[1][1] == game[2][0] == "x"):
        flag = 1
        count += 1
    if (game[0][0] == game[1][0] == game[2][0] == "o"
            or game[0][1] == game[1][1] == game[2][1] == "o"
            or game[0][2] == game[1][2] == game[2][2] == "o"
            or game[0][0] == game[0][1] == game[0][2] == "o"
            or game[1][0] == game[1][1] == game[1][2] == "o"
            or game[2][0] == game[2][1] == game[2][2] == "o"
            or game[0][0] == game[1][1] == game[2][2] == "o"
            or game[0][2] == game[1][1] == game[2][0] == "o"):
        flag = 2
        count += 1
    if count == 2:
        return 'invalid game'
    if flag == 1:
        return 'x'
    if flag == 2:
        return 'o'
    return 'draw'
def main():
    '''
    giving input to a program
    '''
    game = []
    flag = 0
    count_of_of_x = 0
    count_of_o = 0
    for i in range(3):
        game.append(input().split())
    for i in range(3):
        for j in range(3):
            if game[i][j] == "x" or game[i][j] == "o" or game[i][j] == ".":
                flag = 1
            else:
                flag = 0
            if game[i][j] == "x":
                count_of_of_x += 1
            elif game[i][j] == "o":
                count_of_o += 1
    if flag == 0:
        print("invalid input")
    elif count_of_of_x > 5 or count_of_o > 5:
        print("invalid game")
    else:
        print(tictactoe(game))
if __name__ == '__main__':
    main()
    