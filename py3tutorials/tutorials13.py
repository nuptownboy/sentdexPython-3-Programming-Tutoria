game = [[2,2,2],
       [1,2,0],
       [2,2,2],]

#horizontal
def win(current_game):
    for row in game:
        print(row)
        if(row.count(row[0])==len(row)) and (row[0]!=0):
#'''comparing the occurance of row[0] with the length of list
#so to find if the list has all identical element, and row[0]
#should not be 0'''            
            print(f'Player {row[0]} is the winner horizontally!')

#diagonal
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):
#use enumerate when you are dealing with the indexes and 
#reversed is a built in function that returns the reverse
        diags.append(game[row][col])
    if(diags.count(diags[0])==len(diags)) and (diags[0]!=0):

    #'''comparing the occurance of row[0] with the length of list
    #so to find if the list has all identical element, and row[0]
    #should not be 0''' 
         print(f'Player {diags[0]} is the winner diagonally(/)!')#Output:winner!



    diags= []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    

    if(diags.count(diags[0])==len(diags)) and (diags[0]!=0):
    #'''comparing the occurance of row[0] with the length of list
    #so to find if the list has all identical element, and row[0]
    #should not be 0''' 
            print(f'Player {diags[0]} is the winner diagonally(\\)!')#Output:winner!

    check=[]
    for col in range(len(game)):
        for row in game:
            check.append(row[col])#create a list of every column of game board

        if(check.count(row[0])==len(check)) and (check[0]!=0):
    #'''comparing the occurance of row[0] with the length of list
    #so to find if the list has all identical element, and row[0]
    #should not be 0''' 
            print(f'Player {check[0]} is the winner vertically(|)!')
            #Output:winner!
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

play=True
players=[1,2]
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0],]
    game_won = False
    game=game_board(game,just_display=True)
    while not game_won:
        current_player=1
        column_choice=input("What column do you want to play?(0,1,2): ")
        row_choice=input("What row do you want to play?(0,1,2): ")
        game=game_board(game,current_player,row_choice,column_choice)

# game=game_board(game,player=1,row=3,column=1)#Error:make sure you input row/column as 0,1 or 2? list index out of range
# game=game_board(game_board,player=1,row=3,column=1)#Something went very wrong! 'function' object is not subscriptable
