game = [[1,1,1],
       [0,2,0],
       [2,2,0],]

#handling horizontal winner
def win(current_game):
    for row in game:
        print(row)
        if(row.count(row[0])==len(row)) and (row[0]!=0):
#'''comparing the occurance of row[0] with the length of list
#so to find if the list has all identical element, and row[0]
#should not be 0'''            
            print('winner!')


win(game)
'''Output:[1, 1, 1]
           winner!
          [0, 2, 0]
          [2, 2, 0]'''
