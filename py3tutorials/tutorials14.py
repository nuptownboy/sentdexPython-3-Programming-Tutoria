import  itertools #module implements a number of iterator 

#horizontal winner
def win(current_game):#will check for the winner and the way they won


    def all_same(l):#will check if all elements in the list are same and not equal to 0
        if(l.count(l[0])==len(l)) and (l[0]!=0):
            return True
        else:
            return False



#Horizontal winner
    for row in game:
        print(row)
        if(all_same(row)):
           
            print(f'Player {row[0]} is the winner horizontally!')
            return True

#diagonal winner
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):

        diags.append(game[row][col])
    if(all_same(diags)):

         print(f'Player {diags[0]} is the winner diagonally(/)!')
         return True



    diags= []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    

    if(all_same(diags)):

            print(f'Player {diags[0]} is the winner diagonally(\\)!')
            return True
#vertical winner
    check=[]
    for col in range(len(game)):
        for row in game:
            check.append(row[col])#create a list of every column of game board

        if(all_same(check)):
 
            print(f'Player {check[0]} is the winner vertically(|)!')
            return True

    return False        
            
def game_board(game_map,player=0,row=0,column=0,just_display=False):

   try:
      if(game_map[row][column]!=0):#wont allow overwriting
        print("This position is occupado! Choose another!")
        return game_map, False
      print("   "+"  ".join([str(i) for i in range(len(game_map))]))
      if not just_display:
        game_map[row][column]=player
      for count,row in enumerate(game):
          print(count,row)
      return game_map,True   
   except IndexError as e:
      print("Error:make sure you input row/column as 0,1 or 2?",e)
      return game_map, False
   except Exception as e:
      print("Something went very wrong!",e)
      return game_map, False

play=True
player_choice=itertools.cycle([1,2])#iterator
while play:
    game_size=int(input("What size of tic tac toe ?"))
    game = [[0 for i in range(game_size)]for i in range(game_size)]#dynamic size of tic tac toe

    game_won = False
    game,_=game_board(game,just_display=True)
    while not game_won:
        current_player=next(player_choice)#will switch between the players
        print(f'current_player: {current_player}')
        played = False

        while not played:

            column_choice=int(input("What column do you want to play?(0,1,2): "))
            row_choice=int(input("What row do you want to play?(0,1,2): "))
            game,played=game_board(game,current_player,row_choice,column_choice)

        if win(game):
            game_won=True
            again=input("The game is over ,would you like to play again? (y/n) ")
            if(again.lower() == 'y'):
                print('restarting')
            elif(again.lower()=='n'):
                print('Byeeeeee')
                play=False
            else:
                print("Not a valid answer")
                play=False


