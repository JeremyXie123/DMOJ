N, H = [int(i) for i in input().split()]

height_map = [[None for i in range (N)] for j in range(N)]

for i in range(N):
    array = [int(i) for i in input().split()]
    height_map[i] = array

init_pos = (0, 0)
end_pos = (N-1, N-1)

from queue import Queue
q = Queue()
q.put(init_pos)
v = set([init_pos])

def get_viable(grid, pos):
    viable = []
    max_X, max_Y = N, N
    
    cur_X = pos[0]
    cur_Y = pos[1]

    cur_height = grid[cur_X][cur_Y]

    if cur_X + 1 < max_X:
        right = grid[cur_X+1][cur_Y]
        if abs(right-cur_height)<=H:
            viable.append((cur_X+1,cur_Y))
    if cur_Y + 1 < max_Y:
        down = grid[cur_X][cur_Y+1]
        if abs(down-cur_height)<=H:
            viable.append((cur_X,cur_Y+1))
    return viable

found = False
while not q.empty():
    cur_coord = q.get()
    if cur_coord == end_pos:
        found = True
        break

    for coord in get_viable(height_map,cur_coord):
        if coord not in v:
            q.put(coord) 
            v.add(coord) 

if found:
    print("yes")
else:
    print("no")