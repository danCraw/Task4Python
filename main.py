import re


def readLineFromFile(fileName):
    f = open(fileName, encoding="utf-8")
    line = f.read()

    return line


def numberIt(line):
    result = re.split('(?<=[.?!])\s+', line)

    for i in range(len(result)):
        result[i] = result[i] + '[' + str(i + 1) + ']'

    print(result)


if __name__ == '__main__':
    line = readLineFromFile('input01.txt')
    numberIt(line)
