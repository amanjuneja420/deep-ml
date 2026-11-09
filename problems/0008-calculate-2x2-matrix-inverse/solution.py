def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    if(a*d-b*c == 0.0 ):
        return "None"
    det = a*d -b*c

    ans = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    ans[0][1] = -matrix[0][1]  
    ans[1][0] = -matrix[1][0] 
    ans[0][0] = matrix[1][1]
    ans[1][1] = matrix[0][0]

    ans[0][0]/=det
    ans[0][1]/=det
    ans[1][0]/=det
    ans[1][1]/=det

    return ans
