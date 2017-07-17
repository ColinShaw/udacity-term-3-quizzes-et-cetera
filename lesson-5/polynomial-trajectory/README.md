# Polynomial Trajectory

Goal is to look at the weights of the various cost functions and adjust to accomplish the task.  The cost functions are all defined in `cost_functions.py`, which 
is very interesting to see what the form of the various cost functions are.  `ptg.py` had to be fixed for python 3 for printing the name of the function in
verbose mode.



### Fixing the Problem(s)
There are 5 files in the provided code. You'll probably want to start by modifying cost function weights in ptg.py but may also want to add cost functions of your own.

### File Descriptions

 *  ptg.py - The primary code for generating a polynomial trajectory for some constraints. This is also where weights are assigned to cost functions. Adjusting these weights (and possibly adding new cost functions), can have a big effect on vehicle behavior.

 * cost_functions.py - This file contains many cost functions which are used in ptg.py when selecting the best trajectory. Some cost functions aren't yet implemented...

 * evaluate_ptg.py - This file sets a start state, goal, and traffic conditions and runs the PTG code. Feel free to modify the goal, add traffic, etc... to test your vehicle's trajectory generation ability.

 * constants.py - constants like speed limit, vehicle size, etc...

 * helpers.py - helper functions used by other files.
