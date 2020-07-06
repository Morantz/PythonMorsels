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

for (ms1, ms2) in zip(matrix1, matrix2):
    result.append(ms1 + ms2)

print(f'Results are {result}')

