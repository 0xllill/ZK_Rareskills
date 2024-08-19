import numpy as np
import galois
from functools import reduce
from py_ecc.bn128 import G1, G2, multiply, add, curve_order, eq, Z1, pairing, is_on_curve

print("this may take some time")
fieldOrder = curve_order
GF = galois.GF(fieldOrder)

L = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

R = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

O = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [(fieldOrder - 3),1,1,2,0,(fieldOrder - 1)]])

L_galois = GF(L)
R_galois = GF(R)
O_galois = GF(O)

x = GF(21)
y = GF(21)

out = 3 * x * x * y + 5 * x * y + GF(fieldOrder - 1)*x + GF(fieldOrder - 2) * y + GF(3)
v1 = 3*x*x
v2 = v1 * y
w = GF(np.array([1, out, x, y, v1, v2]))

assert all(np.equal(np.matmul(L_galois, w) * np.matmul(R_galois, w), np.matmul(O_galois, w))), "not equal"

def interpolate_column(col):
    xs = GF(np.array([1,2,3]))
    return galois.lagrange_poly(xs, col)

# axis 0 is the columns. apply_along_axis is the same as doing a for loop over the columns and collecting the results in an array
U_polys = np.apply_along_axis(interpolate_column, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, O_galois)

def inner_product_polynomials_with_witness(polys, witness):
    mul_ = lambda x, y: x * y
    sum_ = lambda x, y: x + y
    return reduce(sum_, map(mul_, polys, witness))

U = inner_product_polynomials_with_witness(U_polys, w)
V = inner_product_polynomials_with_witness(V_polys, w)
W = inner_product_polynomials_with_witness(W_polys, w)

# t = (x - 1)(x - 2)(x - 3)
t = galois.Poly([1, (fieldOrder - 1)], field = GF) * galois.Poly([1, (fieldOrder - 2)], field = GF) * galois.Poly([1, (fieldOrder - 3)], field = GF)

h = (U * V - W) // t
HT_poly = h * t

lhs = U * V
rhs = W + HT_poly
print(f'{lhs} = {rhs}')
assert lhs == rhs, "the unencrypted polynomials do not match"
print('the unencrypted polynomials match. so far so good.\n\n')


"""
STEP 1 : Do an encrypted evaluation of each of these polynomials, this will result in
    eval(U) = [A]_1\\  in G1
    eval(V)=[B]_2,\\ in G2
    eval(W)=[C']_1,\\ in G1
    eval(HT)=[HT]_1 \\ in G1
"""

# evaluate at 8
tau = GF(8)


def generate_powers_of_tau(tau, degree):
    return [multiply(G1, int(tau ** i)) for i in range(degree + 1)]

def generate_powers_of_tau_G2(tau, degree):
    return [multiply(G2, int(tau ** i)) for i in range(degree + 1)]

## create power of tau G1 and G2
g1_srs = generate_powers_of_tau(tau, 4)
g2_srs = generate_powers_of_tau_G2(tau, 4)


# re-wrote inner_product a few different ways to see if there is an error in what is from the textbook
# these all output the same values
def inner_product(ec_points, coeffs):
    return reduce(add, (multiply(point, int(coeff)) for point, coeff in zip(ec_points, coeffs)), Z1)


# evaluate then convert

A_1 = inner_product(g1_srs, U.coeffs[::-1])

B_2 = inner_product(g2_srs, V.coeffs[::-1])

C_1 = inner_product(g1_srs, W.coeffs[::-1])

# evaluate HT polynomial with G1_srs to produce [HT]1
HT_1 = inner_product(g1_srs, HT_poly.coeffs[::-1])


"""
STEP 2 :
    Then create [C]=[C']_1+[HT]_1
"""
C_1 = add(C_1, HT_1)

"""
STEP 3 : 
    Verify \text{pairing}([A]_1,[B]_2)-\text{pairing}([C]_1,[G]_2) = 0
"""

left_side = pairing(B_2,A_1)
right_side = pairing(G2, C_1)
print(f'left = {left_side}')
print(f'right = {right_side}')

zeroG12 = left_side - right_side
assert eq(left_side, right_side), "Pairing check failed"

print("Pairing check passed successfully!")
# below should be G12 point at infinity
print(f'zeroG12 = {zeroG12}\n\n')