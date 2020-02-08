def runner_up(positionsList):
    positionsList.sort(reverse=True)
    result = list(dict.fromkeys(positionsList)) #remove duplicates
    return result[1] 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up(list(arr)))