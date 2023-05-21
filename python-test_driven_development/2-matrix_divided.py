#!/usr/bin/python3

"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """''def matrix_divided(matrix, div):'' divide each
    elelemt of the matrix is divided by div and
    return a new matrix with the results with a 2
    precision numbers. If div not is a number raise
    TypeError or ZeroDivisionError if div is 0:
    If matrix not is a list of lists return TypeError.
    If some sub-list aren't a list return TypeError.
    If some element of some sub-list aren't integer
    or float number return TypeError."""

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    """ check if all rows have the same size """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ check if div is a number (integer or float) """
    if not isinstance(div, (int, float)):
        raise TypeError("must be a number")

    """ check if div is not equal to zero """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
    """ Perform the division and round the results to 2 decimal places """
