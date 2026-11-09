def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])

    # a x b => a_col should be equal to b_row
    # a_row x b_col

    if(a_col!=b_row): 
        return -1

    mat_ans = [[0 for _ in range(b_col)] for _ in range(a_row)]

    # a[i][j]*b[j][k] = mat_ans[i][k]

    for i in range(a_row):
        for j in range(b_row):
            for k in range(b_col):
                mat_ans[i][k] = mat_ans[i][k] + a[i][j]*b[j][k]

    return mat_ans