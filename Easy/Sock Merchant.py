
def sockMerchant(n, array):
    counter = 0
    d = {}
    for i in array:
        d[i] = d.get(i,0) + 1
    for key in d.keys():
        counter += d[key] // 2
    return counter
    
if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

