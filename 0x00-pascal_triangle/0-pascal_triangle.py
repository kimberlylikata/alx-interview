#!/usr/bin/python3
"""
Function to generate Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Create the new row using elements from the previous row
        new_row = [1]  # Start with 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
