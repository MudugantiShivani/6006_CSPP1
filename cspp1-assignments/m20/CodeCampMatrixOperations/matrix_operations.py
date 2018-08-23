from copy import deepcopy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) != len(m2):
        print("Error: Matrix shapes invalid for mult")
        return None
    res = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            row.append(sum([m1[i][k]*m2[k][j] for k in range(len(m1[0]))]))
        res.append(row)
    return res


def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    res = deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] += m2[i][j]
    return res
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    r, c = list(map(int, input() . split(',')))
    matrix = []
    for i in range(r):
        row = list(map(int, input() . split(' ')))
        if len(row) != c:
            print("Error: Invalid input for the matrix")
            return None
        matrix.append(row)
    return matrix

def main():
    # read matrix 1
    matrix1 = read_matrix()
    if not matrix1:
        return

    # read matrix 2
    matrix2 = read_matrix()
    if not matrix2:
        return 

    # add matrix 1 and matrix 2
    res = add_matrix(matrix1 , matrix2)
    print(res)
    # multiply matrix 1 and matrix 2
    res = mult_matrix(matrix1 , matrix2)
    print(res)
    

if __name__ == '__main__':
    main()
