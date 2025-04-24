def countApplesAndOranges(s, t, a, b, apples, oranges):
    # apples_count  = oranges_count = 0

    # for i in range(len(apples)):
    #     if s <= a + apples[i] <= t:
    #         apples_count += 1

    # for i in range(len(oranges)):
    #     if s <= a + oranges[i] <= t:
    #         oranges_count += 1

    # print(apples_count,oranges_count,sep="\n")
    apples_count = sum(1 for d in apples if s <= a + d <= t)
    oranges_count = sum(1 for d in oranges if s <= b + d <= t)
    print(apples_count,oranges_count,sep="\n")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
