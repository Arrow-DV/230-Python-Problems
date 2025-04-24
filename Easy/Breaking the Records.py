def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0
    
    for score in scores[1:]:
        if max_score < score:
            max_score = score 
            max_count += 1
        elif min_score > score:
            min_score = score 
            min_count += 1
    
    return [ max_count,min_count]
if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
