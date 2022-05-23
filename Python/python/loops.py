# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])   

# Example of for loop

for i in range(0, 8):
    print(i)

# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])


for i,x in enumerate(['A','B','C']):
    print(i,x)

#While loop

squares = ['purple', 'purple', 'purple', 'purple']
NewSquare = []
i=0

while (squares[i] == 'purple'):
    NewSquare.append(squares[i])
    i += 1
