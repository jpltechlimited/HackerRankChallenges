def mutate_string(string, position, character):
    string_to_list = list(string)
    string_to_list[position] = character
    return ''.join(string_to_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
