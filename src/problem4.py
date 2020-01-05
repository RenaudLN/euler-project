import pandas as pd
import itertools

def is_palindrome(n):
    """ Defines whether an integer is a palindrome.

    Parameters
    ----------
    n : int
        The integer to check

    Returns
    -------
    bool
        Whether the integer is a palindrome
    """
    s = str(n)
    return all([s[i] == s[- i - 1] for i in range(int(len(s) / 2))])

if __name__ == "__main__":
    products_3digits = pd.Series(map(lambda x: x[0] * x[1], itertools.product(range(100, 1000), range(100, 1000))))
    fit_criteria = products_3digits[products_3digits.apply(is_palindrome)]
    print(f"There are {len(fit_criteria)} numbers fitting the criteria, the biggest one is {fit_criteria.max()}")