import random
import math
import time

def is_prime(num):
    """Checks if a number is prime using trial division."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_random_prime(bit_length):
    """Generates a random prime number of a specified bit length."""
    while True:
        # Generate a random number within the desired bit length
        num = random.getrandbits(bit_length)
        # Make sure the number is odd and has the desired bit length
        num |= 1  # Ensure the number is odd
        num |= (1 << (bit_length - 1))  # Ensure the number has the correct bit length
        
        # Check if the number is prime
        if is_prime(num):
            return num
    
n= int(input("Enter public modulus(n): "))
e= int(input("Enter public key(e): "))
Encrypted= int(input("Enter the encrypted number: "))
Decrypted= int(input("Enter the decrypted number: "))
users_bits= int(input("Enter required bit (8 or 16): "))
p= int(input("Enter p: "))
q= int(input("Enter q: "))
Time= time.time()
phi_n= (q-1)*(p-1) 
def bruteforce(e, phi_n, Encrypted, Decrypted):
    for i in range(2, phi_n): 
        if (e * i) % phi_n == 1:
            Decrypted = pow (Encrypted, i, n)
            if Decrypted == Decrypted:
                return i
    return None 

find= bruteforce(e, phi_n, Encrypted, Decrypted)
print("Private key(d) ", find)
calculated_Time= time.time() - Time 
calculated_Time*=1000 
print( f"Time taken: {calculated_Time:.15f} milli-seconds ")

    


