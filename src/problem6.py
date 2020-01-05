import numpy as np

if __name__ == "__main__":
    N = 100
    values = np.arange(N + 1)
    print(f"The result is {values.sum() ** 2 - (values ** 2).sum()}")