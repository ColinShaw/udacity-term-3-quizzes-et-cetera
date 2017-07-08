# The map
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
        
# A map-based heuristic function
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

# Initialization
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

# The moves
delta = [[-1, 0 ],
         [ 0, -1],
         [ 1, 0 ],
         [ 0, 1 ]]

# Pictographs of moves
delta_name = ['^', 
              '<',
              'v', 
              '>']



def search(grid, init, goal, cost, heuristic):

    # Initialize closed cells
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    # Initialize expansion and action
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    # Intitial position
    x = init[0]
    y = init[1]

    # Cost and heuristic
    g = 0
    h = heuristic[x][y]
    f = g + h

    # Specific (intitial) open cell
    open = [[f, g, h, x, y]]

    # Control variables
    found = False  
    resign = False 
    count = 0
    
    # Main bool loop
    while not found and not resign:

        # If there are no open cells we haven't gotten to the end
        if len(open) == 0:
            return "Fail"

        else:
            # Sort, reverse and take first open element
            open.sort()
            open.reverse()
            next = open.pop()

            # Update variables
            x = next[3]
            y = next[4]
            g = next[1] 

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
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and closed[x2][y2] == 0 and grid[x2][y2] ==0:

                        # Update the cost with heuristic
                        g2 = g + cost 
                        h2 = heuristic[x2][y2]
                        f2 = g2 + h2

                        # Add new element to open cells, close current
                        open.append([f2, g2, h2, x2, y2])
                        closed[x2][y2] = 1

    return expand



e = search(grid, init, goal, cost, heuristic)
print(e)
