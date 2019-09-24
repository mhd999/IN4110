import sys

def countNumberOfWordsInFile(file):
    f = open("./test.txt", "r")
    numberOfWords = f.read().split()
    print(len(numberOfWords))

def countNumberOfLinesInFile(file):
    f = open("./test.txt", "r")
    nummberOflines = sum(1 for line in f)
    print(nummberOflines)


def countNumberOfCharsInFile(file):
    text1=open(file,'r').read()
    print(len(text1))

def main(argv):
    countNumberOfWordsInFile(argv[0])
    countNumberOfLinesInFile(argv[0])
    countNumberOfCharsInFile(argv[0])
  
  
if __name__ == '__main__':
    main(sys.argv[1:])