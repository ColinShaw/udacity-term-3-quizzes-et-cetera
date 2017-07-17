import numpy as np
from numpy.linalg import inv

def JMT(start, end, T):
    # The first three coefficients easily come from derivatives of s(t) evaluated at t=0
    o1 = start[0]
    o2 = start[1]
    o3 = start[2] / 2

    # Setting t=T in these derivatives gives us (including corrected b[1] equation)
    A = [ [T**3,           T**4,       T**5],
          [3 * T**2,   4 * T**3,   5 * T**4],
          [6 * T,     12 * T**2,  20 * T**3] ]
    b = [ end[0] - (start[0] + start[1] * T + 0.5 * start[2] * T**2),
          end[1] - (start[1] + start[2] * T),
          end[2] - start[2] ]
    
    # Make numpy arrays out of these so we get easy arithmetic
    A = np.array(A)
    b = np.array(b)

    # Compute x in Ax=b as defined above
    x = inv(A).dot(b)

    # Define the last three coefficients
    o4 = x[0]
    o5 = x[1]
    o6 = x[2]

    # Return the coefficient array
    out = [o1, o2, o3, o4, o5, o6]
    print(out)
    return out
