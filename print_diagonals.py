def print_diagonals(arr):
    """
    Print out the diagonals (top-right to bottom-left) of a given 2-D array

    >>> arr = [[9, 3, 2, 4], [8, 6, 1, 2], [5, 5, 6, 7], [1, 2, 8, 4]]
    >>> print_diagonals(arr)
    9 
    3 8 
    2 6 5 
    4 1 5 1 
    2 6 2 
    7 8 
    4 

    """
    for i in range((len(arr) + len(arr[0])) - 1):
        diag = ""
        j = i / len(arr)
        while i - j >= 0 and j < len(arr):
            if i - j < len(arr):
                diag += str(arr[j][i - j]) + " "
            j += 1
        print diag


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"
