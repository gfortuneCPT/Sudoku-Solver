#test function
def check (y,x,n):
    #check rows for same number (n)
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    #check colum for same number (n)
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    #Check Cell for same number (n)
    cellx = (x//3)*3
    celly = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[celly+i][cellx+j] == n:
                return False
    #return true if pass row,col,cell check
    return True

#Display function
def printgrid(grid):
    gridline = "|----------+----------+----------|"
    bordline = "----------------------------------"
    print(bordline)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(gridline)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(bordline)

#Bactrack Implementation
def solve ():
        for y in range(9):
            for x in range(9):
                    if grid[y][x] == 0:
                        for n in range(1,10):
                            if check(y,x,n):
                                grid[y][x] = n
                                solve()
                                grid[y][x] = 0
                        return
        printgrid(grid)
#row by row grid
row = 9
grid = []

for block in range(row):
    grid.append([int(n) for n in input("Enter Row "+str(block)+": ").split( )])

printgrid(grid)
solve()
input("Exit?")