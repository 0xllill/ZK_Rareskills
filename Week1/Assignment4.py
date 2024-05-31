from sympy import randprime
from random import randint
from sympy.ntheory import discrete_log

# Define the public parameters
n = 3089
g = 5

# Let's assume we have the solution (x, y) to the given system of equations
#x = 420  # Example solution
#y = 888   # Example solution

# :( better to ask for g^(2x+8y) input but difficult to enter such a big number
print('Enter first commit x:') 
input1 = int(input())


# :( better to ask for g^(2x+8y) input but difficult to enter such a big number
print('Enter second commit y:')
input2 = int(input())


left_side_1 = pow(g, int(2 * input1 + 8 * input2), n)
left_side_2 = pow(g, int(5 * input1 + 3 * input2), n)




###### VERIFIER SIDE
# Homomorphic proof
# 2x + 8y = 7944
right_side_1 = pow(g, 7944, n)
# 5x + 3y = 4764
right_side_2 = pow(g, 4764, n)

# Verifier checks 
print(f"Verify first equation: {left_side_1 == right_side_1}")
print(f"Verify second equation: {left_side_2 == right_side_2}")



