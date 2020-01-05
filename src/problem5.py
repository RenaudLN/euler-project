import numpy as np
import pandas as pd

from problem3 import prime_factors

def smallest_multiple(values):
    decompositions = []
    for v in values:
        factors, powers = prime_factors(v)
        decompositions.append(pd.Series(powers, index=factors))
    decompositions = pd.concat(decompositions, axis=1, keys=values)
    smallest_multiple_decomposition = decompositions.max(axis=1)
    factors = pd.Series(smallest_multiple_decomposition.index)
    powers = smallest_multiple_decomposition.reset_index(drop=True)
    return int((factors ** powers).prod())

if __name__ == "__main__":
    values = np.arange(2, 21)
    print(f"The result is {smallest_multiple(values)}.")