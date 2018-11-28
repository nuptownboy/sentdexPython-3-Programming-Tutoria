'''quiz

x = 1
def test():
    x = 2
test()
print(x)#Output:1,will print the global variable also both 'x' will have diff ids


x = 1
def test():
    global x
    x = 2
test()
print(x)#Output:2,will update the global variable inside the test() also both 'x' will have same id


x = [1]
def test():
    x = [2]
test()
print(x)#Output:[1],will print the global variable


x = [1]
def test():
    global x
    x = [2]
test()
print(x)#Output:[2],will update the global variable inside the test()


x = [1]
def test():
    x[0] = 2
test()
print(x)#Output:[2],will modify the global variable inside the test()'''
game = [[0,0,0],
       [0,0,0],
       [0,0,0],]


def game_board(game_map,player=0,row=0,column=0,just_display=False):
 #by introducing the game_map in params of the function and returning it,we are making sure that changes made to game_board is retained
    print("   a  b  c")
    if not just_display:
        game_map[row][column]=player
    for count,row in enumerate(game):
        print(count,row)

    return game_map    

game=game_board(game,just_display=True)
'''Output:    a  b  c
           0 [0, 0, 0]
           1 [0, 0, 0]
           2 [0, 0, 0]'''
game=game_board(game,player=1,row=2,column=1)
'''Output:    a  b  c
           0 [0, 0, 0]
           1 [0, 0, 0]
           2 [0, 1, 0]'''

