import pdb

def mat_mult(mat1, mat2):
    if ( mat1 == [] or mat2 == [] or mat1 == None or mat2 == None ):
        print("ERROR: One or both matrices are empty")
        return 254
    
    if ( isinstance(mat1, list) == False or isinstance(mat2, list) == False ):
        print("ERROR: Matrices are not list type")
        return 253

    if ( isinstance(mat1[0], list) == False or isinstance(mat2[0], list) == False ):
        print("ERROR: Matrices do not have internal lists")
        return 252
        
    if ( len(mat1[0]) != len(mat2) ):
        print("ERROR: Matrices are not appropriate size for multiplication")
        return 255
    
    for j in range(len(mat1) - 1):
        if (len(mat1[j]) != len(mat1[j+1])):
            print("ERROR: Matrix 1 does not have uniform size of rows")
            return 106
                   
    for i in range(len(mat2) - 1):
        if (len(mat2[i]) != len(mat2[i+1])):
            print("ERROR: Matrix 2 does not have uniform size of rows")
            return 107

    product = [[0] * len(mat2[0]) for l in range(len(mat1))]
    
    #pdb.set_trace()
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                product[i][j] += mat1[i][k] * mat2[k][j]
                   
    return product

    