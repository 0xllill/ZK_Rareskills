import numpy as np
import random
from scipy.interpolate import lagrange
from numpy.typing import NDArray
from numpy import poly1d
from numpy.polynomial.polynomial import Polynomial
import galois
from functools import reduce


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
               [76,1,1,2,0,78]])


GF = galois.GF(79)
A_galois = GF(A)
B_galois = GF(B)
C_galois = GF(C)

# pick values for x and y
x = GF(79-21) # 100 modulo 79 to keep the same as Ex 2
y = GF(79-21) # 100 modulo 79 to keep the same as Ex 2

# this is our original formula
# out = 3yx^2 + 5xy - x - 2xy + 3
out = GF(3) * x * x * y + 5 * x * y - x + GF(79-2)*y + GF(3)# the witness vector with the intermediate variables inside
v1 = GF(3)*x*x
v2 = v1 * y

w = GF(np.array([1, out, x, y, v1, v2]))

assert all(np.equal(np.matmul(A_galois, w) * np.matmul(B_galois, w), np.matmul(C_galois, w))), "not equal"

def interpolate_column(col):
    xs = GF(np.array([1,2,3]))
    return galois.lagrange_poly(xs, col)

# axis 0 is the columns. apply_along_axis is the same as doing a for loop over the columns and collecting the results in an array
U_polys = np.apply_along_axis(interpolate_column, 0, A_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, B_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, C_galois)


# Check => [Poly(0, GF(79)) Poly(0, GF(79))]# [Poly(0, GF(79)) Poly(0, GF(79))]# [Poly(0, GF(79))]

def inner_product_polynomials_with_witness(polys, witness):
    mul_ = lambda x, y: x * y
    sum_ = lambda x, y: x + y
    return reduce(sum_, map(mul_, polys, witness))

term_1 = inner_product_polynomials_with_witness(U_polys, w)
term_2 = inner_product_polynomials_with_witness(V_polys, w)
term_3 = inner_product_polynomials_with_witness(W_polys, w)

# t = (x - 1)(x - 2)(x - 3)
t = galois.Poly([1, 78], field = GF) * galois.Poly([1, 77], field = GF) * galois.Poly([1, 76], field = GF) 

h = (term_1 * term_2 - term_3) // t

assert term_1 * term_2 == term_3 + h * t, "division has a remainder"