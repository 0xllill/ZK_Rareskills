import numpy as np
import random
from scipy.interpolate import lagrange
from numpy.typing import NDArray
from numpy import poly1d
from numpy.polynomial.polynomial import Polynomial


# Convert the following R1CS into a QAP over real numbers, not a finite field

# Define the matrices
A = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

B = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

C = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [-3,1,1,2,0,-1]])

# pick values for x and y
x = 100
y = 100

# this is our original formula
# out = 3yx^2 + 5xy - x - 2xy + 3
out = 3 * x * x * y + 5 * x * y - x- 2*y + 3# the witness vector with the intermediate variables inside
v1 = 3*x*x
v2 = v1 * y
w = np.array([1, out, x, y, v1, v2])

result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
assert result.all(), "result contains an inequality"

# You can use a computer (Python, sage, etc) to check your work at each step and do the Lagrange interpolate,
# but you must show each step.
#
# **Be sure to check the polynomials manually because you will get precision loss when interpolating over
# floats/real numbers.**
#
# Check your work by seeing that the polynomial on both sides of the equation is the same.

# Aw*Bw = Cw


# let's turn each matrix into polynomials!
def vectorsToPolynomials(m, witness):
    polys = []
    
    # Arbitrary
    xs = np.array([1, 2, 3])

    # For each columns of matrice m
    for i in range(len(m[0])):
        # take column and interpolate it using lagrange
        col = m.take(i, 1)
        myPoly = lagrange(xs, col)
        # polys = polys + myPolys => Homomorphism of vector to poly under +
        polys.append(myPoly)

    # multiply the polynomials by the witness and + them
    newPolys = []
    for i in range(len(polys)):
        newPoly = polys[i] * w[i]
        newPolys.append(newPoly)

    finalPolynomial = 0
    for i in range(len(newPolys)):
        finalPolynomial = newPolys[i] + finalPolynomial

    return finalPolynomial

aPolynomial = vectorsToPolynomials(A, w)
bPolynomial = vectorsToPolynomials(B, w)
cPolynomial = vectorsToPolynomials(C, w)

# W(x) = U(x) * V(x)
leftPolynomial = aPolynomial * bPolynomial

# sanity check evaluate at x=1
print(f'{leftPolynomial(1)}')
print(f'{cPolynomial(1)}')

# calculate T
t = (x-1) * (x-2) * (x-3)

# calculate h = {U(x)*V(x) - W(x)} / t(x)
h = (aPolynomial * bPolynomial - cPolynomial) / t

# left
left = aPolynomial * bPolynomial

# right
right = cPolynomial + h*t

print(f'left: {left}')
print(f'right: {right}')