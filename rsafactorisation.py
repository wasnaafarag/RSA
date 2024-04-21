import math
import random
import time 

user= int(input("Enter 8 or 16 bits: "))#O(c)
users_input= int(input("Enter message to encrypt: "))#O(c)
start=time.time()#O(c)

def is_prime(num):#O(c)
    """Checks if a number is prime using trial division."""
    if num <= 1: #O(C)
        return False
    if num <= 3:#O(C)
        return True
    if num % 2 == 0 or num % 3 == 0:#O(C)
        return False
    i = 5
    while i * i <= num:#O(n)
        if num % i == 0 or num % (i + 2) == 0:#O(C)
            return False
        i += 6
    return True

def get_random_prime(user):
    """Generates a random prime number of a specified bit length."""
    while True:#O(n)
        # Generate a random number within the desired bit length
        num = random.getrandbits(user)
        # Make sure the number is odd and has the desired bit length
        num |= 1  # Ensure the number is odd
        num |= (1 << (user - 1))  # Ensure the number has the correct bit length
        
        # Check if the number is prime
        if is_prime(num):#O(c)
            return num
        

def extended_gcd(a, b):
    """Extended Euclidean algorithm to find the gcd of a and b and coefficients x and y."""
    if a == 0:#O(C)
        return b, 0, 1
    else: #O(C)
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def rsa_key_generation(bit_length):
    """Generates RSA public and private keys."""
    # Generate prime numbers p and q
    if user == 8:#O(C)
        p = get_random_prime(8)
        q = get_random_prime(8)
    elif user == 16: #O(C)
        p = get_random_prime(16)
        q = get_random_prime(16)
    else: #O(C)
        exit()
    
    # Compute n and euler's totient function (eul)
    n = p * q
    eul = (p - 1) * (q - 1)
    
    # Choose a public exponent e
    e = 65537  # Common choice for e
    
    # Ensure e is coprime to eul
    gcd, x, y = extended_gcd(e, eul)
    
    while gcd != 1: #O(n)
        e = random.randint(2, eul - 1)
        gcd, x, y = extended_gcd(e, eul)
    
    # Calculate the private exponent d
    d = x % eul
    if d < 0:#O(C)
        d += eul
    
    # Return public and private keys
    public_key = (n, e)
    private_key = (n, d)
    print("p&q =" ,p, q)
    return public_key, private_key

# Generate RSA keys
public_key, private_key = rsa_key_generation(bit_length=16)
print("Public key:", public_key)
print("Private key:", private_key)

# Test encryption and decryption
# m = 11  # Message to be encrypted
(n, e) = public_key
(n, d) = private_key

# Encrypt the message
C = pow(users_input, e, n)

# Decrypt the message
M = pow(C, d, n)
end=time.time()
time=(end-start)*1000

print("\nEncrypted message:", C)
print("\nDecrypted message:", M)
print("n = ", n)
print("time taken is: ", time) 







