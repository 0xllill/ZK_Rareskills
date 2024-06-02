import hashlib
import random
from ecdsa.ellipticcurve import Point, CurveFp


OrderN = 115792089237316195423570985008687907852837564279074904382605163141518161494337 
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F  # Prime
A = 0  # Curve parameter a
B = 7  # Curve parameter b
OrderN = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Order of the curve

# Initialize the ECC curve
curve = CurveFp(P, A, B)
generator = Point(curve, Gx, Gy, OrderN)


# Step 1: Pick a private key
def generate_private_key():
    return random.randint(1, OrderN - 1)


# Step 2: Generate the public key
def generate_public_key(private_key):
    public_key = private_key * generator
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
    R = k * generator
    # take coordinate r = R.x
    r = R.x() % OrderN
    # compute signature proof 
    s = ((message_hash + r * private_key) * pow(k, -1, OrderN)) % OrderN
    # return signature
    return (r, s)


# Step 5: Verify the signature
def verify_signature(r, s, message, public_key):
    # hash msg using same way used when signed
    message_hash = hash_message(message)
    # calculate modular inverse of signature proof
    s1 = pow(s, -1, OrderN)
    # recover random point R' 
        # point1 = h * s1 * G
    u1 = (message_hash * s1) % OrderN
    point1 = u1 * generator
        # point2 = r * s1 * pubKey
    u2 = (r * s1) % OrderN
    point2 = u2 * public_key
    
    # Add point1 and point 2 = (h * s1 * G) + r * s1 * pubKey
    point = point1 + point2
    # ensure r == r'
    return r == point.x() % OrderN



# Example usage
private_key = generate_private_key()
public_key = generate_public_key(private_key)

message = "ret2Basic the beast"
r, s = sign_message(private_key, message)

is_valid = verify_signature(r, s, message, public_key)
print(f"Signature valid: {is_valid}")