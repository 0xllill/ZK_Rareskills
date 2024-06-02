import hashlib
import random
from ecdsa.ellipticcurve import Point

OrderN = 115792089237316195423570985008687907852837564279074904382605163141518161494337 
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
P = 115792089237316195423570985008687907853269984665640564039457584007908834671663  # Prime
A = 0  # Curve parameter a
B = 7  # Curve parameter b
OrderN = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Order of the curve



# Define the modular inverse function
def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s % p

# Define point addition
def point_addition(P, Q):
    if P == Q:
        return point_doubling(P)
    if P.x() == Q.x() and P.y() != Q.y():
        return Point(None, None, None, None)
    
    lam = ((Q.y() - P.y()) * inverse_mod(Q.x() - P.x(), P.curve().p)) % P.curve().p
    x_r = (lam**2 - P.x() - Q.x()) % P.curve().p
    y_r = (lam * (P.x() - x_r) - P.y()) % P.curve().p
    
    return Point(P.curve(), x_r, y_r, P.order())

# Define point doubling
def point_doubling(P):
    lam = ((3 * P.x()**2 + P.curve().a) * inverse_mod(2 * P.y(), P.curve().p)) % P.curve().p
    x_r = (lam**2 - 2 * P.x()) % P.curve().p
    y_r = (lam * (P.x() - x_r) - P.y()) % P.curve().p
    
    return Point(P.curve(), x_r, y_r, P.order())

# Define scalar multiplication
def scalar_multiplication(k, P):
    Q = Point(None, None, None, None)
    while k:
        if k & 1:
            if Q.x() is None:
                Q = P
            else:
                Q = point_addition(Q, P)
        P = point_doubling(P)
        k >>= 1
    return Q

# Custom curve representation
class Curve:
    def __init__(self, p, a, b):
        self._p = p
        self._a = a
        self._b = b

    def contains_point(self, x, y):
        return (y**2 - (x**3 + self._a * x + self._b)) % self._p == 0

    @property
    def p(self):
        return self._p

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def cofactor(self):
        return 1



################### EXERCICE ###################

# Initialize the ECC curve
curve = Curve(P, A, B)
generator = Point(curve, Gx, Gy, OrderN)


# Step 1: Pick a private key
def generate_private_key():
    return random.randint(1, OrderN - 1)


# Step 2: Generate the public key
def generate_public_key(private_key):
    public_key = scalar_multiplication(private_key, generator)
    return public_key

# Step 3: Pick a message and hash it
def hash_message(message):
    message_hash = hashlib.sha256(message.encode('utf-8')).digest()
    return int.from_bytes(message_hash, 'big')


# Step 4: Sign the message
def sign_message(private_key, message):
    # calculate message hash
    message_hash = hash_message(message)
    # Generate random point in (1,n-1) (non-deterministic ECDSA)
    k = random.randint(1, OrderN - 1)

    # compute random point R = k * G TODO
    R = scalar_multiplication(k, generator)
    # take coordinate r = R.x
    r = R.x() % OrderN
    # compute signature proof 
    s = ((message_hash + r * private_key) * inverse_mod(k, OrderN)) % OrderN
    # return signature
    return (r, s)


# Step 5: Verify the signature
def verify_signature(r, s, message, public_key):
    # hash msg using same way used when signed
    message_hash = hash_message(message)
    # calculate modular inverse of signature proof
    s1 = inverse_mod(s, OrderN)
    # recover random point R' 
        # point1 = h * s1 * G
    u1 = (message_hash * s1) % OrderN
    point1 = scalar_multiplication(u1, generator)
        # point2 = r * s1 * pubKey
    u2 = (r * s1) % OrderN
    point2 = scalar_multiplication(u2, public_key)
    
    # Add point1 and point 2 = (h * s1 * G) + r * s1 * pubKey
    point = point_addition(point1, point2)
    # ensure r == r'
    return r == point.x() % OrderN



# Example usage
private_key = generate_private_key()
public_key = generate_public_key(private_key)

message = "ret2Basic the beast"
r, s = sign_message(private_key, message)

is_valid = verify_signature(r, s, message, public_key)
print(f"Signature valid: {is_valid}")
