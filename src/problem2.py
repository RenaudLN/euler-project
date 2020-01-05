import numpy as np

from problem1 import find_multiples_of

def fibonacci(max_N, initial=[1, 1]):
    """ Return the Fibonacci sequence up to max_N

    Parameters
    ----------
    max_N : int
        The value not to exceed in the sequence
    initial : list of int, optional
        The starting points for the Fibonacci sequence

    Returns
    -------
    np.array
        The 1D Fibonacci sequence
    """
    fb = initial
    while fb[-1] <= max_N:
        fb.append(fb[-1] + fb[-2])
    return np.array(fb)

if __name__ == "__main__":
    fibo = fibonacci(4e6)
    print(f"The result is {sum(find_multiples_of([2], fibo))}.")
