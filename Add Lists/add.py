
def show_header():
    print('*******************************')
    print('     Adding Lists of Lists')
    print('*******************************')
    print()

def addlist(mat1, mat2):
    sums = []

    # for (mat1, mat2) in zip(matrix1, matrix2):
    for (m1, m2) in zip(mat1, mat2):
        sums.append(m1 + m2)

    return sums

def add(list1, list2):
    a1 = addlist(list1[0], list2[0])
    a2 = addlist(list1[1], list2[1])
    print(f'A1 is: [{a1}, {a2}]')

    r = addlist(a1, a2)
    return r


def main():
    show_header()

    print('Test One:')

    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]

    print(f'Matrix1 is: {matrix1}')
    print(f'Matrix2 is: {matrix2}')
    print()

    result = add(matrix1, matrix2)

    print(f'Results are {result}')

    print('Test Two:')

    matrix1 = [[1, -2, 3], [-4, 5, -6]]
    matrix2 = [[1, 1, 0], [1, -2, 3]]

    print(f'Matrix1 is: {matrix1}')
    print(f'Matrix2 is: {matrix2}')
    print()

    result = add(matrix1, matrix2)

    print(f'Results are {result}')


if __name__ == '__main__':
    main()
