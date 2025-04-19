def plusMinus(arr):
    postive = negative = zero = 0
    for i in arr:
        if i > 0:
            postive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    return postive / len(arr) , negative / len(arr) , zero / len (arr) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(*plusMinus(arr))
