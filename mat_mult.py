

def mat_mult(mat1, mat2):
    if ( mat1 == None or mat2 == None ):
        print("ERROR: One or both matrices are empty")
        return 254
    
    if ( len(mat1) != len(mat2[0]) ):
        print("ERROR: Matrices are not appropriate size for multiplication")
        return 255
    
    for j in range(len(mat1) - 1):
        if (len(mat1[j]) != len(mat1[j+1])):
            print("ERROR: Matrix 1 does not have uniform size of rows")
            return 106
                   
    for i in range(len(mat2) - 1):
        if (len(mat2[i]) != len(mat2[i+1])):
            print("ERROR: Matrix 2 does not have uniform size of rows")
            return 106

    product = []
                   
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            product[i][j] = mat1[i][j] * mat2[j][i]
            
                   
    return product

class TestMat:
    def test_shell(self):
        assert mat_mult([0],[0]) == 0
    
