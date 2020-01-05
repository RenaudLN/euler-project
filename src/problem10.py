import numpy as np

from problem1 import find_multiples_of
from problem7 import is_prime

def primes_below(n):
    factors = np.arange(2, np.sqrt(n))
    values = np.arange(2, n + 1)
    multiples = find_multiples_of(factors, values)
    primes_above_sqrtn = set(values) - multiples
    primes_below_sqrtn = set([int(f) for f in factors if is_prime(f)])
    return primes_below_sqrtn.union(primes_above_sqrtn)

if __name__ == "__main__":
    N = 2e6
    print(f"The result is {sum(primes_below(N))}.")