#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     08/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#average score of 2
#simulataneious assignment - calculates several values at same time
def main():
    print("This program computes the average of 2 scores")
    score1,score2 = eval(input("Enter 2 scores seprated by commas:"))
    average =(score1+score2)/2
    print(" The average score is: ", average)
main()