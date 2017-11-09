# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit test pass and your code meets all of the conditions.
#

import hamming.iteration
import hamming.brute_force
import hamming.streaming


def compute(value1, value2):

    # Brute force solve the problem.  Straight forward solution.
    #return brute_force.compute(value1, value2)

    # Use the built-ins to solve the problem.  Most pythonic solution.
    #return iteration.compute(value1, value2)

    # Use generators to solve the problem.  Low memory streaming solution.
    return streaming.compute(value1, value2)
