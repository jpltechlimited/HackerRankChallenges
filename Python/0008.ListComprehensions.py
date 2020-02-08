def print_lexicographic(x, y, z, n):
    result = []
    for xAxis in range(x + 1):
        for yAxis in range(y + 1):
            for zAxis in range(z + 1):
                if xAxis + yAxis + zAxis != n:
                    vector = [xAxis, yAxis, zAxis]   
                    result.append(vector)
    print(result, end='')

if __name__ == '__main__':
    print_lexicographic(1,1,1,2)