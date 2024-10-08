def main():
    row = int(input('Input the number of rows: ').strip())
    column = int(input('Input the number of columns: ').strip())
    divisible = int(input('Please input the number by which the numbers in the resulting matrix should be divisible by: '))
    greater = int(input('Please input the number that should serve as a minimum threshold for the numbers in the resulting matrix: '))
    matrix_a = [[int(input()) for _ in range(row)] for _ in range(column)]
    matrix_b = [[int(input()) for _ in range(row)] for _ in range(column)]
    result = fun(matrix_a, matrix_b)
    fun2(result,greater, divisible)

def fun(matrix_a, matrix_b):
    transposed_b = list(zip(*matrix_b))
    result = [[sum(a*b for (a,b) in zip(rows,cols)) for cols in transposed_b] for rows in matrix_a]
    return result

def fun2(result,greater, divisible):
    result = sorted([x for y in result for x in y if x % divisible == 0 and x > greater])
    print(*result)

if __name__ == '__main__':
    main()
