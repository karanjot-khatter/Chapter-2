#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     08/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#finds the average of 3 exam scores
def main():
    print("Program averages the 3 exam scores")
    score1, score2, score3 = eval(input("Enter 3 scores seprated by commas"))
    Average = (score1 + score2 + score3) / 3
    print("Average of the 3 scores is:", Average)
main()