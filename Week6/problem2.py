import numpy as np



def verify_r1cs(A, B, C, w):
    """
    Verifies the R1CS equation: Aw ⊙ Bw - Cw = 0
    
    Parameters:
    A, B, C (np.array): The R1CS matrices
    w (np.array): The witness vector
    
    Returns:
    bool: True if the equation holds, False otherwise
    """
    Aw = A.dot(w)
    Bw = B.dot(w)
    Cw = C.dot(w)
    
    # Hadamard (element-wise) product
    AwBw = np.multiply(Aw, Bw)
    
    # Check if AwBw - Cw = 0
    result = np.allclose(AwBw - Cw, np.zeros_like(Cw))
    
    return result

# Define the improved matrices
A = np.array([
    [0, 0, 1, 0, 0],  # x
    [0, 0, 0, 1, 0],  # v₁
    [0, 1, 0, 0, 0]   # out
])

B = np.array([
    [0, 0, 1, 0, 0],  # x
    [0, 0, 1, 0, 0],  # x
    [1, 0, 0, 0, 0]   # 1 (constant)
])

C = np.array([
    [0, 0, 0, 1, 0],  # v₁
    [0, 0, 0, 0, 1],  # v₂
    [5, 0, 1, 0, 1]   # 5 + x + v₂
])

# Define the witness vector for x = 3
w = np.array([1, 35, 3, 9, 27])  # [1, out, x, v₁, v₂]

is_valid = verify_r1cs(A, B, C, w)
print(f"Is the R1CS valid? {is_valid}")