import math
import random
import time 

p = 5
q = 9
e = 2
n = p * q
eul = (p - 1) * (q - 1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

g, x, d = egcd(e, eul)
if g == 1:
    d = x % eul

pub_key = (n, e)
pri_key = (n, d)

print("public key:", pub_key, "\nprivate key:", pri_key)

m = 11
c = pow(m, e, n)
M = pow(c, d, n)

print("\nencrypt:", c, "\ndecrypt:", M)

