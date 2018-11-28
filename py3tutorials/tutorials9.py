game = [[0,0,0],
       [0,0,0],
       [0,0,0],]


def game_board(game_map,player=0,row=0,column=0,just_display=False):

   try:
      print("   a  b  c")
      if not just_display:
      	game_map[row][column]=player
      for count,row in enumerate(game):
          print(count,row)
      return game_map   
   except IndexError as e:
      print("Error:make sure you input row/column as 0,1 or 2?",e)
      
   except Exception as e:
      print("Something went very wrong!",e)


game=game_board(game,just_display=True)
'''Output:   a  b  c
           0 [0, 0, 0]
           1 [0, 0, 0]
           2 [0, 0, 0]'''
game=game_board(game,player=1,row=3,column=1)#Error:make sure you input row/column as 0,1 or 2? list index out of range
game=game_board(game_board,player=1,row=3,column=1)#Something went very wrong! 'function' object is not subscriptable
