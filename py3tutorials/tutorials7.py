'''def addition(x,y):
    return x+y

a=addition(5,3)
print(a)#Output:8
b=addition('hey ','there')
print(b)#Output:hey there
#c=addition(5,'hey')#error as they are of different type'''


game = [[0,0,0],
       [0,0,0],
       [0,0,0],]


def game_board(player=0,row=0,column=0,just_display=False):
    print("   a  b  c")
    if not just_display:
    	game[row][column]=player
    for count,row in enumerate(game):
        print(count,row)

game_board(just_display=True)
'''Output:    a  b  c
		   0 [0, 0, 0]
		   1 [0, 0, 0]
		   2 [0, 0, 0]'''
game_board(player=1,row=2,column=1)
'''Output:      a  b  c
			 0 [0, 0, 0]
			 1 [0, 0, 0]
			 2 [0, 1, 0]'''