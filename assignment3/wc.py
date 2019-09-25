import sys
import ntpath

def countNumberOfWordsInFile(file):
    f = open(file, "r")
    numberOfWords = f.read().split()
    print('number of words in a file: {wordsNo}'.format(wordsNo=len(numberOfWords)))

def countNumberOfLinesInFile(file):
    f = open(file, "r")
    nummberOflines = sum(1 for line in f)
    print('number of lines in a file: {lineNo}'.format(lineNo=nummberOflines))


def countNumberOfCharsInFile(file):
    text1=open(file,'r').read()
    print('number of chars in a file: {charNo}'.format(charNo=len(text1)))

def printFileName(file):
    print('name of the file: {fileName}'.format(fileName=ntpath.basename(file)))

def main(argv):
    countNumberOfWordsInFile(argv[0])
    countNumberOfLinesInFile(argv[0])
    countNumberOfCharsInFile(argv[0])
    printFileName(argv[0])
  
  
if __name__ == '__main__':
    main(sys.argv[1:])