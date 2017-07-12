grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

moves = [[-1, 0], 
         [ 0,-1],
         [ 1, 0],
         [ 0, 1]]

init = [0, 0]
goal = [4, 5]


has_checked_map = [[0 for col in len(grid[0])] for row in len(grid)]



has_found_goal = False



while has_found_goal == False:

	for col in range(len(grid[0])):
		for row in range(len(grid)):

				


