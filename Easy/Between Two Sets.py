

from functools import reduce
def getTotalX(a, b):
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a % b)
    def lcm(a,b):
        return a * b // gcd(a,b)
    l =  reduce(lcm,a)
    g = reduce(gcd,b)
    s = 0
    for i in range(l,g+1,l):
        if g % i == 0:
            s+=1
    return s 
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)


