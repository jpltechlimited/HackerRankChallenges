def solve(s):
    lst = [x for x in s]
    for index, charact in enumerate(lst):
        if (lst[index] != " ") & (index == 0):
            lst[index] = charact.capitalize() 
        elif (lst[index] != " ") & (lst[index -1] == " "):            
            lst[index] = charact.capitalize() 
    return "".join(lst)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)