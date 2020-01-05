import numpy as np

from problem3 import prime_factors

def is_prime(n):
    f, p = prime_factors(n)
    return len(f) == 1 and p[0] == 1

def nth_prime(N):
    n, i = 2, 1
    while i < N:
        n += 1
        if is_prime(n):
            i += 1
    return n
    

if __name__ == "__main__":
    N = 10001
    print(f"The {N}th prime is {nth_prime(N)}")