from scipy.interpolate import lagrange
import numpy as np


xs = np.array([1,2,3])
ys = np.array([3,4,5])

a = np.array([4,2,0])
b = np.array([4,9,20])

def phi(c):
    return lagrange(xs,c)


print(phi(a+b) == phi(a) + phi(b))
print(phi(xs+ys) == phi(xs) + phi(ys))


"""
Homomorphism from colum vector under addtion to polynomials under addition => R1CS can be expressed via polynomials instead of column vectors
Means each time we add columns vectors together we can convert them to polynomials and add polynomials together
"""