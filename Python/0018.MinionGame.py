#idea shamelessly copied from discussion board
def minion_game(s):
    vowels = "AEIOU"
    kevinPoints = 0
    stuartPoints = 0
    for index in range(len(s)):
        if s[index] in vowels:
            kevinPoints += (len(s)-index)
        else:
            stuartPoints += (len(s)-index)

    if kevinPoints > stuartPoints:
        print("Kevin", kevinPoints)
    elif kevinPoints < stuartPoints:
        print("Stuart", stuartPoints)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)