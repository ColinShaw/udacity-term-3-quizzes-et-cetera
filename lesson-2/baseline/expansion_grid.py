# The map
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

# Initialization
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

# The moves
delta = [[-1, 0], 
         [ 0,-1], 
         [ 1, 0], 
         [ 0, 1]] 

# Pictographs of the moves
delta_name = ['^', 
              '<', 
              'v', 
              '>']



def search(grid, init, goal, cost):

    # Initialize closed cells
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    # Initialize expansion
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    # Initialize position and cost
    x = init[0]
    y = init[1]
    g = 0

    # Specific (initial) open cell
    open = [[g, x, y]]

    # Control variables
    found = False 
    resign = False 
    count = 0

    # Main bool loop
    while not found and not resign:

        # Done if there are no more open cells
        if len(open) == 0:
            resign = True
  
        else:
            # Sort, reverse and take first open element
            open.sort()
            open.reverse()
            next = open.pop()

            # Update variables
            x = next[1]
            y = next[2]
            g = next[0]

            # Update expansion counter
            expand[x][y] = count
            count += 1
           
            # Trigger end of loop if we met the goal 
            if x == goal[0] and y == goal[1]:
                found = True

            else:
                # Go through the possible moves
                for i in range(len(delta)):

                    # Compute new position
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    # See if the new position is valid
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and closed[x2][y2] == 0 and grid[x2][y2] == 0:
 
                            # Update the cost
                            g2 = g + cost

                            # Add new element to open cells, close current
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    return expand



e = search(grid, init, goal, cost)
print(e)

