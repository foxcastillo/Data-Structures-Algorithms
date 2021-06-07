# Edgar Castillo / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Castillo

# Recursive vs Iterative solutions

#Recursive Solution
def powerofTwo(n):
    if n == 0:
        return 1
    else:
        power = powerofTwo(n-1)
        return power * 2
# Warning: system crash.

#Iterative Solution
def powerofTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
# Could consume PC cycle due to infinite.

# Iteration is very space and time efficient but no easy to code.
# Recursion is not space and time effient but it's easy to code. 

# When to use it Recursion?
# it's a simple solution to implement in a problem.
# When tranversing a tree 

# When to avoid Recursion?
# space and time complexity are very important.
# Recursion uses more memory than Iteration.
# Recursion may be slow.
