def solve(array):
    result = 0
    for i in array:
        result += i 
    return result

if __name__ == "__main__":
    array = [ 1, 2 , 3 , 4, 5, 6, 7]
    print(solve(array))