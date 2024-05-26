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
print('Enter first commit 2x+8y:') 
input1 = input()
left_side_1 = pow(g, int(input1), n)

# :( better to ask for g^(2x+8y) input but difficult to enter such a big number
print('Enter second commit 5x+3y:')
input2 = input()
left_side_2 = pow(g, int(input2), n)

# Homomorphic proof
# 2x + 8y = 7944
right_side_1 = pow(g, 7944, n)
# 5x + 3y = 4764
right_side_2 = pow(g, 4764, n)

# Verifier checks
print(f"Verify first equation: {left_side_1 == right_side_1}")
print(f"Verify second equation: {left_side_2 == right_side_2}")

# For demonstration, the verifier can check that discrete logs match
x_discrete_log = discrete_log(n, left_side_1, g)
y_discrete_log = discrete_log(n, left_side_2, g)

print(f"Discrete log of C_x: {x_discrete_log == input1}")
print(f"Discrete log of C_y: {y_discrete_log == input2}")