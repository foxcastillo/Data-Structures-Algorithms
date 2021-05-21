
# The Blueprint for recursion
"""
def recursionMethod(parameters):
    if exit from condition satisfied:
        return some Value
    else:
        recursionMethod(modified parameters)
"""
# How the Recursion works

def firstMethod(): # First then second 
    secondMethod()
    print("I am the first Method") # Print 1st method
    
def secondMethod(): # Second then third
    thirdMethod()
    print("I am the second Method") # Print 2nd method

def thirdMethod(): # Third then fourth
    fourthMethod()
    print("I am the third Method") # Print 3rd method
    
def fourthMethod(): # Finally last
    print("I am the fourth Method") # end of the algorithm

# Example
def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
        
# Visual of Example^

# recursiveMethod(4) > recursiveMethod(3) then,
# recursiveMethod(3) > recursiveMethod(2) then,
# recursiveMethod(2) > recursiveMethod(1) then,
# recurisveMethod(1) > recursiveMethod(0) 
# then, go in reverse till recursiveMethod(4).
