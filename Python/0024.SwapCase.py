def swap_case(s):
    result = ""
    for letter in s:
        upperCase = letter.upper()
        if upperCase == letter:
            result += letter.lower()
        else:
            result += upperCase
    return result

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)