# The moves
forward = [[-1,  0], 
           [ 0, -1],
           [ 1,  0], 
           [ 0,  1]] 

# Move names
forward_name = ['up', 'left', 'down', 'right']

# Move change actions (cyclic on the moves)
action = [-1, 0, 1]

# Names of the move actions
action_name = ['R', '#', 'L']

# The map
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

# Intialization
init = [4, 3, 0]  # [row, col, direction]
goal = [2, 0]     # [row, col]
cost = [2, 1, 20] # [R, #, L]



def optimum_policy2D(grid, init, goal, cost):

    # Initialzie value and policy    
    value  = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for x in range(4)]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))] for x in range(4)]
    
    # Initialize final policy map
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    # Control variable
    change = True

    # Main bool loop
    while change:

        change = False
  
        # Double loop over grid coordinates
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                # Loop over possible moves
                for orientation in range(4):

                    # Check if we have met the goal and value is legitimate
                    if goal[0] == x and goal[1] == y and value[orientation][x][y] > 0:

                        # Update the orientation and policy maps
                        value[orientation][x][y] = 0
                        policy[orientation][x][y] = '*'
                        change = True
   
                    # Check if we are on a valid map cell 
                    elif grid[x][y] == 0:

                        # Go through the three possible changes to the orientation (moves)
                        for i in range(3):

                            # Update orientation and position
                            o2 = (orientation + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                        
                            # Check if we are on the map
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                        
                                # Update the value based on new value and cost of move
                                v2 = value[o2][x2][y2] + cost[i]
    
                                # If the new value is less than the old value
                                if v2 < value[orientation][x][y]:

                                    # Update the old value and policy
                                    change = True
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[i]
    
    # Set initial position and orientation 
    x = init[0]
    y = init[1]
    orientation = init[2]
    
    # Generate first output map point
    policy2D[x][y] = policy[orientation][x][y]
    
    # Main bool loop generating output map
    while policy[orientation][x][y] != '*':

        # If we moved forward
        if policy[orientation][x][y] == '#':
            o2 = orientation

        # If we turned right
        if policy[orientation][x][y] == 'R':
            o2 = (orientation - 1) % 4

        # If we turned left
        if policy[orientation][x][y] == 'L':
            o2 = (orientation + 1) % 4

        # Update position and orientation
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2

        # Set resulting map
        policy2D[x][y] = policy[orientation][x][y]
    
    return policy2D



op = optimum_policy2D(grid, init, goal, cost)
for i in range(len(op)):
    print(op[i])
    
