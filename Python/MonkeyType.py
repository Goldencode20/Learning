import random
import string
import time

# I thought of the infinite monkey theorem and I wanted to see how long 
# it would take to write to be or not to be in as simple terms as possible 
# and I gave it two diffrent ways to write it with a word at a time not in 
# order and then the whole string.

compareString = "to be or not to be"
chars = string.ascii_lowercase + ' ' 
wordList = ["to ", "be ", "or ", "not ", "to ", "be"]

def fullString():
    tempNum = 0
    currentString = ""
    while compareString != currentString:
        currentString += random.choice(chars)
        if currentString[tempNum] == compareString[tempNum]:
            tempNum += 1
        else:
            if (tempNum == 7):
                print(currentString)
            elif (tempNum == 9):
                print(currentString)
            elif (tempNum == 14):
                print(currentString)
            elif (tempNum == 17):
                print(currentString)
            currentString = ""
            tempNum = 0

def septrateWords():
    currentWord = ""
    haveWords = []
    while len(wordList) != 0:
        currentWord += random.choice(chars)
        if len(currentWord) == 1:
            if not (currentWord != "t" or currentWord != "b" or currentWord != "o" or currentWord != "n"):
                currentWord = ""
        elif len(currentWord) == 2:
            if currentWord in wordList:
                wordList.remove(currentWord)
            elif not (currentWord != "to" or currentWord != "be" or currentWord != "or" or currentWord != "no"):
                currentWord = ""
        elif len(currentWord) == 3:
            if currentWord in wordList:
                wordList.remove(currentWord)
                print("Removed: " + currentWord)
                currentWord = "" 
            elif currentWord != "not":
                currentWord = ""
        else:
            if currentWord in wordList:
               wordList.remove(currentWord)
               print("Removed: " + currentWord)
               currentWord = "" 
            else:
                currentWord = "" 



def temp():
    currentString = ""
    for x in range(100):
        currentString += random.choice(chars)
        print (currentString)
        

def main():
    print("Start")
    start_time1 = time.time()
    septrateWords()
    print("--- %s seconds ---" % (time.time() - start_time1))
    start_time2 = time.time()
    fullString()
    print("--- %s seconds ---" % (time.time() - start_time2))

#temp()
main()