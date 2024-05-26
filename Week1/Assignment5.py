from sympy import mod_inverse

# Given values
a_num = 53
a_den = 192
b_num = 61
b_den = 511

modulus = 1033

print(f"Output result of 53/192 + 61/511 (mod 1033) : ")

# Compute the modular inverses of the denominators
    # 192 ^(-1) mod 1033 = 382
a_den_inv = pow(a_den, -1, modulus)
    # 511 ^(-1) mod 1033 = 845
b_den_inv = pow(b_den, -1, modulus)


# Convert the fractions to integers under modulo 1033
    # 192 * 845
frac1 = (a_num * a_den_inv) % modulus
frac2 = (b_num * b_den_inv) % modulus

# Add the two numbers and take the result modulo 1033
result_mod = (frac1 + frac2) % modulus

# Print the results
sol_num = 38795
sol_den = 98112
# Verify with original rational sum

    # 98112 ^(-1) mod 1033 = 845
sol_den_inv = pow(sol_den, -1, modulus)

result_mod2 = (sol_num * sol_den_inv) % modulus
print(f"Sum of 53/192 + 61/511 (mod 1033) modulo 1033  : {result_mod}")
print(f"Sum of 38795/98112 modulo 1033                 : {result_mod2}")