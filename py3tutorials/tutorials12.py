game = [[1,0,2],
       [1,2,0],
       [2,2,1],]

#Dealing with the diagonals
#1:Dealing with the other diagonal
diags = []
for col,row in enumerate(reversed(range(len(game)))):
#use enumerate when you are dealing with the indexes and 
#reversed is a built in function that returns the reverse
    diags.append(game[row][col])

#2:Dealing with the main diagonal
game_d = [[1,0,2],
       [1,1,0],
       [2,2,1],]

diags= []
for ix in range(len(game_d)):
    diags.append(game_d[ix][ix])
    

if(diags.count(diags[0])==len(diags)) and (diags[0]!=0):
#'''comparing the occurance of row[0] with the length of list
#so to find if the list has all identical element, and row[0]
#should not be 0''' 
        print('winner!')#Output:winner!