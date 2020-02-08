def execute_command(result, line):
    command = line[0].strip()
    if command == "insert":
        result.insert(int(line[1]),int(line[2]))
    elif command == "remove":
        result.remove(int(line[1]))
    elif command == "append":
        result.append(int(line[1]))
    elif command == "sort":
        result.sort()
    elif command == "print":
        print(result)
    elif command == "reverse":
        result = list(reversed(result))
    elif command == "pop":
        result.pop()
    else:
        pass
    return result

if __name__ == '__main__':
    # N = int(input())
    result = []
    lines = [['insert', '0', '5'], ['insert', '1', '10'], ['insert', '0', '6'], ['print'], ['remove', '6'], ['append', '9'], ['append', '1'], ['sort'], ['print'], ['pop'], ['reverse'], ['print']]
    # for _ in range(N):
    #     line = input().split()
    #     mappedLine = list(map(str, line))
    #     lines.append(mappedLine)
    for line in lines:
        result = execute_command(result, line)       
