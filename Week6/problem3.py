import numpy as np
from numpy.typing import NDArray
from typing import Any
from py_ecc.bn128 import G1, G2, add, curve_order, multiply, neg, pairing, eq

def verifyEquation(s1: NDArray[Any], s2: NDArray[Any]) -> bool:
    assert len(s1) == len(s2)
    # Validate that all s1 and s2 points are equivalent points in G1<->G2 space
    for j in range(len(s1)):
        left = pairing(multiply(G2, 5), s1[j])
        right = pairing(s2[j], multiply(G1, 5))
        assert eq(left, right), f"Points at index {j} are not equivalent in G1 and G2 spaces"

    A = np.dot(L, s1)
    B = np.dot(R, s2)
    C = np.dot(O, s1)

    for i in range(len(L)):
        left = pairing(B[i], A[i])
        right = pairing(G2, C[i])
        if not eq(left, right):
            return False
    return True

# Define the matrices for the equation xy = v, v*v = w
L = np.array([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

R = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
])

O = np.array([
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])

# Test cases
print("Running test cases:")

# Test case 1: Should pass (2 * 3 = 6, 6 * 6 = 36)
s1 = np.array([G1, multiply(G1, 2), multiply(G1, 3), multiply(G1, 6), multiply(G1, 36)])
s2 = np.array([G2, multiply(G2, 2), multiply(G2, 3), multiply(G2, 6), multiply(G2, 36)])
result = verifyEquation(s1, s2)
print(f"Test case 1 (should pass): {result}")
assert result == True, "Test case 1 failed"

# Test case 2: Should fail (incorrect last value)
s1 = np.array([G1, multiply(G1, 2), multiply(G1, 3), multiply(G1, 6), multiply(G1, 35)])
s2 = np.array([G2, multiply(G2, 2), multiply(G2, 3), multiply(G2, 6), multiply(G2, 35)])
result = verifyEquation(s1, s2)
print(f"Test case 2 (should fail): {result}")
assert result == False, "Test case 2 failed"

# Test case 3: Should raise an assertion error (mismatched s1 and s2)
try:
    s1 = np.array([G1, multiply(G1, 3), multiply(G1, 3), multiply(G1, 6), multiply(G1, 35)])
    s2 = np.array([G2, multiply(G2, 2), multiply(G2, 3), multiply(G2, 6), multiply(G2, 35)])
    verifyEquation(s1, s2)
    print("Test case 3 failed: Expected AssertionError")
except AssertionError:
    print("Test case 3 passed: AssertionError raised as expected")

print('All tests completed')