from sympy.ntheory import discrete_log

n = 1000004119
g = 5
encrypted_number = 767805982

# Finding the solution
student_solution = discrete_log(n,encrypted_number, g)

assert pow(g, student_solution, n) == encrypted_number
print("student_solution is {}".format(student_solution))