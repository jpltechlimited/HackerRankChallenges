if __name__ == '__main__':
    numberOfEnglishStudents = int(input())
    englishStudentsRollNumbers = set(map(int, input().split()))
    numberOfFrenchStudents = int(input())
    frenchStudentsRollNumbers = set(map(int, input().split()))
    print(len(englishStudentsRollNumbers.symmetric_difference(frenchStudentsRollNumbers)))