import numpy as np

def pythagorean_triplets(N):    
    for a in range(1, N - 1):
        for b in range(1, N - a + 1):
            for c in range(1, N - b - a + 1):
                if a + b + c == N:
                    [x, y, z] = sorted([a, b, c])
                    if x ** 2 + y ** 2 == z ** 2:
                        return x, y, z

if __name__ == "__main__":
    N = 1000
    print(f"The result is {np.array(pythagorean_triplets(N)).prod()}")