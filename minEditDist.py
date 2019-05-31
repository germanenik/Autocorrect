
#finds the minimum between three values
#attempting to replicate the ternary operator in C++
def minof3(a, b, c):
    min1 = (b, a)[a < b]
    return (c, min1)[min1 < c]
    
#calculates the minimum edit distance between a source and a target words.
#both deleting and inserting a letter each cost 1 point,
#substituting costs 2
#useful for autocorrect
def MED(source, target):
    #lengths
    lengthS, lengthT = len(source) + 1, len(target) + 1
    
    #initializing arrays
    grid = [[0 for col in range(lengthT)] for col in range(lengthS)]
    #anotherGrid = [[0] * lengthT] * lengthS
    #printList(grid)
    
    #set initials
    for i in range(1, lengthS):
        grid[i][0] = grid[i - 1][0] + 1
   
    for i in range(1, lengthT):
        grid[0][i] = grid[0][i - 1] + 1
  
    #printList(grid)
    minVal = 0
    #fill the list with values
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            a = grid[row - 1][col] + 1
            b = grid[row - 1][col - 1] + (2, 0)[source[row - 1] == target[col - 1]]
            c = grid[row][col - 1] + 1
            grid[row][col] = minof3(a, b, c)

            #midpt check
            if grid[lengthS // 2][lengthT // 2] > 3:
                return -1

            #printList(grid)
            #print()
    
    return grid[-1][-1]


#ask user for input
def askForInput(word_type):
    return input("Please enter a " + word_type + " word: ")

#prints out the graph with the source word on top and the target word
#on the left
def printList(l):
    for arr in l:
        for num in arr:
            print(num, end = ' ')
            
        print(end = '\n')
