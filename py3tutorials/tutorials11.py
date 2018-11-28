game = [[2,0,1],
       [2,0,0],
       [2,2,0],]
check = []

#handling vertical winner

for col in range(len(game)):
    for row in game:
        check.append(row[col])#create a list of every column of game board

    if(check.count(row[0])==len(check)) and (check[0]!=0):
#'''comparing the occurance of row[0] with the length of list
#so to find if the list has all identical element, and row[0]
#should not be 0''' 
        print('winner!')#Output:winner!

    
