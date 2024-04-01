import pandas as pd

def main():
    userInput = str(input("What is the square you are guessing: "))
    userLetter = userInput[0].upper()
    userNum = int(userInput[1:]) - 2
    if(not('B' <= userLetter <= 'O')):
        print("That is not a valid location")
        return
    if(not(0 <= userNum <= 27)): 
        print("That is not a valid location")
        return
    
    df1 = pd.read_excel(r"Projects-Learning\Python\HuesAndCues\HintsOneWord.xlsx")
    hintsOneWord = pd.DataFrame(df1)
    df2 = pd.read_excel(r"Projects-Learning\Python\HuesAndCues\HintsTwoWords.xlsx")
    hintsTwoWord = pd.DataFrame(df2)
    
    print("One Word")
    print(hintsOneWord[userLetter][userNum])
    print("Two Words")
    print(hintsTwoWord[userLetter][userNum])
    
main()