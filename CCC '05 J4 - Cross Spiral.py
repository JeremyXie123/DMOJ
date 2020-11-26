# initial conditions
room_width, room_height, cut_width, cut_height, max_steps =  [int(input()) for i in range(5)]

# generation of intial square
grid = [[0 for i in range(room_width)] for j in range(room_height)]

# addition of cutouts
for row in range (0,cut_height):
    for column in range(0,cut_width):
        grid[row][column] = 1
        grid[room_height-1-row][column] = 1
        grid[row][room_width-1-column] = 1
        grid[room_height-1-row][room_width-1-column] = 1

def printGrid():
    for row in grid:
        print(row)

# function for determining path
def safe_get(grid, row, col):
  try:
    return grid[row][col]
  except IndexError:
    return 1

def getDirX(grid,row,col):
    right = safe_get(grid,row+1,col)
    left = safe_get(grid,row-1,col)
    return left-right

def getDirY(grid,row,col):
    up = safe_get(grid,row,col+1)
    down = safe_get(grid,row,col-1)
    return up-down

# simulation

# intial pos is the cutout width to the right of 1,1 (zero based)
pos_x = cut_width
pos_y = 0

#grid[pos_x][pos_y]=1
#printGrid()

# initial direction is straight right
dir_x = 1
dir_y = 0


for i in range(max_steps):
    grid[pos_y][pos_x] = 1

    pos_x += dir_x
    pos_y += pos_y

    dir_x = getDirX(grid,pos_y,pos_x)
    dir_y = getDirY(grid,pos_y,pos_x)

    print("Iter: "+str(i+1))
    printGrid()
# results
print(pos_x + 1, pos_y + 1)

print("")
#printGrid()