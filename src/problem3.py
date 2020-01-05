import numpy as np

def prime_factors(n):
    """ Returns the prime factors of an integer along with their exponent in the prime decomposition.

    Parameters
    ----------
    n : int
        The integer to decompose
    
    Returns
    -------
    list
        The list of prime factors
    list
        The exponent of the factors in the prime decomposition
    """
    factors = []
    powers = []
    f = 2
    while n > 1:
        if n % f == 0:
            if factors and factors[-1] == f:
                powers[-1] += 1
            else:
                factors.append(f)
                powers.append(1)
            n /= f
        else:
            f += 1
    return factors, powers

if __name__ == "__main__":
    n = 600851475143
    factors, powers = prime_factors(n)
    decomposition = " * ".join(map(lambda x: f"{x[0]}^{x[1]}", zip(factors, powers)))
    print(f"{n} = {decomposition}")
    print(f"The result is {max(factors)}.")