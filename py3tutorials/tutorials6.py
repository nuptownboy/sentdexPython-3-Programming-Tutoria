game = [[0,0,0],
       [0,0,0],
       [0,0,0],]


def game_board():
    print("   a  b  c")
    for count,row in enumerate(game):
        print(count,row)

x = game_board

game[0][1] = 1

x()#don't miss the parenthisis while calling the function

'''output:    a  b  c
           0 [0, 1, 0]
           1 [0, 0, 0]
           2 [0, 0, 0]'''


