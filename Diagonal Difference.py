def diagonalDifference(arr):
    leftDiag = rightDiag = 0
    """
    1 2 3
    4 5 6 
    7 8 9
    """
    for i in range(n):
        leftDiag += arr[i][i]
        rightDiag += arr[i][n - 1 -i]
    return abs( leftDiag - rightDiag )
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

