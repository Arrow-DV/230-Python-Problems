import sys
def miniMaxSum(arr):
    s = 0
    mininum = sys.maxsize
    maxnumber = 0
    for i in range(len(arr)):
        s += arr[i]
        mininum = min(mininum,arr[i])
        maxnumber = max(maxnumber,arr[i])
    return s - maxnumber , s - mininum
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(*miniMaxSum(arr))
