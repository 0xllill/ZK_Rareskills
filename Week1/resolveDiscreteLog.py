
# Brute force approach to find s such that (g^s) % n == encrypted_number
def find_discrete_log(g, n, encrypted_number):
    for s in range(n):
        if pow(g, s, n) == encrypted_number:
            return s
    return None


# Given values
n = 9551
g = 5
encrypted_number = 5666


# Finding the solution
student_solution = find_discrete_log(g, n, encrypted_number)



assert pow(g, student_solution, n) == encrypted_number
print("student_solution is {}".format(student_solution))