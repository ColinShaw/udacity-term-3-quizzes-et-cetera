from math import pi, sqrt, sin, cos, tan, floor
from matplotlib import pyplot as plt

NUM_THETA_CELLS = 90
SPEED = 1.45
LENGTH = 0.5


def decreasing_range(start, length):
    return [start + x for x in range(length)][::-1]

def generate_heuristic(length):
    return [decreasing_range(x, length) for x in range(length)][::-1]

heuristic = generate_heuristic(16)

def theta_to_stack_number(theta):
    new_theta    = (theta + 2 * pi) % (2 * pi)
    stack_number = int(round(new_theta * NUM_THETA_CELLS / (2*pi))) % NUM_THETA_CELLS
    return stack_number

def idx(float_num):
    return int(floor(float_num))

def search(grid, start, goal):
    closed      = [[[0 for row in range(len(grid[0]))] for col in range(len(grid))] for stack in range(NUM_THETA_CELLS)]
    came_from   = [[[0 for row in range(len(grid[0]))] for col in range(len(grid))] for stack in range(NUM_THETA_CELLS)]
    x, y, theta = start
    stack       = theta_to_stack_number(theta)
    g           = 0
    h           = heuristic[idx(x)][idx(y)]
    f           = g + h
    closed[stack][idx(x)][idx(y)]    = (f, g, h, x, y, theta)
    came_from[stack][idx(x)][idx(y)] = (f, g, h, x, y, theta)
    total_closed  = 1
    opened       = [(f, g, h, x, y, theta)]
    while len(opened) > 0:
        opened.sort(reverse=True)
        next                 = opened.pop()
        f, g, h, x, y, theta = next
        test                 = (idx(x), idx(y))
        if (idx(x),idx(y)) == goal:
            print("\n###############\nfound path to goal in {} expansions\n".format(total_closed))
            final = (f, g, h, x, y, theta)
            return closed, came_from, final
        for next_state in expand(next):
            f2, g2, h2, x2, y2, theta2 = next_state
            if x2 < 0 or x2 >= len(grid) or y2 < 0 or y2 >= len(grid[0]):
                continue
            stack2 = theta_to_stack_number(theta2)
            if closed[stack2][idx(x2)][idx(y2)] == 0 and grid[idx(x2)][idx(y2)] == 0:
                opened.append((f2, g2, h2, x2, y2, theta2))
                closed[stack2][idx(x2)][idx(y2)]     = next_state
                came_from[stack2][idx(x2)][idx(y2)]  = next
                total_closed                        += 1
    print("no valid path.")
    final = (f, g, h, x, y, theta)
    return closed, came_from, final

def reconstruct_path(came_from, goal, start, final):
    path                 = [(final)]
    f, g, h, x, y, theta = final
    stack                = theta_to_stack_number(theta)
    current              = came_from[stack][idx(x)][idx(y)]
    f, g, h, x, y, theta = current
    stack                = theta_to_stack_number(theta)
    while (x,y) != (start[0], start[1]):
        path.append(current)
        current              = came_from[stack][idx(x)][idx(y)]
        f, g, h, x, y, theta = current
        stack                = theta_to_stack_number(theta)
    return path

def expand(state):
    f, g, h, x, y, theta = state
    g2          = g + 1	
    h2          = heuristic[idx(x)][idx(y)]
    f2          = g2 + h2
    next_states = []
    for delta in range(-35, 40, 5):
        delta  = pi / 180.0 * delta
        omega  = SPEED / LENGTH * tan(delta)
        theta2 = theta + omega
        x2     = x + SPEED * cos(theta2)
        y2     = y + SPEED * sin(theta2)
        next_states.append((f2, g2, h2, x2, y2, theta2))
    return next_states

def show_path(path, start, goal):
    path.reverse()
    X     = [p[1] for p in path]
    Y     = [p[2] for p in path]
    THETA = [p[3] for p in path]
    plt.scatter(X,Y, color='black')
    plt.scatter([start[0]], [start[1]], color='blue')
    plt.scatter([goal[0]], [goal[1]], color='red')
    plt.show()
