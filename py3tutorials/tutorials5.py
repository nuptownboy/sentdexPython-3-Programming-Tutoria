''' Slicing
l = [1,2,3,4,5]


print(l[-1])#Output:5
print(l[2:])#Output:[3, 4, 5]
l[1]=99
print(l)#Output:[1, 99, 3, 4, 5]'''

game = [[0,0,0],
       [0,0,0],
       [0,0,0],]


game[0][1] = 1
print("   a  b  c")
for count,row in enumerate(game):
    print(count,row)
    '''Output:    a  b  c
			   0 [0, 1, 0]
			   1 [0, 0, 0]
			   2 [0, 0, 0]'''
