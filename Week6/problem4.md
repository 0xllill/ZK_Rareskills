

1. Single Multiplication per Row:
Each row in an R1CS represents one constraint, and each constraint involves exactly one multiplication. This is why it's called a "Rank-1" Constraint System - each constraint is reducible to a single product of two linear combinations.
R1CS Structure:
An R1CS constraint is of the form:
(a · x) * (b · x) = (c · x)
where a, b, and c are vectors, x is the vector of variables and intermediate values, and · denotes the dot product.


Relation to Bilinear Pairings:
Bilinear pairings are functions e: G1 × G2 → GT that satisfy the bilinearity property:
e(aP, bQ) = e(P, Q)^(ab) for any P ∈ G1, Q ∈ G2, and a, b ∈ F
This property aligns perfectly with the structure of R1CS constraints:
a. Left side of R1CS: (a · x) * (b · x)
b. Right side of R1CS: (c · x)
c. Pairing equation: e(g^(a·x), g^(b·x)) = e(g, g)^(c·x)
Where g is a generator of the group.