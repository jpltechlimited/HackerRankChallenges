def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def merge_the_tools(string, k):
    groups = zip(*(iter(string),) * k)
    for group in groups:
        print("".join(remove_duplicates(group)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)