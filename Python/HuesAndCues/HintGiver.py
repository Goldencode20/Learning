import pandas as pd
import random as rand

def main():
    df = pd.read_excel(r"Projects-Learning\Python\HuesAndCues\HintsOneWord.xlsx")
    hints = pd.DataFrame(df)
    df2 = pd.read_excel(r"Projects-Learning\Python\HuesAndCues\HintsTwoWords.xlsx")
    hintsTwoWord = pd.DataFrame(df2)

    letter = rand.choice('BCDEFGHIJKLMNO')
    num = rand.randrange(0, 27)

    print("One Word")
    print(hints[letter][num])
    print("Two Words")
    print(hintsTwoWord[letter][num])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(letter + str(num + 2))

main()