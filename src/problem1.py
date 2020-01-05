import numpy as np
import itertools

def find_multiples_of(factors, values):
    """ Find the multiples of certain factors in an array of natural integers
    
    Parameters
    ----------
    factors : list of int
        The factors to look for
    values : np.array or pd.Series
        The values among which to for the factors

    Returns
    -------
    set
        The integers that are multiple of either of the factors
    """
    return set(itertools.chain.from_iterable([values[values % f == 0] for f in factors]))

if __name__ == "__main__":
    factors = [3, 5]
    max_N = 999
    naturals = np.arange(1, max_N + 1)
    print(f"The results is {sum(find_multiples_of(factors, naturals))}.")
