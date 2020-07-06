import sys
import io

def show_header():
    print('*******************************')
    print('     Adding Lists of Lists')
    print('*******************************')
    print()

def addlists(m1, m2):
    sums = []

    for (ms1, ms2) in zip(m1, m2):
        sums.append(ms1+ms2)

    return sums


show_header()

# matrix1 = [[1, -2], [-3, 4]]
# matrix2 = [[2, -1], [0, -1]]
matrix1 = [1, 2, 3]
matrix2 = [4, 5, 6]

# result = addlists(matrix1, matrix2)

result = []

for (mat1, mat2) in zip(matrix1, matrix2):
    for (m1, m2) in zip(mat1, mat2):
        result.append(m1 + m2)

print(f'Results are {result}')

